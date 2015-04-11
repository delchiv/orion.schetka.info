# coding: utf-8

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://github.com/delchiv/schetka.info.git'

def deploy():
    site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
#    _get_latest_source(source_folder)
#    _update_settings(source_folder, env.host)
#    _update_virtualenv(source_folder)
#    _update_static_files(source_folder)
#    _update_database(source_folder)

def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('db', 'static', 'media', 'virtualenv', 'src'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))

def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'): 
        run('cd %s && git fetch' % (source_folder,))  
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))  
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))

def _update_virtualenv(source_folder, user):
    virtualenv_folder = source_folder + '/../../%s_env' % (user,)
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.list' % (
            virtualenv_folder, source_folder
    ))

def _update_static_files(source_folder, user):
    run('cd %s && ../../%s_env/bin/python manage_viola.py collectstatic --noinput' % (source_folder, user,))
    run('cd %s && ../../%s_env/bin/python manage_ijewel.py collectstatic --noinput' % (source_folder, user,))

def _update_database(source_folder, user):
    run('cd %s && ../../%s_env/bin/python manage_viola.py migrate --noinput' % (source_folder, user,))
    run('cd %s && ../../%s_env/bin/python manage_ijewel.py migrate --noinput' % (source_folder, user,))

def _update_locales(source_folder, user):
    run('cd %s/viola && ../../../%s_env/bin/python ../manage_viola.py compilemessages --settings=viola_com_ua.settings.local' % (source_folder, user,))
    run('cd %s/ijewel && ../../../%s_env/bin/python ../manage_ijewel.py compilemessages --settings=ijewel_ua.settings.local' % (source_folder, user,))

def _restart_apps():
    sudo('service nginx reload')
    sudo('restart viola.com.ua')
    sudo('restart ijewel.ua')


