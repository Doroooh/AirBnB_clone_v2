#!/usr/bin/python3
"""
do_pack(): Generating the .tgz archive from the
contents of the web_static folder
do_deploy(): Distributing an archive to a web server
deploy (): Creating and distributing the archive to a web server
do_clean(): Deleting out-of-date archives
"""

from fabric.operations import local, run, put, sudo
from datetime import datetime
import os
from fabric.api import env
import re


env.hosts = ['54.237.21.22', '54.172.183.7']


def do_pack():
    """Function that compresses the files in the archive"""
    local("mkdir -p versions")
    filename = "versions/web_static_{}.tgz".format(datetime.strftime(
                                                   datetime.now(),
                                                   "%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static"
                   .format(filename))
    if result.failed:
        return None
    return filename


def do_deploy(archive_path):
    """Function for distributing an archive to a server"""
    if not os.path.exists(archive_path):
        return False
    rex = r'^versions/(S+).tgz'
    match = re.search(rex, archive_path)
    filename = match.group(1)
    res = put(archive_path, "/tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("mkdir -p /data/web_static/releases/{}/".format(filename))
    if res.failed:
        return False
    res = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm /tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("mv /data/web_static/releases/{}"
              "/web_static/* /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/releases/{}/web_static"
              .format(filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/current")
    if res.failed:
        return False
    res = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(filename))
    if res.failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """Creating and distributing the archive to a web server"""
    filepath = do_pack()
    if filepath is None:
        return False
    r = do_deploy(filepath)
    return r


def do_clean(number=0):
    """Deleting out-of-date archives"""
    files = local("ls -1t versions", capture=True)
    file_names = files.split(" ")
    f = int(number)
    if f in (0, 1):
        f = 1
    for t in file_names[n:]:
        local("rm versions/{}".format(t))
    dir_server = run("ls -1t /data/web_static/releases")
    dir_server_names = dir_server.split(" ")
    for t in dir_server_names[f:]:
        if t is 'test':
            continue
        run("rm -rf /data/web_static/releases/{}"
            .format(t))
