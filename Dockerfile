FROM jupyterhub/jupyterhub:latest

RUN pip install --no-cache-dir notebook jupyterhub-nativeauthenticator

# useradd 需要這些工具（通常已存在，但保險）
RUN apt-get update && apt-get install -y passwd && rm -rf /var/lib/apt/lists/*
