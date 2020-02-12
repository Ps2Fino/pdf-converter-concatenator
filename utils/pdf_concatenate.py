##
## Creates a tex file for input to pdflatex.
##

import os
import argparse
import json

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

BEAMER_FILE_INSERT = """\\includepdf[landscape=true, pages=-]{@PDF_DIR@/@FILE_NAME@.pdf}
"""

TEX_FILE_PAGE_INSERT = """\\includepdf[pages={@START_PAGE@-@END_PAGE@}]{@PDF_DIR@/@FILE_NAME@.pdf}
"""

BEAMER_FILE_PAGE_INSERT = """\\includepdf[landscape=true, pages={@START_PAGE@-@END_PAGE@}]{@PDF_DIR@/@FILE_NAME@.pdf}
"""

## Simply writes the tex file, replacing the template for the files passed to the program
def main (root_dir, pdf_dir, file_list, is_beamer):
    tex_file_content = TEX_HEADER

    if args.use_json_spec:
        tex_file_content = base_from_json_spec (root_dir, pdf_dir, tex_file_content, is_beamer)
    else:
        for file_name in file_list:
            root, ext = os.path.splitext (os.path.basename (file_name)) # Complete paths are passed into the program from cmake
            if is_beamer:
                build_folder = BEAMER_FILE_INSERT.replace ('@PDF_DIR@', pdf_dir)
            else:
                build_folder = TEX_FILE_INSERT.replace ('@PDF_DIR@', pdf_dir)
            tex_file_content = tex_file_content + build_folder.replace ('@FILE_NAME@', root)
            # print (insert_string)

    tex_file_content = tex_file_content + TEX_FOOTER
    # print (tex_file_content)
    tex_file_path = os.path.join (os.path.join (root_dir, 'src'), 'main.tex')
    with open (tex_file_path, 'w') as fp:
        fp.write (tex_file_content)

    # print ('Done')

def base_from_json_spec (root_dir, pdf_dir, tex_file_content, is_beamer):
    with open ((os.path.join (root_dir, os.path.join (pdf_dir, 'page_spec.json')))) as jsonfile:
        page_spec = json.load (jsonfile)

    for item in page_spec['items']:
        # print (item)
        filename = item ['filename']
        start = item ['start_page']
        end = item ['end_page']

        if is_beamer:
            item_tex = BEAMER_FILE_PAGE_INSERT.replace ('@PDF_DIR@', pdf_dir)
        else:
            item_tex = TEX_FILE_PAGE_INSERT.replace ('@PDF_DIR@', pdf_dir)
        item_tex = item_tex.replace ('@FILE_NAME@', filename)
        item_tex = item_tex.replace ('@START_PAGE@', start)
        item_tex = item_tex.replace ('@END_PAGE@', end)
        tex_file_content = tex_file_content + item_tex

    return tex_file_content

if __name__ == '__main__':
    # root_dir = os.getcwd ()
    parser = argparse.ArgumentParser (description='Generates a tex file specifying pdf files to concatentate together')
    parser.add_argument ('files', nargs='+', help='List of files to convert. Specify file name only')
    parser.add_argument ('--working-directory', dest='working_dir', action='store', help='Root directory of this python script')
    parser.add_argument ('--pdf-directory', dest='pdf_dir', action='store', help='Directory containing the PDFs')
    parser.add_argument ('--use-json-spec', dest='use_json_spec', action='store_true', help='Use a json specification to creat the latex template')
    parser.add_argument ('-b', '--beamer', dest='is_beamer', action='store_true', help='Use landscape (beamer) mode')

    args = parser.parse_args ()
    root_dir = os.path.abspath (args.working_dir)
    main(root_dir, args.pdf_dir, args.files, args.is_beamer)