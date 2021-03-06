#
# Module automatically generated by Updater v1.0
# @author Daniel J. Finnegan
#

import os
from subprocess import call

USE_FILE_LIST = ['-DUSE_FILE_LIST=ON']
SKIP_CONVERSION = ['-DSKIP_CONVERSION=ON']
USE_SPEC_PAGES = ['-DUSE_SPEC_PAGES=ON']
USE_BEAMER = ['-DUSE_BEAMER=ON']

# Default implementation just calls cmake
# Reimplement as you see fit
def build_full_package(project_root, use_file, skip_conversion, page_spec, is_beamer):
	if not os.path.isdir(os.path.join(project_root, 'bin')):
		os.mkdir(os.path.join(project_root, 'bin'))

	os.chdir(os.path.join(project_root, 'bin'))

	CMAKE_ARGS = []
	if use_file:
		CMAKE_ARGS = CMAKE_ARGS + USE_FILE_LIST

	if skip_conversion:
		CMAKE_ARGS = CMAKE_ARGS + SKIP_CONVERSION

	if page_spec:
		CMAKE_ARGS = CMAKE_ARGS + USE_SPEC_PAGES

	if is_beamer:
		CMAKE_ARGS = CMAKE_ARGS + USE_BEAMER

	# if use_file:
	# 	call(['cmake'] + UPDATER_CMAKE_ARGS + ['..'])
	# else:
	# 	call(['cmake'] + ['..'])

	print (CMAKE_ARGS)

	call (['cmake'] + CMAKE_ARGS + ['..'])
	call(['cmake', '--build', '.'])

####################################################################
