#!/usr/bin/python3

import os
from subprocess import run, PIPE


HTML_TEMPLATE_FILE = 'dashboard-template.html'
PROBES_DIR = 'probes'

li_class = {
    0: 'ok',
    1: 'error',
    2: 'warning',
    3: 'info',
}

li_template = '''\
<li class="{cls}">
    <strong>{title}</strong>
    <div>{stdout}</div>
    <div class="stderr">{stderr}</div>
</li>'''

def list_executable_files(directory):
    for filename in os.listdir(directory):
        fullpath = os.path.join(directory, filename)
        if os.path.isfile(fullpath) and os.access(fullpath, os.X_OK):
            yield fullpath

def generate_li(script_path):
    proc = run([script_path], stdout=PIPE, stderr=PIPE, encoding='utf-8')

    basename = os.path.basename(script_path)
    err_class = li_class.get(proc.returncode, 'error')
    li = li_template.format(cls=err_class,
                            title=basename,
                            stdout=proc.stdout,
                            stderr=proc.stderr)
    return li


def main():
    with open(HTML_TEMPLATE_FILE, 'r') as fd:
        html_template = fd.read()

    lis = ''
    for script in list_executable_files(PROBES_DIR):
        lis += generate_li(script)

    print(html_template.replace('CONTENT_PLACEHOLDER', lis))

if __name__ == '__main__':
    main()
