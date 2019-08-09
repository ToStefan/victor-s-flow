import os
import sys
import shutil
from distutils.dir_util import copy_tree

react_app_dir = "C:/Users/stefa/Documents/Workspaces/Portfolio/react-blog"
react_app_src_dir = react_app_dir + "/src"
react_app_build_dir = react_app_dir + "/build"

portfolio_app_dir = "C:/Users/stefa/Documents/Workspaces/Portfolio/portfolio"
portfolio_app_resource_dir = portfolio_app_dir + "/src/main/resources"
portfolio_app_static_dir = portfolio_app_resource_dir + "/static"
portfolio_util_dir = portfolio_app_dir + "/src/main/java/t/stefan/portfolio/util"

commit_message = "stefantflc.me - generic commit message - there is an error on victor's flow"

def main():

	update_file(react_app_src_dir + "/config.js", heroku_config_js())

	commit_push(react_app_dir)
	
	os.system("npm run build")

	update_file(react_app_src_dir + "/config.js", local_config_js())

	try:
		delete_folder_content(portfolio_app_static_dir)
	except Exception:
		pass

	copy_tree(react_app_build_dir, portfolio_app_static_dir)

	delete_folder_content(react_app_build_dir)

	update_file(portfolio_app_resource_dir + "/application.yml", heroku_app_yml())

	update_file(portfolio_util_dir + "/Constants.java", heroku_constants_java())

	commit_push(portfolio_app_dir)

	update_file(portfolio_app_resource_dir + "/application.yml", local_app_yml())

	update_file(portfolio_util_dir + "/Constants.java", local_constants_java())

def update_file(file_path, file_content):
	f = open(file_path, "w")
	f.write(file_content)
	f.close()
	
def delete_folder_content(folder_path):
    shutil.rmtree(folder_path)
    os.makedirs(folder_path)

def commit_push(project):
	os.chdir(project)
	os.system("Git add *")
	os.system('Git commit -m "' + commit_message + '"')
	os.system("Git push")

# config.js
def heroku_config_js():
	return "const API_URL = \"http://www.stefantflc.me/api\";\n\n" + config_js_end()

def local_config_js():
	return "const API_URL = \"http://localhost:8080/api\";\n\n" + config_js_end()

def config_js_end():
	return "export {\n    API_URL\n}"

# application.yml
def heroku_app_yml():
	return app_yml_start() + "    url: ${SPRING_DATASOURCE_URL}\n    username: ${SPRING_DATASOURCE_USERNAME}\n" \
		+ "    password: ${SPRING_DATASOURCE_PASSWORD}\n" + app_yml_end_heroku()

def local_app_yml():
	return app_yml_start() + "    url: jdbc:mysql://localhost:3306/stefantflcdb\n    username: root\n    password: root\n" + app_yml_end_local()

def app_yml_start():
	return "spring:\n  datasource:\n"

def app_yml_end_local():
	return "  jpa:\n    hibernate:\n      ddl-auto: create\nlogging:\n  level:\n    org:\n      hibernate:\n        SQL: debug"

def app_yml_end_heroku():
	return "  jpa:\n    hibernate:\n      ddl-auto: update\nlogging:\n  level:\n    org:\n      hibernate:\n        SQL: debug"

# Constants.java
def heroku_constants_java():
	return constants_java("http://www.stefantflc.me")

def local_constants_java():
	return constants_java("http://localhost:8080")

def constants_java(base_path):
	file = "package t.stefan.portfolio.util;\n\npublic class Constants {\n    public final static String tokenHeader = \"Authorization\";\n"
	file += "    public final static String jwtSecret = \"secret\";\n    public final static Integer jwtExpirationInMs = 864000000;\n"
	file += "    public final static String appMail = \"stefantflc@gmail.com\";\n"
	file += "    public final static String appMailPass = \"portfolio12345\";\n    public final static String basePath = \""
	file += base_path + "\";\n}"
	return file

if __name__ == '__main__':
	commit_message = sys.argv[1]
	main()