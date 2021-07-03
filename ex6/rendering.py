from jinja2 import Template,Environment,FileSystemLoader
import json

env = Environment(loader=FileSystemLoader('./',encoding='utf8'))
tmp = env.get_template('child.html')

with open('parameter.json') as f:
	params = json.load(f)

render = tmp.render(params)
print(render)
