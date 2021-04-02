import os
import sys
import subprocess

def clone(repo):
  curdir = os.getcwd()
  repoName = repo['name']
  repoURL = repo['url']
  print(os.path.dirname(__file__))
  if not repoExists(repoName):
    os.system(f'git clone {repoURL} ./cached/{repoName}')
  elif not useCached(repo):
    os.system(f'rm -rf ./cached/{repoName}')
    os.system(f'git clone {repoURL} ./cached/{repoName}')

  executeFile(repoName)

def repoExists(name):
  try:
    with open(f'./cached/{name}/__init__.py'):
      return True
  except FileNotFoundError:
    return False

def useCached(repo):
  repoName = repo['name']
  url = repo['url']
  os.chdir(os.path.dirname(__file__) + f'/cached/{repoName}')  # Go to root of repository
  currentHash = subprocess.check_output('git rev-parse HEAD', shell=True).decode('UTF-8').strip()
  latestHash = subprocess.check_output(f'git ls-remote {url} HEAD', shell=True).decode('UTF-8').split('\t')[0].strip()
  print(latestHash)
  if latestHash != currentHash:
    return False
  else:
    return True

def executeFile(name):
  os.chdir(f'./cached/{name}')
  activatefile = './venv/bin/activate_this.py'
  execfile(activatefile, dict(__file__=activatefile))
  os.system('python __init__.py')

if __name__ == '__main__':
  clone({'name':'TestRepo', 'url': 'https://github.com/SonicRift/VBTEST'})