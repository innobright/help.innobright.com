import os

from fabric.api import cd, env, local, parallel, run, settings, sudo, prefix, task
from fabric.contrib.project import rsync_project
from fabric.colors import *

env.hosts = ['alps.innobright.com']

# change cwd to location of the fab file
local_path = os.path.dirname(os.path.abspath(env.real_fabfile)) + os.sep
os.chdir(local_path)
print(green('changing cwd to ' + local_path))

@task
def build():
    print(red("Building Sphinx Website"))
    with virtualenv():
        local("sphinx-build -b dirhtml src build")

@task
def clean():
    local("rm -rf build/*")
    # HACK: Put the README back
    local("git checkout build/README.md")

@task(alias='push')
def deploy():
    build()

    print(red("Deploying help.innobright.com"))
    remote_path = '/srv/help.innobright.com/public'
    rsync_project(
        local_dir='./build/',
        remote_dir=remote_path,
        exclude=['.git', '.gitignore', 'fabfile.py*', 'update.sh', 'venv', '__pycache__'],
        )

## virtualenv stuff ##

from contextlib import contextmanager

@contextmanager
def virtualenv():
    with prefix(". venv/bin/activate"):
        yield

@task
def venv():
    # Debian pkgs needed: python3-pip python-pip python-wheel
    local("pyvenv venv")
    with virtualenv():
        local("pip install -r requirements.txt")
