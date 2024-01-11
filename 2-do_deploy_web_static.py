#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
"""

from fabric.api import local, env, put, run
from datetime import datetime
from os.path import isdir
env.hosts = ['54.160.88.241', '54.197.75.39']


def do_pack():
    """ make tgz archive file """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir('versions'):
            local("mkdir versions")
        file_path = f"versions/web_static_{date}.tgz"
        local(f"tar -cvzf {file_path} web_static")
        return file_path
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        return False
