import os 
import git 
import shutil

pwd=os.getcwd()
INITIAL_DIR=pwd
os.mkdir(r"C:\tmp")
os.chdir("C:\\tmp")

git.Git().clone("https://github.com/embeddedartistry/config-files","config-files",depth=1)
os.chdir("C:\\tmp\\config-files")
exec(open('copy_config.sh').read())
os.listdir()
os.chdir("C:\\tmp")
shutil.rmtree(r"C:\tmp\config-files")
os.chdir(f"{INITIAL_DIR}")




