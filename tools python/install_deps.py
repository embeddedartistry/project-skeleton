import os 
import sys 
import getopt

pwd=os.getcwd()
STARTING_DIR=pwd
TOOLCHAIN_INSTALL_DIR="/usr/local/toolchains"
TOOL_INSTALL_DIR="/usr/local/tools"
TOOLCHAIN_DISABLE_SUDO=0
TOOL_DISABLE_SUDO=0


#commands :
UPDATE=0
UPDATE_ENV=0
PIP_UPDATE=None
BREW_COMMAND="install"
APT_COMMAND="install"
TOOLS_SUDO="Sudo"

BREW_PACKAGE=["python3" ,"ninja" ,"wget" ,"gcc@7" ,"gcc@8" ,"gcc@9" ,"llvm" ,"adr-tools" ,"cmocka" ,"pkg-config"]
BREW_PACKAGE.append["vale","doxygen","cppcheck","clang-format","gcovr","lcov","sloccount"]
APT_PACKAGES=["python3" ,"python3-pip", "ninja-build", "wget" ,"build-essential", "clang" ,"lld" ,"llvm"]
APT_PACKAGES.append=["clang-tools", "libcmocka0" ,"libcmocka-dev" ,"pkg-config" ,"sloccount" ,"curl"]
APT_PACKAGES.append=["doxygen", "cppcheck", "gcovr" ,"lcov" ,"clang-format" ,"clang-tidy", "clang-tools"]
APT_PACKAGES.append=["gcc-7" ,"g++-7", "gcc-8" ,"g++-8", "gcc-9" ,"g++-9"]
PIP3_PACKAGES=["meson" ,"lizard" ,"thefuck"]
try :
    opts, args = getopt.getopt(sys.argv[1:], "euhdst")
except:
    print("Error in the getopts function")
for o , a in opts :
    if o=="-d":
        TOOLCHAIN_INSTALL_DIR=input("TOOLCHAIN_INSTALL_DIR : ")
    elif o == "-s":
        TOOL_INSTALL_DIR=input("TOOL_INSTALL_DIR :")
    elif o =="-r":
        TOOLCHAIN_DISABLE_SUDO=input("TOOLCHAIN_DISABLE_SUDO :")
    elif o =="-z":
        TOOL_DISABLE_SUDO=input("TOOL_DISABLE_SUDO :")
    elif o == "-e":
        UPDATE_ENV=1
    elif o == "-u":
        UPDATE=1
        PIP_UPDATE="--upgrade"
        BREW_COMMAND="upgrade"
        APT_COMMAND="upgrade"
	 
    elif o =="-h":
        print("Usage: install_deps.sh [optional ags]")
        print("Optional args:")
        print("-u: Run an update instead of install")
        print(" -e: Include environment setup during install process (.bashrc + .bash_profile)")
        exit()

    else:
        print(f"Invalid option {args[0]}")


if (platform.release() == "Darwin"):
    if(UPDATE==1):
        os.system("brew update")
    else:
        


    




