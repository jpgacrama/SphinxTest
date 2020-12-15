import os
from sphinxcontrib.plantuml import plantuml
import re

sphinx_resolved_labels = None
sphinx_resolved_objects = None

BASE_URL = 'URL to Sphinx Server'

def link_uml_references(app, doctree, docname):
    global sphinx_resolved_labels, sphinx_resolved_objects
    if not sphinx_resolved_labels:
        sphinx_resolved_labels = app.env.domaindata['std']['labels']
        sphinx_resolved_objects = app.env.domaindata['std']['objects']
        if not sphinx_resolved_objects:
            print 'WRN: No Domain Objects (Glossary) found! Glossary terms may not resolve.'

    for node in doctree.traverse(plantuml):
        '''
        match[0]: whole match, e.g. (1) ":ref:`display<reflink>`" or  (2) ":ref:`reflink`"
        match[1]: role, e.g. "ref"
        match[2]: display text, e.g. "display" for case (1) or
                  reference link, e.g. "reflink" for case (2)
        match[3]: reference link, e.g. "reflink" for case (1)
        '''
        for match in re.findall(r"(:(\S+):[\s]*`([^`<]+)[<]?([^>`]*)[>]?`)", node['uml']):
            role = match[1]
            if 'ref' == role:
                reflink_in_match = unicode((match[3] if match[3] != '' else match[2]).lower())
                if reflink_in_match in sphinx_resolved_labels:
                    display_text = match[2] if match[3] != '' else sphinx_resolved_labels[reflink_in_match][2]
                    plantuml_hyperlink = "[[{0} {1}]]".format(os.path.join(BASE_URL, sphinx_resolved_labels[reflink_in_match][0]+'.html'),
                                                              display_text)
                    node['uml'] = node['uml'].replace(match[0], plantuml_hyperlink)
                else:
                    print 'WRN: Could not resolve reflink "%s" found in UML diagram in file "%s"! '\
                    'Please double-check if file referenced by reflink exists.' % (reflink_in_match, docname)
            elif 'term' == role:
                matched_term = match[3] if match[3] != '' else match[2]
                reflink_in_match = (role, unicode(matched_term.lower()))
                if reflink_in_match in sphinx_resolved_objects:
                    plantuml_hyperlink = "[[{0} {1}]]".format(os.path.join(BASE_URL,
                                                                           sphinx_resolved_objects[reflink_in_match][0]+'.html#'+\
                                                                           sphinx_resolved_objects[reflink_in_match][1]),
                                                              match[2])
                    node['uml'] = node['uml'].replace(match[0], plantuml_hyperlink)
                else:
                    print 'WRN: Could not resolve glossary term "%s" found in UML diagram in file "%s"! '\
                    'Please double-check if term is defined in the glossary.' % (matched_term, docname)


def setup(app):
    app.connect('doctree-resolved', link_uml_references)
