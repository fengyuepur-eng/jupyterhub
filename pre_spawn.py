import pwd
import subprocess
import os

def ensure_system_user(spawner):
    username = spawner.user.name

    try:
        # 如果使用者已存在，pwd.getpwnam 會成功
        pwd.getpwnam(username)
        spawner.log.info(f"System user '{username}' already exists")

    except KeyError:
        # 使用者不存在 → 建立
        spawner.log.warning(f"Creating system user '{username}'")

        subprocess.check_call([
            "useradd",
            "-m",
            "-s", "/bin/bash",
            username
        ])

        # 確保 home 權限正確
        home = f"/home/{username}"
        subprocess.check_call(["chown", "-R", f"{username}:{username}", home])

    # 指定 Notebook 的 HOME
    spawner.environment["HOME"] = f"/home/{username}"
