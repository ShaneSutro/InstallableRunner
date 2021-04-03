import os
import sys
import subprocess

def clone(repo):
  repoName = repo['name']
  repoURL = repo['url']
  print(os.path.dirname(__file__))
  if not repoExists(repoName):
    os.system(f'git clone {repoURL} ./cached/{repoName}')
  else:
    try:
      updateCache(repoName)
    except Exception as e:
      print(e)
      os.system(f'rm -rf ./cached/{repoName}')
      os.system(f'git clone {repoURL} ./cached/{repoName}')

  executeFile(repoName)

def repoExists(name):
  try:
    with open(f'./cached/{name}/__init__.py'):
      return True
  except FileNotFoundError:
    return False

def updateCache(name):
  os.chdir(os.path.dirname(__file__) + f'/cached/{name}')  # Go to root of repository
  os.system('git fetch')
  currentHash = subprocess.check_output('git rev-parse HEAD', shell=True).decode('UTF-8').strip()
  remoteHash = subprocess.check_output('git log origin -1', shell=True).decode('UTF-8').split('\n')[0].split(' ')[1]
  if currentHash != remoteHash:
    os.system('git merge')

  os.chdir(os.path.dirname(__file__)) #Switch back to main directory

def executeFile(name):
  os.chdir(f'./cached/{name}')
  activatefile = './venv/bin/activate_this.py'
  execfile(activatefile, dict(__file__=activatefile))
  os.system('python __init__.py')

if __name__ == '__main__':
  clone({'name':'TestRepo', 'url': 'https://github.com/SonicRift/VBTEST'})