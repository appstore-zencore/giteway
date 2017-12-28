import os
import subprocess
from .utils import CMD_GIT
from .utils import CMD_CHMOD
from .utils import CMD_CHOWN
from .utils import CMD_MV


def init_repo(name, username, root):
    ownner = "{}:{}".format(username, username)
    subprocess.run([CMD_GIT, "init", name, "--bare"], cwd=root)
    subprocess.run([CMD_CHMOD, "-R", "700", name], cwd=root)
    subprocess.run([CMD_CHOWN, "-R", ownner, name], cwd=root)
    return True


def rename_repo(old_name, new_name, root):
    subprocess.run([CMD_MV,old_name, new_name], cwd=root)
    return True
