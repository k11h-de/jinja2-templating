#!/usr/bin/python3 

# run.py example/vars.yaml example/ssh_config.j2 [out.txt]

from jinja2 import Template
import yaml, sys
# load yaml vars file
yaml = yaml.safe_load(open(str(sys.argv[1]), 'r'))
# load jinja2 template file
template = Template(open(str(sys.argv[2])).read())
# if no out file was provided
if len(sys.argv) == 3:
    # print to stdout
    print(template.render(yaml))
# if outfile was provided
elif len(sys.argv) == 4:
    # write result to output file
    with open(str(sys.argv[3]), 'w') as f:
        print(template.render(yaml), file=f)