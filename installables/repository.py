import os
import sys
import subprocess
import json

def run(repo):
  repoName = repo['name']
  repoURL = repo['url']
  print(os.path.dirname(__file__))
  if not repoExists(repoName):
    os.system(f'git clone {repoURL} ./cached/{repoName}')
  else:
    try:
      updateCache(repoName)
    except Exception as e:
      print(os.getcwd())
      print(e)
      os.system(f'rm -rf ./cached/{repoName}')
      os.system(f'git clone {repoURL} ./cached/{repoName}')

  getFields(repo)
  executeFile(repoName)

def repoExists(name):
  try:
    with open(f'./cached/{name}/run.py'):
      return True
  except FileNotFoundError:
    return False

def updateCache(name):
  os.chdir(f'./cached/{name}')  # Go to root of repository
  print(os.getcwd())
  os.system('git fetch')
  currentHash = subprocess.check_output('git rev-parse HEAD', shell=True).decode('UTF-8').strip()
  remoteHash = subprocess.check_output('git log origin -1', shell=True).decode('UTF-8').split('\n')[0].split(' ')[1]
  if currentHash != remoteHash:
    os.system('git merge origin')

  os.chdir(os.path.dirname(__file__))  #Switch back to main directory
  os.chdir('..')
  print(os.getcwd())

def executeFile(name):
  os.chdir(f'./cached/{name}')
  sys.path.append(os.getcwd())
  activatefile = './venv/bin/activate_this.py'
  try:
    execfile(activatefile, dict(__file__=activatefile))
  except FileNotFoundError:
    message = 'The virtualenv is not configured correctly.'
    print(message)
    return message
  try:
    import run
    runValue = run.main({'user': 'user'}, {'dev': 'dev'})
  except (ModuleNotFoundError, AttributeError, TypeError):
    message = 'The script should be named "run.py" and should have a function called "main," accepting 2 arguments.'
    print(message)
    return message
  print(runValue)

def getFields(repo):
  name = repo['name']
  try:
    with open(f'./cached/{name}/vbconfig.json') as config:
      config = json.loads(config.read())
      print(config)
      return True
  except FileNotFoundError:
    return False

if __name__ == '__main__':
  # arg = json.loads(sys.argv[1]) # Get repo from command line argument
  run({'name':'VBTEST', 'url': 'https://github.com/SonicRift/VBTEST'})