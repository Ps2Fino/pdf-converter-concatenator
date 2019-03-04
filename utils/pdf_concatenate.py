##
## Creates a tex file for input to pdflatex.
##

import os
import argparse

TEX_HEADER = """
%%
%% Template for concatentating pdf files together
%% @author Daniel J. Finnegan
%%

\\documentclass{article}

\\usepackage[utf8]{inputenc}
\\usepackage{pdfpages}

\\begin{document}

%% \\includepdf[landscape=true,pages={1,2,3}]{file.pdf} %% For individual pages.
"""

TEX_FOOTER = """
\\end{document}
"""

TEX_FILE_INSERT = """\\includepdf[pages=-]{@PDF_DIR@/@FILE_NAME@.pdf}
"""

## Simply writes the tex file, replacing the template for the files passed to the program
def main (root_dir, pdf_dir, file_list):
    tex_file_content = TEX_HEADER
    for file_name in file_list:
        root, ext = os.path.splitext (os.path.basename (file_name)) # Complete paths are passed into the program from cmake
        build_folder = TEX_FILE_INSERT.replace ('@PDF_DIR@', pdf_dir)
        tex_file_content = tex_file_content + build_folder.replace ('@FILE_NAME@', root)
        # print (insert_string)

    tex_file_content = tex_file_content + TEX_FOOTER
    # print (tex_file_content)
    tex_file_path = os.path.join (os.path.join (root_dir, 'src'), 'main.tex')
    with open (tex_file_path, 'w') as fp:
        fp.write (tex_file_content)

    # print ('Done')

if __name__ == '__main__':
    # root_dir = os.getcwd ()
    parser = argparse.ArgumentParser (description='Generates a tex file specifying pdf files to concatentate together')
    parser.add_argument ('files', nargs='+', help='List of files to convert. Specify file name only')
    parser.add_argument ('--working-directory', dest='working_dir', action='store', help='Root directory of this python script')
    parser.add_argument ('--pdf-directory', dest='pdf_dir', action='store', help='Directory containing the PDFs')

    args = parser.parse_args ()
    root_dir = os.path.abspath (args.working_dir)
    main(root_dir, args.pdf_dir, args.files)