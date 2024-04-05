#!/usr/bin/python3
"""Deploy the static contents"""
from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['100.24.240.126', '54.157.134.215']


@runs_once
def do_pack():
    """Create the .tgz file"""
    now = datetime.now()
    file_name = (f"versions/web_static_{now.year}{now.month}"
                 f"{now.day}{now.hour}{now.minute}{now.second}.tgz")
    full_command = f"tar -cvzf {file_name} web_static/"
    local("mkdir -p versions")
    command = local(full_command)
    if (command.succeeded):
        return file_name


def do_deploy(archive_path):
    """Deploy the static contents to the server"""
    if exists(archive_path) is False:
        return False
    try:
        file_with_extenstion = archive_path.split("/")[-1]
        file_name = file_with_extenstion.split(".")[0]
        extraction_path = f'/data/web_static/releases/{file_name}/'
        extracted_content = f'{extraction_path}/web_static/*'
        put(archive_path, '/tmp/')
        run(f"mkdir -p {extraction_path}")
        run(f"tar -xzf /tmp/{file_with_extenstion} -C {extraction_path}")
        run(f"rm /tmp/{file_with_extenstion}")
        run(f'mv {extracted_content} {extraction_path}')
        run(f'rm -rf {extraction_path}/web_static/')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {extraction_path} /data/web_static/current')
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Do a comlete deployment"""
    try:
        archive_path = do_pack()
        return do_deploy(archive_path)
    except Exception:
        return False
