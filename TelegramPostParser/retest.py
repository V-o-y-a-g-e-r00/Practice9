import re
import copy

Str='12.345, 67.890'
Str1=re.findall('\d+.\d+', Str)
print(Str1)