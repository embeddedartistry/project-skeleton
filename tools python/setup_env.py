import getopt
import sys
import platform
import os
import wget
import shutil
import git 

TOOLCHAIN_INSTALL_DIR="/usr/local/toolchains"
TOOL_INSTALL_DIR="/usr/local/tools"

def helpfunction():
        print("Usage: setup_env.py [optional ags] dest_dir ")
        print("Optional args:")
        print("-a: initialize the toolchain install directory")
        print(" -p: initialize TOOL install directory ")
        print("-r: give the path ")
        print("-s: initialize home directory")
        exit() 
try :
    opts, args = getopt.getopt(sys.argv[1:], "aprs:")
except:
    print("An Error has occured !")
    helpfunction()
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
        print("An Error has occured ! ")
        helpfunction()



DEPLOY_URL="https://gist.githubusercontent.com/phillipjohnston/bb95f19d156007f99be4c10c1efdf694/raw/f2f141e31fca0a12eb391e8251efe2ce1f9e68bd/download_and_deploy.sh"
if(platform.system()=="Darwin"):
    file=open('.bash_profile','a')
    file.write("if [ -f \$HOME/.bashrc ]; then")
    file.write("    source \$HOME/.bashrc")
    file.write("fi")
    file.close()

        
PATHMOD=f"{TOOLCHAIN_INSTALL_DIR}/gcc-arm-none-eabi/bin:{TOOL_INSTALL_DIR}/pottery/src"
if (platform.system()=="Darwin"):
    PATHMOD=f"{PATHMOD}:/usr/local/opt/llvm/bin"
else:
    PATHMOD=f"{PATHMOD}:{TOOL_INSTALL_DIR}:adr-tools/src"


file2=open(".bashrc","a")
file2.write("################")
file2.write("# Path Updates #")
file2.write("################")
file2.write("export PATH=${PATHMOD}:\$PATH")
file2.write("# set PATH so it includes user's private bin if it exists")
file2.write("if [ -d \$HOME/bin ] ; then")
file2.write("    PATH=\$HOME/bin:\$PATH")
file2.write("fi")
file2.write("")
file2.write("#########################")
file2.write("# Aliases and Functions #")
file2.write("#########################")
file2.write("function deploy_skeleton()")
file2.write("{")
file2.write("	INITIAL_DIR=\$(pwd)")
file2.write("	cd /tmp")
file2.write("	wget $DEPLOY_URL")
file2.write("	bash download_and_deploy.sh \$@")
file2.write("	rm download_and_deploy.sh")
file2.write("	cd \$INITIAL_DIR")
file2.write("}")
file2.write("alias init_skeleton='deploy_skeleton -a -p `pwd`'")
file2.write("function init_repo()")
file2.write("{")
file2.write("	URL=\$1")
file2.write("	shift")
file2.write("	git clone \$URL")
file2.write('"	cd \$(basename "\$URL" .git)"')
file2.write("	deploy_skeleton -a -p \${@} `pwd`")
file2.write("	deploy_skeleton -a -p \${@} `pwd`")
file2.write("}")
file2.write("")
file2.write('alias sm_update_build="cd build; git checkout master; git pull; cd ../"')
file2.write('alias sm_update_commit_build="sm_update_build; git add build; git commit -m "Update build submodule to use the latest changes."')

























