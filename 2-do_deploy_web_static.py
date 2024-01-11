#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.160.88.241', '54.197.75.39']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        ''' Upload a tar archive of an application '''
        put(archive_path, "/tmp/")

        ''' Extract only the file name from the path '''
        file_name = archive_path.split("/")[-1]

        ''' Extract file name without extension '''
        no_exten = file_name.split(".")[0]

        ''' Create the archive to the folder '''
        path = "/data/web_static/releases/"
        static_path = f"{path}{no_exten}"
        run(f"mkdir -p {static_path}")

        ''' Uncompress the archive to the folder '''
        run(f"tar -xzf /tmp/{file_name} -C {static_path}")
        run(f'mv {static_path}/web_static/* {static_path}/')
        run(f'rm -rf {static_path}/web_static')

        ''' Delete the archive from the web server '''
        run(f"rm /tmp/{file_name}")

        ''' Delete the symbolic link /data/web_static/current '''
        run("rm -rf /data/web_static/current")

        ''' Create a new the symbolic link /data/web_static/current '''
        run(f"ln -s {static_path} /data/web_static/current")

        return True
    except:
        return False
