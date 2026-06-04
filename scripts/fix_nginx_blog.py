#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ajusta o vhost nginx de transportes75 para servir os posts da subpasta /blog/.
Troca o rewrite flat (padrao Desmonte75) por try_files que acha blog/<slug>.html.
Faz backup, valida com nginx -t e so recarrega se passar.
"""
import os, time, paramiko

ENV_PATH = r"C:\VPSLOJA\.env"
CONF = "/etc/nginx/sites-available/transportes75.com.br"
OLD = "location /blog/ { rewrite ^/blog/(.+)$ /$1.html last; }"
NEW = "location /blog/ { try_files $uri $uri.html =404; }"

def load_env(path):
    env = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env

env = load_env(ENV_PATH)
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(env["VPS_HOST"], username=env["VPS_USER"], password=env["VPS_PASS"])
sftp = c.open_sftp()

with sftp.open(CONF) as f:
    conf = f.read().decode("utf-8")

if NEW in conf:
    print("Ja estava ajustado (try_files). Nada a fazer.")
elif OLD not in conf:
    print("AVISO: linha esperada nao encontrada. Conteudo /blog/:")
    for ln in conf.splitlines():
        if "blog" in ln:
            print("  >", ln)
else:
    bak = f"{CONF}.bak.{time.strftime('%Y%m%d-%H%M%S')}"
    c.exec_command(f"cp {CONF} {bak}")[1].channel.recv_exit_status()
    print(f"Backup: {bak}")
    with sftp.open(CONF, "w") as f:
        f.write(conf.replace(OLD, NEW))
    print("Config atualizada.")

# valida
_, out, err = c.exec_command("nginx -t")
out.channel.recv_exit_status()
test = (out.read() + err.read()).decode("utf-8", "ignore")
print("--- nginx -t ---")
print(test.strip())
if "test is successful" in test or "syntax is ok" in test:
    _, o2, e2 = c.exec_command("systemctl reload nginx")
    o2.channel.recv_exit_status()
    print("nginx recarregado OK.")
else:
    print("ERRO no nginx -t -- NAO recarreguei. Verifique/restaure o backup.")

sftp.close(); c.close()
