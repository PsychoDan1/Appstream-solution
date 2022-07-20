#!/usr/bin/python3

import yaml

with open('manifest.yml', 'rb') as f:
        config = yaml.safe_load(f)

core_config = config['environment']
subnet_config = core_config['streamView']
print(subnet_config)



