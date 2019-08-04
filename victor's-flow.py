import os
import sys
import shutil
from distutils.dir_util import copy_tree

react_app_dir = "C:/Users/stefa/Documents/Workspaces/Portfolio/react-blog"
react_app_build_dir = react_app_dir + "/build"

portfolio_app_dir = "C:/Users/stefa/Documents/Workspaces/Portfolio/portfolio"
portfolio_app_static_dir = portfolio_app_dir + "/src/main/resources/static"

commit_message = "stefantflc.me - generic commit message - there is an error on victor's flow"

def main():

	commit_push(react_app_dir)

	os.system("npm run build")

	delete_folder_content(portfolio_app_static_dir)

	copy_tree(react_app_build_dir, portfolio_app_static_dir)

	delete_folder_content(react_app_build_dir)

	commit_push(portfolio_app_dir)
	
def delete_folder_content(folder_path):
    shutil.rmtree(folder_path)
    os.makedirs(folder_path)

def commit_push(project):
	os.chdir(project)
	os.system("Git add *")
	os.system('Git commit -m "' + commit_message + '"')
	os.system("Git push")

if __name__ == '__main__':
	commit_message = sys.argv[1]
	main()