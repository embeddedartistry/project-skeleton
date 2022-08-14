import getopt
import sys
import os 
import subprocess
import platform
import shutil
from turtle import update
import git 
from git import Repo 


USE_ADR=0
USE_POTTERY=0
COPY_LICENSE=0
USE_GIT=1
USE_SUBMODULES=1
REPLACE_NAME = None

def help():
        print("Usage: deploy_skeleton.sh [optional ags] dest_dir ")
        print("Optional args:")
        print("-a: initialize destination to use adr-tools")
        print(" -p: initialize destination to use pottery")
        print("-l: copy the license file")
        print("-r <name>: Replace template project/app name values with specified name")
        print("-g: Assume non-git environment. Installs submodule files directly.")
        print("-s: Don't use submodules, and copy files directly")
        exit () 

if (platform.release() == "Darwin"):   
    SED="sed -i ''"
else:
    SED="sed -i"

try :
    opts, args = getopt.getopt(sys.argv[1:], "aplghsr:")
except:
    print("Error in the getopts function")
for o , a in opts:
    if o == "-a" :
        USE_ADR = 1
    elif o == "-p":
        USE_POTTERY=1
    elif o == "-l":
        COPY_LICENSE=1
    elif o == "-g":
        USE_GIT=0
        USE_SUBMODULES=0
    elif o =="-r":
        REPLACE_NAME=args[0]
    elif o =="-h":
        help()
        
    else :
        print(f"Invalid option {args[0]}")
        help()

#variable=len(opts)
#for i in range(1,variable) :
#   del opts[i]

CHECK_DIR="c:/subprojects"
pwd=os.getcwd()
CHECK_PATH_1= os.path.exists(f"{CHECK_DIR}/Tools")
if(CHECK_PATH_1==False):
    CHECK_DIR=os.chdir(f"{CHECK_DIR}")
    CHECK_PATH_1= os.path.exists(f"{CHECK_DIR}")
    if(CHECK_PATH_1==False):
        print("This script must be run from the project skeleton root or the tools/ directory.")
        exit ()


DEST_DIR=args[0]
DEST_PATH_2= os.path.exists(f"{args[0]}")
if(DEST_PATH_2==False):
     DEST_PATH_2= os.path.exists(f"{pwd}/{args[0]}")
     if(DEST_PATH_2==False):
        DEST_DIR=f"{pwd}/{args[0]}"
     else:
        print(f"Destination directory {DEST_DIR} cannot be found. Does it exist?")
        exit()


# Remove .DS_Store files


findCMD = f'find . -name ".DS_Store"'
out = subprocess.Popen(findCMD,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
for file in os.listdir("c:"):
        if file.endswith(".DS_Store"):
            shutil.rmtree(file)


CORE_FILES="docs src test tools .clang-format .clang-tidy Makefile meson.build meson_options.txt README.md"
GIT_FILES=".gitattributes .github .gitignore"

        
SUBMODULE_DIRS="build"
SUBMODULE_URLS="git@github.com:embeddedartistry/meson-buildsystem.git"

# Copy skeleton files to the destination

shutil.copytree(CORE_FILES,DEST_DIR )
path = os.path.join(DEST_DIR, f"{CHECK_DIR}") 
os.mkdir(path)
shutil.copytree("subprojects/*.wrap",f"{DEST_DIR}/subprojects" )
shutil.rmtree(f"{DEST_DIR}/tools/deploy_skeleton.py")
shutil.rmtree(f"{DEST_DIR}/tools/download_and_deploy.py")
if (USE_GIT == 1):
    shutil.copytree(GIT_FILES,DEST_DIR)
if (USE_SUBMODULES==0):
    repo = git.Repo(pwd)
    output = repo.git.submodule('update','--init','--recursive')
    shutil.copytree(SUBMODULE_DIRS,DEST_DIR)
if (COPY_LICENSE == 1):
    shutil.copytree("LICENSE",DEST_DIR)

## The following operations all take place in the destination directory

os.chdir(DEST_DIR)

# Initialize Submodules

if (USE_SUBMODULES==1):
        repo = git.Repo(SUBMODULE_URLS)
        output = repo.git.submodule('add')
        index=Repo.init(SUBMODULE_DIRS).index
        index.commit("Add submodules from project skeleton. ")
else :
    find = f'find {SUBMODULE_DIRS} -name ".git*"'
    out = subprocess.Popen(findCMD,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    for file in os.listdir(SUBMODULE_DIRS):
        if file.endswith(".git*"):
            shutil.rmtree(SUBMODULE_DIRS)
if (USE_GIT==1):
    repo.git.add(all=True )
    index=Repo.init(SUBMODULE_DIRS).index
    index.commit("Initial commit of project skeleton files.")

if (REPLACE_NAME !=""):
    p=subprocess.Popen(f"{SED}")