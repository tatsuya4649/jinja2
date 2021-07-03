from jinja2 import Template,Environment,FileSystemLoader
import json

# loading Tempalte
env = Environment(loader=FileSystemLoader('./',encoding='utf8'))
tmpl = env.get_template('template.html')

# loading Parameter
with open('parameter.json') as f:
	params = json.load(f)

# output
rendered = tmpl.render(params)
print(rendered)
