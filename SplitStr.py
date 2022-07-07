# Разбивает строку сообщения из поста на список, пригодный к использованию в базе данных
def SplitStr(Str):
	import re
	import copy

	List=[]
	Result=[0, []]
	#Название и тэг
	Str1=re.split('\n\n', Str)[0]	
	#Название
	List.append(re.split(', ', Str1)[0])
	#Тэг
	if len(re.split(', ', Str1))>=2: #Чтобы избежать переполнения.	
		if re.split(', ', Str1)[1][0]!='#': #Чтобы игнорировать рекламные посты.
			Result[0]=-1		
			return Result
		List.append(re.split(', ', Str1)[1][1:])
	else:
		Result[0]=-1		
		return Result

	#Описание. Его пока нет, поэтому будет пустая строка
	List.append('')
	
	#Координаты	
	Str2=re.split('\n\n', Str)[1]
	List.append(re.split(', ', Str2)[0])
	List.append(re.split(', ', Str2)[1])

#	print(List)
	Result[1]=copy.copy(List)
	return Result
