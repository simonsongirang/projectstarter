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
from github import Github
#from git import repo

def createproject(pname):
    os.mkdir(pname)
    os.chdir(pname)
    os.mkdir("screenshots")
    os.mkdir("logs")
    os.mkdir("report")

#def downloadpayload():
#    Repo.clone_from("https://github.com/simonsongirang/payload_library.git")

if __name__ == '__main__':
    arguments = docopt(__doc__, version='v1')
    payload=arguments['--payload']
    burp=arguments['--burp']
    project=arguments['--p']
    print (payload)
    print (burp)
    print (project)
