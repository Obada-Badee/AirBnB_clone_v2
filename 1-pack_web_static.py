#!/usr/bin/python3

"""Compress the contents of the web_static folder"""
from fabric.api import *
from datetime import datetime


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
