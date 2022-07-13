# It's a Python script that searches for Font Awesome icons in the templates.
import os
import re
import argparse

parser = argparse.ArgumentParser(description='Find Font Awesome icons in the templates.')
parser.add_argument('-d', '--directory', help='The directory to search for Font Awesome icons.', required=False,  default='.')

args = parser.parse_args()
searchPath = args.directory

for root, dirs, files in os.walk(searchPath):
    for file in files:
        if file.endswith('.tpl'):
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
                faSearch = re.search(r'<i class(Name)?="[^"]* (fa-.[^"]*?)( |")>', content)
                if faSearch != None:
                    print("%s: %s" % (os.path.join(root, file), faSearch.group(2)))

print('\n')
