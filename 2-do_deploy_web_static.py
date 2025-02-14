#!/usr/bin/python3
# Fabric script  generating a .tgz archive from the
# contents of the web_static folder of AirBnB Clone repo
# using the function do_pack
import os
from fabric.api import run, put, env

env.hosts = ['54.237.21.22', '54.172.183.7']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Creating the tar gzipped archive of directory web_static."""
    if os.path.exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            file_name = archive_path.split("/")[1]
            file_name2 = file_name.split(".")[0]
            final_name = "/data/web_static/releases/" + file_name2 + "/"
            run("mkdir -p " + final_name)
            run("tar -xzf /tmp/" + file_name + " -C " + final_name)
            run("rm /tmp/" + file_name)
            run("mv " + final_name + "web_static/* " + final_name)
            run("rm -rf " + final_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + final_name + " /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception as e:
            print("Error:", e)
            return False
