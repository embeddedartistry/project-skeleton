import getopt
from posixpath import basename
import sys
import platform
import os
import wget
import shutil
import git 

TOOLCHAIN_INSTALL_DIR="/usr/local/toolchains"
TOOL_INSTALL_DIR="/usr/local/tools"

try :
    opts, args = getopt.getopt(sys.argv[1:], "aprs:")
except:
    print("Error in the getopts function")
for o , a in opts:
    if o == "-a" :
        TOOLCHAIN_INSTALL_DIR = input("TOOLCHAIN_INSTALL_DIR :")
    elif o == "-p":
        TOOL_INSTALL_DIR=input("TOOL_INSTALL_DIR :")
    elif o == "-r":
        PATH=input("PATH :")
    elif o == "-s":
        HOME=input("Give Home Directory :")
    else :
        print("erreur + help function ")
    
DEPLOY_URL="https://gist.githubusercontent.com/phillipjohnston/bb95f19d156007f99be4c10c1efdf694/raw/f2f141e31fca0a12eb391e8251efe2ce1f9e68bd/download_and_deploy.sh"
if(platform.release()=="Darwin"):
    os.system(f"cat  {HOME}/.bash_profile")
    if (os.path.isfile("c:/.bash_profile")==True):
        exec(open('c:/.bash_profile').read())

        
PATHMOD=f"{TOOLCHAIN_INSTALL_DIR}/gcc-arm-none-eabi/bin:{TOOL_INSTALL_DIR}/pottery/src"
if (platform.release()=="Darwin"):
    PATHMOD=f"{PATHMOD}:/usr/local/opt/llvm/bin"
else:
    PATHMOD=f"{PATHMOD}:{TOOL_INSTALL_DIR}:adr-tools/src"

os.system(f"cat {HOME}/.bashrc")


################    
# Path Updates #
################
PATH= f"{PATHMOD}:\{PATH}"
os.system(f"export PATH={PATH}")
if(os.path.isdir(f"{HOME}/bin")==True):
    PATH=f"\{HOME}/bin:\{PATH}"

os.system(f"cat  {HOME}/.bashrc")

#########################
# Aliases and Functions #
#########################
pwd=os.getcwd()

def deploy_skeleton():
    INITIAL_DIR=f"\{pwd}"
    os.chdir("c/tmp")
    wget.download(DEPLOY_URL,'c:\\tmp')
    exec(open('download_and_deploy.py').read())
    shutil.rmtree(r"C:\tmp")
    os.chdir(pwd)
os.system("alias init_skeleton='deploy_skeleton -a -p `pwd`'")

def init_repo():
    URL=args[0]
    git.Git().clone(f"{URL}","URL")
    A=URL.rsplit('/', 1).pop()
    os.chdir(f"{A}.git")
    os.system("deploy_skeleton -a -p \${@} `pwd`")

# Skeleton Update Aliases





