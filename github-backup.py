# hack to use pygithub3 from the submodule (while waiting for a fix)
import sys
sys.path.append('pygithub3')

from pygithub3 import Github
import ConfigParser
import subprocess
import time
import os

CONFIG_PATH = 'github-backup.cfg'

def gitp(cwd, *args):
	return subprocess.call(['git'] + list(args), cwd=cwd)

if not os.path.isfile(CONFIG_PATH) : exit('Error: Config file {0} missing, please create it'.format(CONFIG_PATH))

config = ConfigParser.ConfigParser()
config.read(CONFIG_PATH)

start = time.time();

gh = Github(login=config.get('GitHub', 'username'), token=config.get('GitHub', 'token'))

user = gh.users.get()
repos = gh.repos.list().all()

for repo in repos :
	print repo.full_name
	if not os.path.exists(repo.full_name) :
		gitp('.', 'clone', repo.ssh_url, repo.full_name)
	else :
		gitp(repo.full_name, 'fetch', '--all', '--verbose')
		gitp(repo.full_name, 'reset', '--hard', 'origin/master')
	
print 'Completed backup in {0:.2f} seconds'.format(time.time() - start)