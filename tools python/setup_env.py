import getopt
import sys
import platform
import os 

TOOLCHAIN_INSTALL_DIR="/usr/local/toolchains"
TOOL_INSTALL_DIR="/usr/local/tools"

try :
    opts, args = getopt.getopt(sys.argv[1:], "ap:")
except:
    print("Error in the getopts function")
for o , a in opts:
    if o == "-a" :
        TOOLCHAIN_INSTALL_DIR = input("TOOLCHAIN_INSTALL_DIR :")
    elif o == "-p":
        TOOL_INSTALL_DIR=input("TOOL_INSTALL_DIR :")
    else :
        print("erreur")
    
DEPLOY_URL="https://gist.githubusercontent.com/phillipjohnston/bb95f19d156007f99be4c10c1efdf694/raw/f2f141e31fca0a12eb391e8251efe2ce1f9e68bd/download_and_deploy.sh"
if(platform.release()=="Darwin"):
    os.system(r"cat << ENDOFBLOCK >> c:/.bash_profile")
    if (os.path.isfile("c:/.bash_profile")==True):
        


