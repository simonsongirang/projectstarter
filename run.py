"""Naval Fate.

Usage:
  projectstarter.py [--p=<projectname>] [--burp] [--payload]

Options:
  -h --help           Show this screen.
  --version           Show version.
  --p=<projectname>   Create projects directory.
  --burp              Download Burpsuite configuration files.
  --payload           Download payloads.

"""
from docopt import docopt
import os

def download_payload():
    os.system("git clone https://github.com/simonsongirang/payload_library.git")

def download_setup():
    os.system("git clone https://github.com/simonsongirang/burpsetup.git")

def createproject(pname):
    if !os.path.isdir("projects"):
        os.mkdir("projects")
    os.chdir("projects")

    if !os.path.isdir(pname):
        os.mkdir(pname)
        os.chdir(pname)
        os.mkdir("screenshots")
        os.mkdir("logs")
        os.mkdir("report")
        os.mkdir("documentation")

#def downloadpayload():
#    Repo.clone_from("https://github.com/simonsongirang/payload_library.git")

if __name__ == '__main__':
    arguments = docopt(__doc__, version='v1')
    payload=arguments['--payload']
    burp=arguments['--burp']
    project=arguments['--p']
    os.chdir("..")
    if payload:
        download_payload()
    if burp:
        download_setup()
    if project != None:
        createproject(project)
