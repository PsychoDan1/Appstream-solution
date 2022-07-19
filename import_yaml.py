#!/usr/bin/python3

import yaml

with open('manifest.yml', 'rb') as f:
        config = yaml.safe_load(f)

core_config = config['spec']
env = core_config['environments']
env_name = env['name']
#print(core_config)
print(env_name)

