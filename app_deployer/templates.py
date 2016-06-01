# Import built-in packages
import os
import re
import logging

# Import third-party packages
import jinja2


def render_templates(in_dir, out_dir, templ_vars):
    # Create out dir
    os.makedirs(out_dir, exist_ok=True)
    # Walk template directory
    for dirpath, dirs, files in os.walk(in_dir):
        for filename in files:
            # Set in and out file names
            in_file = os.path.join(dirpath, filename)
            in_file = re.sub(r'^{}/'.format(in_dir), '', in_file)
            out_file = '{}/{}'.format(out_dir, in_file)
            # Create out_file path
            os.makedirs(os.path.dirname(out_file), exist_ok=True)
            # continue
            # Render template
            loader = jinja2.FileSystemLoader(in_dir)
            env = jinja2.Environment(loader=loader)
            template = env.get_template(in_file)
            with open(out_file, 'w') as f:
                f.write(template.render(templ_vars))
