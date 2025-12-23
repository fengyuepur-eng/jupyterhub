c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"

# ✅ JupyterHub 5 必須明確允許登入
c.Authenticator.allow_all = True

# 管理員帳號（登入後才生效）
c.Authenticator.admin_users = {"admin"}

# 開放註冊
c.NativeAuthenticator.open_signup = True
