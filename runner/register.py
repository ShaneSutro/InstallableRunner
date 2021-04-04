import os, sys
import hashlib

sys.path.append(os.getcwd() + '/database')
from db import client as db

def register(repo):
  urlElements = repo['url'].split('/')
  repoUserName = urlElements[len(urlElements) - 2:len(urlElements) - 1][0]
  repoName = urlElements[len(urlElements) - 1:len(urlElements)][0]

  db.client.insert_one({'name': f'{repoUserName}/{repoName}'})

  combined = (repoUserName + repoName).encode()

  hashed = hashlib.blake2s(combined).hexdigest() #Database ID Value based on repoUserName and repoName

if __name__ == '__main__':
  register({'name':'TestRepo', 'url': 'https://github.com/SonicRift/VBTEST'})