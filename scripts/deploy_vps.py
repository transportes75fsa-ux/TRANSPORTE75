#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deploy Transportes75 -> VPS Contabo (/var/www/transportes75).

- Le credenciais de C:\\VPSLOJA\\.env (VPS_HOST/VPS_USER/VPS_PASS) -- nada hardcoded.
- Sobe via SFTP os arquivos do site (HTML, blog/, img/, dist/, robots.txt, sitemap.xml).
- Pula scripts de build/dev, .git, docs, src, arquivos .py/.md/.log e teste-*.html.
- Ajusta dono/permissoes (www-data, 755/644).

NAO mexe no nginx aqui -- isso e feito em passo separado e verificado.
"""
import os
import sys
import posixpath
import paramiko

BASE_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # ...\sitetransportes75
REMOTE_ROOT = "/var/www/transportes75"
ENV_PATH   = r"C:\VPSLOJA\.env"

def load_env(path):
    env = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env

env = load_env(ENV_PATH)
HOST = env["VPS_HOST"]; USER = env["VPS_USER"]; PASS = env["VPS_PASS"]

SKIP_DIRS  = {".git", "__pycache__", "node_modules", "scripts", "src", "docs"}
SKIP_FILES = {".gitignore", "STATUS.md", "README.md"}
SKIP_EXTS  = {".py", ".log", ".md", ".pyc"}

def keep(filename):
    if filename in SKIP_FILES:
        return False
    if filename.startswith("teste-"):
        return False
    _, ext = os.path.splitext(filename)
    if ext.lower() in SKIP_EXTS:
        return False
    return True

def ensure_remote_dir(sftp, path):
    try:
        sftp.stat(path)
    except IOError:
        sftp.mkdir(path)

def main():
    print(f"Deploy Transportes75 -> {USER}@{HOST}:{REMOTE_ROOT}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, username=USER, password=PASS)
    sftp = client.open_sftp()

    ensure_remote_dir(sftp, REMOTE_ROOT)

    total = 0
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel = os.path.relpath(root, BASE_DIR).replace("\\", "/")
        remote_path = REMOTE_ROOT if rel == "." else posixpath.join(REMOTE_ROOT, rel)
        ensure_remote_dir(sftp, remote_path)
        for fn in files:
            if not keep(fn):
                continue
            local_file  = os.path.join(root, fn)
            remote_file = posixpath.join(remote_path, fn)
            sftp.put(local_file, remote_file)
            total += 1
            shown = fn if rel == "." else f"{rel}/{fn}"
            print(f"  UP  {shown}")

    print(f"\n{total} arquivos enviados.")

    for cmd in (
        f"chown -R www-data:www-data {REMOTE_ROOT}",
        f"find {REMOTE_ROOT} -type d -exec chmod 755 {{}} +",
        f"find {REMOTE_ROOT} -type f -exec chmod 644 {{}} +",
    ):
        client.exec_command(cmd)[1].channel.recv_exit_status()
    print("Permissoes ajustadas (www-data, 755/644).")

    sftp.close()
    client.close()

if __name__ == "__main__":
    main()
