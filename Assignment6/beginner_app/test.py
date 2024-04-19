import re

string = 'weett====grwd'
result = re.sub('.=', '', string)
# result = re.sub('=', '', string)
print(result)
