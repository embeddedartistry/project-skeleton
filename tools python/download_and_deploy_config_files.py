import os 
import git 
import shutil
import platform

pwd=os.getcwd()
initial_dir=pwd
linux_dir="/tmp"
windows_dir="C:\\tmp"
if (platform.system() == "Darwin" or platform.system() == "Linux" ):

    temporary_dir=linux_dir
    os.mkdir(temporary_dir)
    os.chdir(temporary_dir)
    git.Git().clone("https://github.com/embeddedartistry/config-files","config-files",depth=1)
    os.chdir(f"{temporary_dir}\config-files")
    exec(open('copy_config.sh').read())
    os.chdir(temporary_dir)
    shutil.rmtree(f"{temporary_dir}\config-files")
    os.chdir(f"{initial_dir}")

else :
    temporary_dir=windows_dir
    os.mkdir(temporary_dir)
    os.chdir(temporary_dir)
    git.Git().clone("https://github.com/embeddedartistry/config-files","config-files",depth=1)
    os.chdir(f"{temporary_dir}\\config-files")
    exec(open('copy_config.sh').read())
    os.chdir(temporary_dir)
    shutil.rmtree(f"{temporary_dir}\\config-files")
    os.chdir(f"{initial_dir}")




