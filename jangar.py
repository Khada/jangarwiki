#!usr/bin/env python
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

'''
TODO:

* create index.html for each directory,
  especially for root, used for general browsing
* add interwiki link parser

'''

if __name__ == '__main__':

    try:
        markdown_version = subprocess.check_output(['markdown', '--shortversion'])
    except OSError:
        exit('Aldaa: Markdown suusan baikh yostoi.')
    print 'Markdown {} ashiglaj baina.'.format(markdown_version)
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

        # create sub dirs
        try:
            os.mkdir('./{}/{}'.format(output_dir, dirname))
        except OSError:
            pass
        
        # TODO: create index.html for each directory
        # esp. for root directory general index is needed

        # go on
        for filename in filenames:
            fpath = os.path.join(dirname, filename)
             
            # only convert if the file is wikiformatted
            if filename.split('.')[-1] in wikiformats:
                fpath = fpath[2:]  # remove annoying ./
                pagename = fpath[:-3]  # remove file extension
                outfilename = os.path.join(output_dir, '{}.html'.format(pagename))
                print outfilename
                out_body = subprocess.check_output(['markdown', fpath])
                out_html = template.substitute(content=out_body)
                with open(outfilename, 'w') as outfile:
                    outfile.write(out_html)
        
    print 'Duuslaa.'
