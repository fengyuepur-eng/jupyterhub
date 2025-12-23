import sys
import os

# ⭐ 把 /srv/jupyterhub 加進 Python module path
sys.path.append("/srv/jupyterhub")

from pre_spawn import ensure_system_user


c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"

# 多人可登入
c.Authenticator.allow_all = True

# 管理員
c.Authenticator.admin_users = {"admin"}

# 開放註冊
c.NativeAuthenticator.open_signup = True

# ⭐ 關鍵 hook
c.Spawner.pre_spawn_hook = ensure_system_user
