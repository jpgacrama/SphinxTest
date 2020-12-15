import os
import re
import subprocess

ROOT_KEYWORD = '$rootdir$'
SOURCE_DIR = '/root/sphinx/source'

def replace_root(app, docname, source):
    if ROOT_KEYWORD not in source[0]:
        return

    doc_path = os.path.join(SOURCE_DIR, docname)
    git_rel_path = '.'
    git_root_cmd = 'git -C %s rev-parse --show-toplevel' % os.path.dirname(doc_path)
    git_root_path = subprocess.check_output(git_root_cmd, stderr=subprocess.STDOUT, shell=True).rstrip()

    if SOURCE_DIR in git_root_path:
        git_rel_path = os.path.join(git_rel_path, os.path.relpath(git_root_path, os.path.dirname(doc_path)))
    else:
        print 'WRN: file "%s" is not tracked in any git repo' % docname

    new_source = source[0].replace(ROOT_KEYWORD, git_rel_path)
    source[0] = new_source

def setup(app):
    app.connect('source-read', replace_root)

