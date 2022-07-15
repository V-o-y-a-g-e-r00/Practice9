def SplitStr(Str):
	import re
	List=[]
	
	#Название и тэг
	Str1=re.split('\n\n', Str)[0]	
	#Название
	List.append(re.split(', ', Str1)[0])
	#Тэг
	if re.split(', ', Str1)[1][0]!='#': #Чтобы игнорировать рекламные посты.
		return -1
	List.append(re.split(', ', Str1)[1][1:])

	#Координаты	
	Str2=re.split('\n\n', Str)[1]
	List.append(re.split(', ', Str2)[0])
	List.append(re.split(', ', Str2)[1])

#	print(List)	
	return List

def SplitStr2(Str):
	import re
	import copy

	List=[]
	Result=[0, []]

	#Удаляем пустые строки
	ListLines=[]
	ListLines=re.split('\n', Str)
	i=0	
	while i<len(ListLines):
		if ListLines[i]=='':
			del ListLines[i]
		else:
			i+=1 
	print(ListLines)
	
	#Делим первую непустую строку на название и теги
	index=ListLines[0].find('#')
	name=ListLines[0][:index]

	i=len(name) -1
	while i>=0:
		print(re.match('\w', name))

	print(re.split('\W+', name))
	
	print(name)

Str='Горы Отважная и Шишка, #Самарскаяобласть\n\n53.422337, 49.448636\n\nФото airforce_ru\n\nКрасивые места России в мобильном приложении👇\nСкачать'
SplitStr2(Str)

import re
xx = "guru99,education is fun"
r1 = re.findall(r"$",xx)
print(r1)