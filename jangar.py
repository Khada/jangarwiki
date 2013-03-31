#!usr/bin/env python
import re
import os
import subprocess
from string import Template

output_dir='_html'
input_dir='.'
wikiformats = ['md']

template_string = '''
<!DOCTYPE html>
<html lang="mn">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>
    $content
    </body>
</html>
'''
template = Template(template_string)


def check_markdown():

    try:
        markdown_version = subprocess.check_output(['markdown', '--shortversion'])
    except OSError:
        exit('Aldaa: Markdown suusan baikh yostoi.')
    print 'Markdown {} ashiglaj baina.'.format(markdown_version)


def convert_wikilink(text):
    pattern = re.compile(r'(?P<wikilink>\[\[(?P<pagename>[\w ]+)\|?(?P<linktext>[\w ]+)?\]\])')
    for wikilink, pagename, linktext in pattern.findall(text):
        linktext = linktext or pagename
        text = text.replace(wikilink, '<a href="{}.html">{}</a>'.format(pagename, linktext))

    return text


def make_html():

    check_markdown()
    print 'HTML ruu khuvirgaj baina...'

    # create output dir
    try:
        os.mkdir('./{}'.format(output_dir))
    except OSError:
        pass

    for dirname, dirnames, filenames in os.walk('.'):
        # ignore .git 
        if '.git' in dirnames:
            dirnames.remove('.git')

        # don't walk into output_dir
        if output_dir in dirnames:
            dirnames.remove(output_dir)

        # NOTE:
        # not creating subdirs and
        # not putting pages in respective dirs
        # due to relative interwiki links
        # so, all pages are generated in root.
        # could be improved

        # go on
        for filename in filenames:
            fpath = os.path.join(dirname, filename)

            # only convert if the file is wikiformatted
            if filename.split('.')[-1] in wikiformats:
                fpath = fpath[2:]  # remove annoying ./
                pagename = filename[:-3]  # remove file extension
                outfilename = os.path.join(output_dir, '{}.html'.format(pagename))
                print outfilename
                out_body = subprocess.check_output(['markdown', fpath])
                out_body = convert_wikilink(out_body)
                out_html = template.substitute(content=out_body)
                with open(outfilename, 'w') as outfile:
                    outfile.write(out_html)

    print 'Duuslaa.'


if __name__ == '__main__':
    make_html()
