from jinja2 import Template,Environment,FileSystemLoader
import json

# reading Template
env = Environment(loader=FileSystemLoader('./',encoding='utf8'))
tmpl = env.get_template('template.j2')

# reading Configure file
with open('parameter.json') as f:
	params = json.load(f)
print(params)

# rendering
rendered_s = tmpl.render(params)
print(rendered_s)
