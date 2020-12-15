'''
Sphinx extension for adding commit information on footer page.
'''
import os
import re
import shlex
import shutil
import subprocess
import urllib

__author__ = 'Kevin Migrino <kevin.migrino@nokia.com>'
'''
Based on a script made by
  Szymon Polinkiewicz <szymon.polinkiewicz@nokia.com>
'''

from sphinx.application import Sphinx

INDEX_SHA = 0
INDEX_AUTHOR = 1
INDEX_DATE = 2
INDEX_COMMENT = 3

INDEX_REF = 0
INDEX_DESC = 1
INDEX_REVREF = 2
INDEX_REVIEW = 3

INFO_COUNT = 3

def get_git_log_info_pretty(path, filename):
    cmd = 'git -C ' + path + ' log --follow --pretty=format:"%h|%an|%ad|%s" -- ' + filename
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()

    if process.returncode == 0:
        return re.findall(r'([a-fA-F0-9]+)\|([\w\s]+)\|([\w\s\:\+]+)\|([^\n]+)', out.decode('utf-8'))

def get_git_repo(path):
    cmd = 'git -C %s config --get remote.origin.url' % path
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    if process.returncode == 0:
        return out.decode('utf-8').strip()

def get_git_branch(path):
    cmd = 'git -C %s rev-parse --abbrev-ref HEAD' % path
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    if process.returncode == 0:
        return out.decode('utf-8').strip()

def get_logs_link(repo, branch):
    if 'gitlab' in repo:
        return repo.replace('.git', '/commits/%s' % branch)
    elif 'gerrit' in repo:
        proj = re.findall(r'\.com(\:443)?\/(gerrit\/)?(\S+$)', repo)
        if proj:
            proj = proj[-1][-1]
            return repo.replace(proj, '/gitweb?p=') + proj + '.git;a=shortlog;h=' + branch
        else:
            print 'WRN: No known repository found for %s, branch %s' % (repo, branch)


def add_commit_info(app, pagename, templatename, context, doctree):
    file_path = os.path.join(app.srcdir)

    file_new_path = doctree.attributes['source'] if doctree else os.path.join(file_path, pagename)
    context['current_file_path'] = file_new_path

    file_info = get_git_log_info_pretty(os.path.dirname(file_new_path), os.path.basename(file_new_path))
    file_repo = get_git_repo(os.path.dirname(file_new_path))
    branch = get_git_branch(os.path.dirname(file_new_path))

    if file_repo and file_info:
        context['repo_path'] = file_repo

        for i in range(INFO_COUNT):
            try:
                context['last_commit_revision_%s' % i] = file_info[i][INDEX_SHA]
                context['last_commit_author_%s' % i] = file_info[i][INDEX_AUTHOR]
                context['last_commit_date_%s' % i] = file_info[i][INDEX_DATE]

                match_desc_format1 = re.findall(r'\[DESCRIPTION\]\s*\:?\s*([^\[]+)\s+', file_info[i][INDEX_COMMENT])
                match_rev_format1 = re.findall(r'\[REVIEWER[S]?\]\s*\:?\s*([^\[]+)\s+', file_info[i][INDEX_COMMENT])
                matches = re.findall(r'REFERENCE:\s+(.+)DESCRIPTION:\s+(.+)REVIEW REF:\s+(.+)REVIEWER:\s+(.+$)', file_info[i][INDEX_COMMENT])

                context['last_commit_ref_%s' % i] = matches[0][INDEX_REF] if matches else ''
                context['last_commit_reviewer_%s' % i] = match_rev_format1[0] if match_rev_format1 else matches[0][INDEX_REVIEW] if matches else ''
                context['last_commit_revref_%s' % i] = matches[0][INDEX_REVREF] if matches else ''
                context['last_commit_comment_%s' % i] = match_desc_format1[0] if match_desc_format1 else matches[0][1] if matches else file_info[i][INDEX_COMMENT]

            except:
                pass

        context['log_hyperlink'] = get_logs_link(file_repo, branch)


def setup(app):
    '''
    Sphinx extension setup function

    :param app: Sphinx app instance
    '''

    app.connect('html-page-context', add_commit_info)
    return {'version': '1.0'}

