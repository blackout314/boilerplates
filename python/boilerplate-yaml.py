### credential.yml ###
#
#qa:
# user:
#   - user
# pass:
#   - password
#
### eof ##

import yaml

config = yaml.safe_load(open("credential.yml"))

print (config[env]['user'][0])
