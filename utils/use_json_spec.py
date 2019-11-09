##
## Creates a tex file for input to pdflatex.
##

import os
import argparse
import csv
import json

## Simply writes the tex file, replacing the template for the files passed to the program
def main (root_dir, spec_dir):
    ## We need to read in the csv file and then create a json specification from it
    page_spec = {}
    items = []
    with open (os.path.join (root_dir, os.path.join (spec_dir, 'page_spec.csv'))) as csvfile:
        csv_data = csv.reader (csvfile, delimiter=',')
        for row in csv_data:
            concat_item = {}
            concat_item ['filename'] = row [0]
            concat_item ['start_page'] = row [1]
            concat_item ['end_page'] = row [2]
            items.append (concat_item)

    page_spec ['items'] = items
    with open (os.path.join (root_dir, os.path.join (spec_dir, 'page_spec.json')), 'w') as jsonfile:
        json.dump (page_spec, jsonfile, indent='\t')

if __name__ == '__main__':
    root_dir = os.getcwd ()
    parser = argparse.ArgumentParser (description='Generates a json file specifying files with corresponding pages to concatenate in the tex output')
    parser.add_argument ('--working-directory', dest='working_dir', action='store', help='Root directory of this python script')
    parser.add_argument ('--spec-directory', dest='spec_dir', action='store', help='Directory containing the csv spec')

    args = parser.parse_args ()
    root_dir = os.path.abspath (args.working_dir)
    main(root_dir, args.spec_dir)