import os
import shutil
from distutils.dir_util import copy_tree


### Commands ###

def production_update_config_js():
	delete_move_file(config_js_production_path, config_js)

def commit_push_front_end(commit_message):
	commit_push(front_end_app_dir, commit_message)

def build_front_end():
	os.system("npm run build")

def development_update_config_js():
	delete_move_file(config_js_development_path, config_js)

def move_build_to_static():
	delete_folder_content(static_dir)
	copy_tree(build_dir, static_dir)
	delete_folder_content(build_dir)

def production_update_application_yml():
	delete_move_file(application_yml_production_path, application_yml)

def commit_push_back_end(commit_message):
	commit_push(back_end_app_dir, commit_message)
	delete_folder_content(static_dir)

def development_update_application_yml():
	delete_move_file(application_yml_development_path, application_yml)



### Utils ###

def delete_move_file(file_path_from, file_path_to):
	os.remove(file_path_to)
	shutil.copyfile(file_path_from, file_path_to)

def delete_folder_content(folder_path):
    shutil.rmtree(folder_path)
    os.makedirs(folder_path)

def commit_push(project, commit_message):
	os.chdir(project)
	os.system("Git add *")
	os.system('Git commit -m "' + commit_message + '"')
	os.system("Git push")



### Paths ###

this_directory = os.getcwd()


front_end_app_dir = "C:/Users/stefa/Documents/Workspaces/Portfolio/react-blog"
config_js = front_end_app_dir + "/src/config.js"
build_dir = front_end_app_dir + "/build"

back_end_app_dir = "C:/Users/stefa/Documents/Workspaces/Portfolio/portfolio"
application_yml = back_end_app_dir + "/src/main/resources/application.yml"
static_dir = back_end_app_dir + "/src/main/resources/static"


application_yml_production_path = this_directory + "/production_files/application.yml"
config_js_production_path = this_directory + "/production_files/config.js"

config_js_development_path = this_directory + "/development_files/config.js"
application_yml_development_path = this_directory + "/development_files/application.yml"