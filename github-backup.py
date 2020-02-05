from github import Github
import configparser
import subprocess
import time
import os

CONFIG_PATH = 'github-backup.cfg'

def gitp(cwd, *args):
	return subprocess.call(['git'] + list(args), cwd=cwd)

if not os.path.isfile(CONFIG_PATH) : exit(f'Error: Config file {CONFIG_PATH} missing, please create it')

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

start = time.time();

gh = Github(config.get('GitHub', 'token'))

repos = gh.get_user().get_repos()

count = 0
for repo in repos :
	print(repo.full_name)
	count = count + 1
	if not os.path.exists(repo.full_name) :
		gitp('.', 'clone', repo.ssh_url, repo.full_name)
	else :
		gitp(repo.full_name, 'fetch', '--all', '--verbose')
		gitp(repo.full_name, 'reset', '--hard', 'origin/master')

print(f'Completed backup of {count} repositories in {time.time() - start:.1f} seconds')
