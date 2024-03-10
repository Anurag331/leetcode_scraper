import configparser
import os
import shutil

config = configparser.ConfigParser()

def createCopyOfConfig():
  mainDirectoryName = os.path.dirname(__file__)
  configPath = os.path.join(os.path.dirname(mainDirectoryName),"config.ini")
  internalConfigPath = os.path.join(mainDirectoryName,"config.ini")
  if os.path.isfile(internalConfigPath):
    print(f"Deleting config.ini file from {mainDirectoryName}")
    os.remove(internalConfigPath)
  shutil.copy(configPath,mainDirectoryName)

def getUserInput():
  config.read("./config.ini")
  config['Constants']['overwrite']


if __name__ == '__main__':
  createCopyOfConfig()
  getUserInput()