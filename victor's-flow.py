import sys
import os

from utils import *

def main():

	production_update_config_js()

	commit_push_front_end(sys.argv[1])

	build_front_end()

	move_build_to_static()

	development_update_config_js()

	production_update_application_yml()

	commit_push_back_end(sys.argv[1])

	development_update_application_yml()

if __name__ == '__main__':
	main()