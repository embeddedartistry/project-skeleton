import os 
import git
import shutil


pwd=os.getcwd()
INITIAL_DIR=pwd
os.mkdir(r"C:\tmp")
os.chdir("C:\\tmp")
git.Git().clone("https://github.com/embeddedartistry/project-skeleton","project-skeleton",depth=1,recursive=True) 
os.chdir(r"C:\tmp\project-skeleton")
os.chdir(r"C:\tmp\project-skeleton\tools")
#os.system("bash tools/deploy_skeleton.sh $@")
exec(open('deploy_skeleton.py').read())
os.chdir("c:")
shutil.rmtree(r"C:\tmp\project-skeleton")
os.chdir(f"{INITIAL_DIR}")






