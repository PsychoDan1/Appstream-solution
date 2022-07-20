#!/usr/bin/python3

import yaml

with open('manifest.yml', 'rb') as f:
        config = yaml.safe_load(f)

core_config = config['environment']
fleet_name = core_config['maxCapacity']
print(fleet_name)



