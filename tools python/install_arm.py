import os 
import platform
import os.path
import wget 
import shutil
import tarfile
import sys 


# pwd 
pwd=os.getcwd()
STARTING_DIR=pwd
# taking arguments from the client 
args=sys.argv[1:]
if (args[0]==None):
    TOOLCHAIN_INSTALL_DIR = "/usr/local/toolchains "
else :
    TOOLCHAIN_INSTALL_DIR = args[0]
#TOOLCHAIN_INSTALL_DIR=input(" Please inssert TOOLCHAIN_INSTALL_DIR :")
if(args[1]==None):
    TOOLCHAIN_DISABLE_SUDO = 0
else :
    TOOLCHAIN_DISABLE_SUDO = args[1]

TOOLCHAIN_SUDO="sudo"

if (TOOLCHAIN_DISABLE_SUDO==1):
    TOOLCHAIN_SUDO = None
OSX_ARM_URL="https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019q4/gcc-arm-none-eabi-9-2019-q4-major-mac.tar.bz2"
LINUX_ARM_URL="https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019q4/gcc-arm-none-eabi-9-2019-q4-major-aarch64-linux.tar.bz2" 

if (platform.release() == "Darwin"):
    ARM_URL = OSX_ARM_URL
    ARM_DIR=os.path.basename(f"{ARM_URL}"+"-mac.tar.bz2")
else:
    ARM_URL=LINUX_ARM_URL
    ARM_DIR=os.path.basename(f"{ARM_URL}"+"-aarch64-linux.tar.bz2")

ARM_ARCHIVE=os.path.basename(f"{ARM_URL}")


###################################
# Download and install dependency #
###################################

os.chdir('c:\\tmp')
wget.download(ARM_URL,'c:\\tmp')
os.makedirs(TOOLCHAIN_INSTALL_DIR,exist_ok=True)
# Move current toolchain if it exists
if (os.path.exists(f'{TOOLCHAIN_INSTALL_DIR}/gcc-arm-none-eabi')==True):
    os.system("sudo su-")
    shutil.rmtree(f"{TOOLCHAIN_INSTALL_DIR}/gcc-arm-none-eabi")
    shutil.move(f'{TOOLCHAIN_INSTALL_DIR}/gcc-arm-none-eabi',f'{TOOLCHAIN_INSTALL_DIR}/gcc-arm-none-eabi-bak')
tar=tarfile.open(f"{ARM_ARCHIVE}")
os.chdir(f"{TOOLCHAIN_INSTALL_DIR}")
a=os.getcwd()
tar.extractall(a) # specify which folder to extract to

tar.close()
shutil.move(f'{TOOLCHAIN_INSTALL_DIR}/{ARM_DIR}',f'{TOOLCHAIN_INSTALL_DIR}/gcc-arm-none-eabi')
os.remove(f"{ARM_ARCHIVE}")
os.chdir(f"{STARTING_DIR}")












