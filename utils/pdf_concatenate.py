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

TEX_FILE_INSERT = """\\includepdf[pages=-]{build/@FILE_NAME@.pdf}
"""

## Simply writes the tex file, replacing the template for the files passed to the program
def main (root_dir, file_list):
    tex_file_content = TEX_HEADER
    for file_name in file_list:
        root, ext = os.path.splitext (file_name)
        tex_file_content = tex_file_content + TEX_FILE_INSERT.replace ('@FILE_NAME@', root)
        # print (insert_string)

    tex_file_content = tex_file_content + TEX_FOOTER
    # print (tex_file_content)
    tex_file_path = os.path.join (os.path.join (root_dir, 'src'), 'main.tex')
    with open (tex_file_path, 'w') as fp:
        fp.write (tex_file_content)

    # print ('Done')

if __name__ == '__main__':
    root_dir = os.getcwd ()
    parser = argparse.ArgumentParser (description='Generates a tex file specifying pdf files to concatentate together')
    parser.add_argument ('files', nargs='+', help='List of files to convert. Specify file name only')

    args = parser.parse_args ()
    main(root_dir, args.files)