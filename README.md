# docx2pdf tool with concatenation
Use this tool to convert docx files to pdf and concatenate them into a single pdf

## Rationale
I've had to work with docx files (ugh) and I got sick of having to use the GUI to export to PDF.
I also don't want to pay Adobe for the concatenation operation; something I think should really be included for free in Acrobat Reader.

## Dependencies
- [pywin32](https://pypi.org/project/pywin32/)
- [pdflatex](https://miktex.org/) with pdfpages library (search MikTex)
- [cmake](https://cmake.org/)

## Usage
The program can either convert all files located in the `input` folder, or convert a subset of these files specified in the `./input/file_list.txt` file.
To convert all files located in `./input/` simply execute
```
make.bat
```
from the root directory i.e. the one where the top level `CMakeLists.txt` file is located.

To convert a subset of files, take the following steps in order:
1. Run the make file to create a file named `file_list.txt` in the `input` directory, or create the file manually.
2. Place file names with extensions (note *just* the filename, not the absolute path) line by line into the newly created `file_list.txt` file.
3. Put each corresponding `docx` file into the `input` directory. *Make sure the filenames match whats in the `file_list.txt` file*.
4. Execute:
```
make.bat [-f|--use-file-list]
```
to convert all the files specified in the file list
