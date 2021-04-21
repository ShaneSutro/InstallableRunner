import os, sys

sys.path.append(os.getcwd() + '/database')
from db import client as db

def register(repo):
  urlElements = repo['url'].split('/')
  repoUserName = urlElements[len(urlElements) - 2:len(urlElements) - 1][0]
  repoName = urlElements[len(urlElements) - 1:len(urlElements)][0]

  db.installables.insert_one({'name': f'{repoUserName}/{repoName}', 'url': repo['url']})

  # db.installables.find_one_and_update({'name': f'{repoUserName}/{repoName}'}, {'$set': {'id':23}})

if __name__ == '__main__':
  register({'name':'VBTEST', 'url': 'https://github.com/SonicRift/VBTEST'})