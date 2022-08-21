import getopt
import sys
import os 
import subprocess
import platform
import shutil
from turtle import clone, update
import git 
from git import Repo 
import adr_func



use_adr=0
use_pottery=0
copy_license=0
use_git=1
use_submodules=1
replace_name = None
check_dir="c:/subprojects"


def help():
        print("Usage: deploy_skeleton.sh [optional ags] dest_dir ")
        print("Optional args:")
        print("-a: initialize destination to use adr-tools")
        print(" -p: initialize destination to use pottery")
        print("-l: copy the license file")
        print("-r <name>: Replace template project/app name values with specified name")
        print("-g: Assume non-git environment. Installs submodule files directly.")
        print("-s: Don't use submodules, and copy files directly")
        print("-k : Check directory ")
        exit () 

if (platform.release() == "Darwin"):   
    sed="sed -i ''"
else:
    sed="sed -i"

try :
    opts, args = getopt.getopt(sys.argv[1:], "aplghsrk:")
except:
    print("Error !")
    help()
for o , a in opts:
    if o == "-a" :
        use_adr = 1
    elif o == "-p":
        use_pottery=1
    elif o == "-l":
        copy_license=1
    elif o == "-g":
        use_git=0
        use_submodules=0
    elif o =="-r":
        replace_name=args[0]
    elif o == "-k":
        check_dir=input("CHECK_DIRECTORY : ")
    elif o =="-h":
        help()
        
    else :
        print(f"Invalid option {args[0]}")
        help()



pwd=os.getcwd()
check_path_1= os.path.exists(f"{check_dir}/Tools")
if(check_path_1==False):
    check_dir=os.chdir(f"{check_dir}")
    check_path_1= os.path.exists(f"{check_dir}")
    if(check_path_1==False):
        print("This script must be run from the project skeleton root or the tools/ directory.")
        exit ()


dest_dir=args[0]
dest_path_2= os.path.exists(f"{dest_dir}")
if(dest_path_2==False):
     dest_path_2= os.path.exists(f"{pwd}/{dest_dir}")
     if(dest_path_2==False):
        dest_dir=f"{pwd}/{dest_dir}"
     else:
        print(f"Destination directory {dest_dir} cannot be found. Does it exist?")
        exit()


# Remove .DS_Store files


findCMD = f'find . -name ".DS_Store"'
out = subprocess.Popen(findCMD,shell=True,stdin=subprocess.PIPE
                      ,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
for file in os.listdir("c:"):
        if file.endswith(".DS_Store"):
            shutil.rmtree(file)


core_files="docs src test tools .clang-format .clang-tidy Makefile meson.build meson_options.txt README.md"
git_files=".gitattributes .github .gitignore"

        
submodule_dirs="build"
submodule_urls="git@github.com:embeddedartistry/meson-buildsystem.git"

# Copy skeleton files to the destination

shutil.copytree(core_files,dest_dir)
path = os.path.join(dest_dir, f"{check_dir}") 
os.mkdir(path)
shutil.copytree("subprojects/*.wrap",f"{dest_dir}/subprojects" )
shutil.rmtree(f"{dest_dir}/tools/deploy_skeleton.py")
shutil.rmtree(f"{dest_dir}/tools/download_and_deploy.py")
if (use_git == 1):
    shutil.copytree(git_files,dest_dir)
if (use_submodules==0):
    repo = git.Repo(pwd)
    output = repo.git.submodule('update','--init','--recursive')
    shutil.copytree(submodule_dirs,dest_dir)
if (copy_license == 1):
    shutil.copytree("LICENSE",dest_dir)

## The following operations all take place in the destination directory

os.chdir(dest_dir)

# Initialize Submodules

if (use_submodules==1):
        repo = git.Repo(submodule_urls)
        output = repo.git.submodule('add')
        index=Repo.init(submodule_dirs).index
        index.commit("Add submodules from project skeleton. ")
else :
    findCMD = f'find {submodule_dirs} -name ".git*"'
    out = subprocess.Popen(findCMD,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    for file in os.listdir(submodule_dirs):
        if file.endswith(".git*"):
            shutil.rmtree(submodule_dirs)
if (use_git==1):
    repo.git.add(all=True )
    
    index=Repo.init(submodule_dirs).index
    index.commit("Initial commit of project skeleton files.")

if (replace_name !=""):
    subprocess.Popen(f"{sed} ",f's/PROJECT_NAME/{replace_name}/g "meson.build"')
    replace_name=f"{replace_name}// /_"
    subprocess.Popen(f"{sed} ",f's/PROJECT_NAME/{replace_name}/g "src/app/meson.build"')
    subprocess.Popen(f"{sed} ",f's/PROJECT_NAME/{replace_name}/g "test/meson.build"')
    
    if(use_git==1):
        index=Repo.init(submodule_dirs).index
        index.commit(f"Replace placeholder values in build files with {replace_name} ")
    
if(use_adr==1):
    adr_func.adr_init('/docs')
    if use_git==1:
        repo.git.add(all=True )
        index=Repo.init(submodule_dirs).index
        index.commit("Initiaize adr-tools")

if(use_git==1):
    try:
        repo.git.pull("adham")
        repo.git.push("adham")
    except:
        print("WARNING: git push failed: check repository.")

if(replace_name ==""):
    print("NOTE: Replace the placeholder project name in meson.build")
    print("NOTE: Replace the placeholder application name in src/app/meson.build")
    print("NOTE: Replace the placeholder test application name in test/meson.build")

variable_1=os.path.isfile(f"{dest_dir}/LICENSE")
variable_2=os.path.isfile(f"{dest_dir}/LICENSE.md")

if ( (copy_license==0 and variable_1==False) or variable_2==False):
    print("NOTE: Your project does not have a LICENSE or LICENSE.md file in the project root.")
    

