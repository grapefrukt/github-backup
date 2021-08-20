from github import Github
import configparser
import subprocess
import time
import os

CONFIG_PATH = 'github-backup.cfg'

def gitp(cwd, *args):
	#print('git ' + cwd + ' ' + str(list(args)))
	return subprocess.call(['git'] + list(args), cwd=cwd)

if not os.path.isfile(CONFIG_PATH) : exit('Error: Config file ' + CONFIG_PATH + 'is missing, please create it')

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

start = time.time();

gh = Github(config.get('GitHub', 'token'))

repos = gh.get_user().get_repos()

prefix = 'https://' + config.get('GitHub', 'username') + ':' + config.get('GitHub', 'token') + '@'

count = 0
for repo in repos :
	print(repo.full_name)
	count = count + 1
	if not os.path.exists('repos/' + repo.full_name) :
		url = repo.clone_url
		url = url.replace('https://', prefix)
		gitp('.', 'clone', url, 'repos/' + repo.full_name)
	else :
		gitp('repos/' + repo.full_name, 'fetch', '--all', '--verbose')
		gitp('repos/' + repo.full_name, 'reset', '--hard')

print('Completed backup of ' + str(count) + ' repositories in ' + str(int(time.time() - start)) + ' seconds')
