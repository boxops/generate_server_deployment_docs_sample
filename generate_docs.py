import yaml
from jinja2 import Template

with open("service_info.yaml", "r") as y:
    data = yaml.safe_load(y)

with open("template.j2", "r") as j:
    template = j.read()

md_template = Template(template)
documentation = md_template.render(data)
with open("README.md", "w") as file:
    file.write(documentation)

print("Documentation generated successfully!")
