#!/bin/env python3

import yaml
from jinja2 import Template,Environment,FileSystemLoader

env = Environment(loader=FileSystemLoader('./conf/conf.d'))
template = env.get_template('app')

with open('ip.yaml') as f:
	obj = yaml.safe_load(f)
print(obj)

render = template.render(obj)
print(render)

