# ��������� ������ ��������� �� ����� �� ������, ��������� � ������������� � ���� ������
def SplitStr(Str):
	import re
	import copy

	List=[]
	Result=[0, []]
	#�������� � ���
	Str1=re.split('\n\n', Str)[0]	
	#��������
	List.append(re.split(', ', Str1)[0])
	#���
	if len(re.split(', ', Str1))>=2: #����� �������� ������������.	
		if re.split(', ', Str1)[1][0]!='#': #����� ������������ ��������� �����.
			Result[0]=-1		
			return Result
		List.append(re.split(', ', Str1)[1][1:])
	else:
		Result[0]=-1		
		return Result

	#��������. ��� ���� ���, ������� ����� ������ ������
	List.append('')
	
	#����������	
	Str2=re.split('\n\n', Str)[1]
	List.append(re.split(', ', Str2)[0])
	List.append(re.split(', ', Str2)[1])

#	print(List)
	Result[1]=copy.copy(List)
	return Result
