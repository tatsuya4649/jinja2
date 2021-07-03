from jinja2 import Template

tmps = 'Hello {{str}}'
template = Template(tmps)
rens = template.render(str="World")
print(rens)
