import yaml
import os

def init_config(app):
    with app.open_instance_resource('xohrook.yaml') as f:
        buf = yaml.load(f)
    env = os.environ.get('FLASK_ENV', 'DEVELOPMENT')
    for name in (env, env.capitalize(), env.lower()):
        try:
            buf = buf[name]
            break
        except:
            pass

    for key in buf.iterkeys():
        if key.isupper():
            app.config[key] = buf[key]