import re
import copy
from Funcs import *

#Str='12.345, 67.890'
Str='Аракульский Шихан, Озеро Аракуль, #Челябинскаяобласть\n\n55.988143, 60.490475\n\nФото: korolyuk___\n\nКрасивые места России в мобильном приложении👇\nСкачать'

#Str1=re.findall('\d+.\d+', Str)
print(SplitStr(Str))