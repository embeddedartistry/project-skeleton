import os 
import sys 
import getopt
import platform
import subprocess
import requests


pwd=os.getcwd()
starting_dir=pwd
toolchain_install_dir="/usr/local/toolchains"
tool_install_dir="/usr/local/tools"
toolchain_disable_sudo=0
tool_disable_sudo=0


#commands :
update=0
update_env=0
pip_update=None
brew_command="install"
apt_command="install"
tools_sudo="Sudo"

brew_package=["python3" ,"ninja" ,"wget" ,"gcc@7" ,"gcc@8" ,"gcc@9" ,"llvm" ,"adr-tools" ,"cmocka" ,"pkg-config"]
brew_package.append["vale","doxygen","cppcheck","clang-format","gcovr","lcov","sloccount"]
apt_package=["python3" ,"python3-pip", "ninja-build", "wget" ,"build-essential", "clang" ,"lld" ,"llvm"]
apt_package.append=["clang-tools", "libcmocka0" ,"libcmocka-dev" ,"pkg-config" ,"sloccount" ,"curl"]
apt_package.append=["doxygen", "cppcheck", "gcovr" ,"lcov" ,"clang-format" ,"clang-tidy", "clang-tools"]
apt_package.append=["gcc-7" ,"g++-7", "gcc-8" ,"g++-8", "gcc-9" ,"g++-9"]
pip3_package=["meson" ,"lizard" ,"thefuck"]
try :
    opts, args = getopt.getopt(sys.argv[1:], "euhdst")
except:
    print("Error in the getopts function")
for o , a in opts :
    if o=="-d":
        toolchain_install_dir=input("TOOLCHAIN_INSTALL_DIR : ")
    elif o == "-s":
        tool_install_dir=input("TOOL_INSTALL_DIR :")
    elif o =="-r":
        toolchain_disable_sudo=input("TOOLCHAIN_DISABLE_SUDO :")
    elif o =="-z":
        TOOL_DISABLE_SUDO=input("TOOL_DISABLE_SUDO :")
    elif o == "-e":
        update_env=1
    elif o == "-u":
        update=1
        pip_update="--upgrade"
        brew_command="upgrade"
        apt_command="upgrade"
	 
    elif o =="-h":
        print("Usage: install_deps.sh [optional ags]")
        print("Optional args:")
        print("-u: Run an update instead of install")
        print(" -e: Include environment setup during install process (.bashrc + .bash_profile)")
        exit()

    else:
        print(f"Invalid option {args[0]}")


if (platform.system() == "Darwin"):
    if(update==1):
            os.system("brew update")
    else:
            print("installing the Homebrew ...")
            r = requests.get('https://raw.githubusercontent.com/Homebrew/install/master/install.sh')
            r.status_code
    os.system("brew tap homebrew/cask-versions")

    subprocess.Popen(['brew',brew_command,brew_package],shell=True)
    subprocess.Popen(['pip3','install',pip3_package,pip_update],shell=True)
else:
    os.system("sudo apt-get update ")





    
        
        


    




