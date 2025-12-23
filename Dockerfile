FROM jupyterhub/jupyterhub:latest

# 安裝 authenticator
RUN pip install --no-cache-dir notebook jupyterhub-nativeauthenticator

# 建立一個預設 Linux 使用者（給 admin 用）
RUN useradd -m -s /bin/bash admin
