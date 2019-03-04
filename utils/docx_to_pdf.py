##
## Run this script from cmake's PROJECT_SOURCE_DIR
##

import win32com.client as win32
import os
import argparse

## Taken from https://github.com/python-openxml/python-docx/issues/113
def convert_to_pdf(root_dir, file_name, output_dir_path):
	root, ext = os.path.splitext (file_name)
	input_file_path = os.path.join (os.path.join (root_dir, 'input'), file_name)
	output_file_path = os.path.join (output_dir_path, root) + '.pdf'
	try:
		word = win32.DispatchEx("Word.Application")
		# print ('Opening', input_file_path)
		worddoc = word.Documents.Open(input_file_path)
		# print ('Saving', output_file_path)
		worddoc.SaveAs(output_file_path, FileFormat = 17)
		worddoc.Close()
	except:
		print ('An error occurred when converting the docx file to pdf')
	else:
		word.Quit()

def main (root_dir, output_dir_path, file_list):
	## Convert each file to a pdf using 
	if not os.path.isdir (output_dir_path):
		os.mkdir (output_dir_path)

	for file_name in file_list:
		convert_to_pdf (root_dir, os.path.basename (file_name), output_dir_path) # Absolute paths are passed from cmake

if __name__ == '__main__':
	# root_dir = os.getcwd ()
	parser = argparse.ArgumentParser (description='Convert docx files to pdf')
	parser.add_argument ('files', nargs='+', help='List of files to convert. Specify file name only')
	parser.add_argument ('--output-directory', dest='output_dir', help='Directory in which to save PDFs')
	parser.add_argument ('--working-directory', dest='working_dir', action='store', help='Root directory of this python script')

	args = parser.parse_args ()

	root_dir = os.path.abspath (args.working_dir)
	output_dir_path = os.path.join (root_dir, args.output_dir)
	main(root_dir, output_dir_path, args.files)