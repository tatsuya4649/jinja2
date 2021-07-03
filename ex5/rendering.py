from jinja2 import Template,Environment,FileSystemLoader
import json

env = Environment(loader=FileSystemLoader('./',encoding='utf8'))
tmp = env.get_template('template.html')

with open('parameter.json') as f:
	param = json.load(f)

render = tmp.render(param)
print(render)
