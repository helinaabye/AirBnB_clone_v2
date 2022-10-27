#!/usr/bin/python3
# A fabric python script that generates a .tgz archive from the contents of the web_static folder

from datetime import datetime
from fabric.api import local


def do_pack():
    """This method creates a tar archive of the directory web_static"""
    date = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year, date.month, date.day, date.hour, date.minute, date.second)

    local("mkdir -p versions")

    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None

    return file
