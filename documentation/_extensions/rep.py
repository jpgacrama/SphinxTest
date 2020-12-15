import os
import re
import sys

PAGE_PATH = 'URL to Sphinx server'
SRC_PATH = '/root/sphinx/source'
MOD_FILE_LIST = [os.path.join('_templates','breadcrumbs.html'),
                 os.path.join('_extensions','uml_linker','__init__.py'),
                 os.path.join('_extensions','root_dir','__init__.py')]

NEW_SRC_PATH = sys.argv[1]
NEW_DST_PATH = os.path.join(sys.argv[2], 'html\\\\')


if NEW_SRC_PATH and NEW_DST_PATH:
    for item in MOD_FILE_LIST:
        item_path = os.path.join(NEW_SRC_PATH, item)
        with open(item_path, 'r') as infile:
            contents = infile.read()
            if PAGE_PATH in contents or SRC_PATH in contents:
                print 'Found...', item_path
                contents = contents.replace(PAGE_PATH, NEW_DST_PATH)
                contents = contents.replace(SRC_PATH, NEW_DST_PATH)
                with open(item_path, 'w') as outfile:
                    print 'Write to...', item_path
                    outfile.write(contents)

else:
    print 'INF: No changes in extensions'
