# Funcs.py
# Функции для парсеров
# Разбивает строку сообщения из поста на список, пригодный к использованию в базе данных
def SplitStr(Str):
	import re
	import copy

	List=[]
	Result=[0, []]
	
	#Проверям, что в сообщении не менее 2 строк
	if not isinstance(Str, str): #Бывает, что попадает нестрока, как ни странно.
		Result[0]=-1		
		return Result
	if len(re.split('\n\n', str(Str)))<2:
		Result[0]=-1		
		return Result
	#Название и тэг
	Str1=re.split('\n\n', Str)[0]	
	if len(re.split('\W*#', Str1))<2: #Игнорируем рекламу.	
		Result[0]=-1		
		return Result
	else:
		#Название
		List.append(re.split('\W*#', Str1)[0])
		#Тег		
		List.append(re.split('\W*#', Str1)[1])

	#Описание. Его пока нет, поэтому будет пустая строка
	List.append('')
	
	#Координаты	
	Str2=re.split('\n\n', Str)[1] 
	if len(re.findall('\d+.\d+', Str))<2: #Если с координатами что-то не так
		Result[0]=-1		
		return Result
	List.append(re.findall('\d+.\d+', Str)[0]) #Список из элементов: точка, окруженная цифрами
	List.append(re.findall('\d+.\d+', Str)[1])

#	print(List)
	Result[1]=copy.copy(List)
	return Result

# Помещает данные из списка в базу данных. Если базы данных не существует, то создает её.
def PutInmySQL(List):
	from getpass import getpass
	from mysql.connector import connect, Error

	import re #Для работы со строками

	DBNAME="TouristPlaces1"
	try: #Все соединения с базой данных оборачивайте в блоки try ... except  .Так будет проще перехватить и изучить любые исключения.
		fin= open('IdmySQL.txt', 'r')
		user=fin.readline().splitlines()[0]
		password=fin.readline().splitlines()[0]
		fin.close()
		with connect( #Исключения на питоне. выполняется выражение connenct(...), которое возвращает объект. Затем у объекта вызывается метод __enter__(self) его результат присваивается connection. Далее идет попытка print(connection) если возникают иключения, они обрадатываются методом объекта __exit__. Если нет, то этот метод все равно вызывается. Сверху это все дополнительно помещено в блок try exept 
				host="localhost", #Не забывайте закрывать соединение после завершения доступа к базе данных. Неиспользуемые открытые соединения приводят к неожиданным ошибкам и проблемам с производительностью. В коде для этого используется диспетчер контекста (with ... as ...).
				#user=input("Имя пользователя: "), #root
				#password=getpass("Пароль: "),
				user=user,
				password=password,
				#database="online_movie_rating",
		) as connection:
				print(connection)
			
				#Пошла работа с базами данных
				#Проверяем, что таблица существует
				print("Checking existence of", DBNAME, "db...")
				IsTableExist=0
				show_db_query = "SHOW DATABASES"
				with connection.cursor() as cursor:
					cursor.execute(show_db_query)
					for db in cursor:
						temp=re.split('\'', str(db))[1]
						if temp==DBNAME:
							IsTableExist=1
						#print(db)
				#print('IsTableExist=', IsTableExist)

				#Если базы данных нет, то создаем её и создаем в ней таблицу.
				if IsTableExist==0:				
					print(DBNAME, "db does not exist. Creating", DBNAME, " db...")
					create_db_query = "CREATE DATABASE IF NOT EXISTS " + DBNAME 
					with connection.cursor() as cursor:
						cursor.execute(create_db_query)

					use_db_query = "USE "+DBNAME
					with connection.cursor() as cursor:
						cursor.execute(use_db_query)

					create_Places_table_query = """
					CREATE TABLE Places(
						id INT AUTO_INCREMENT PRIMARY KEY,
						name VARCHAR(2047),
						tag VARCHAR(2047),
						description text(10239),
						latitude DECIMAL(11,8),
						longitude DECIMAL(11,8),
						grouped_id VARCHAR(2047)
					)
					"""
					with connection.cursor() as cursor:
						cursor.execute(create_Places_table_query)
						connection.commit()
						print(DBNAME, "db has been created")
				else:
					print(DBNAME, "db exists.")
					use_db_query = "USE "+DBNAME
					with connection.cursor() as cursor:
						cursor.execute(use_db_query)
				
				#Добавляем запись в базу данных
				print("Inserting a new entry...: ", List)
				insert_place_query = """
				INSERT INTO Places (name, tag, description, latitude, longitude, grouped_id)
				VALUES
					(%s, %s, %s, %s, %s, %s)
				"""
				with connection.cursor() as cursor:
					for result in cursor.execute(insert_place_query, List, multi=True):
						if result.with_rows:
							print(result.fetchall())
					connection.commit()
				print("Entry has been inserted") #Выводим все кроме фото

	#ловим необработанные исключения при работе с соединением
	except Error as e:
		print(e)

# Принимает сообщение и посылает его в базу, используя PutInmySQL(List)
def MessageToBase(message, fout):
	from telethon.sync import TelegramClient, events
	#Пишем сообщения для возможности отладки
	with open(fout, 'ab') as f:
		f.write(str(message).encode('utf-8'))
		f.write('\n'.encode('utf-8'))
	print("New post has been appeared. The message is:\n-----------------\n", message.message, "\n-----------------", sep='')
	if SplitStr(message.message)[0]!=-1: #Проверяем, имеет ли сообщение тот текст, который нам необходим.
		print('The message matches the info message criteria')
		List=SplitStr(message.message)[1] #Разбиваем сообщение на список
		if str(message.grouped_id) != 'None': #Если картинка всего одна, то значение None. нужно как-то подругому идентифицировать картинки к постам.
			List.append(message.grouped_id) #Пост по факту разбит на несколько, в одном - текст, в остальных - картинки. Поэтому для того, чтобы понять, какие картинки с ним связаны, нам нужно это свойство.
		else:
			if str(message).find('media=MessageMediaPhoto')!=-1:
				List.append(message.media.photo.id)
			else:
				List.append('NoPhoto') #У поста нет медиаконтента
		#photo_1 = Image.open(event.message.photo)
		#image_buf = BytesIO()
		#photo_1.save(image_buf, format="JPEG")
		#image = image_buf.getvalue()
		
		print("Sending text data to db...")
		PutInmySQL(List) #Передаем функции, отвечающей за добавление в базу данных список, полученный из строки сообщения.
		print("Text data has been sent")
		return "Photos/"+str(List[5])+"/"	
	else: #Сюда входят случаи, когда сообщение рекламное либо когда оно состоит из прикрепленного изображения.
		print('The message does not match the info message criteria')
		
		PathStr='NoPath'
		if str(message.grouped_id) != 'None': #Если картинка всего одна, то значение None. нужно как-то подругому идентифицировать картинки к постам.
			PathStr=str(message.grouped_id)
		else:
			if str(message).find('media=MessageMediaPhoto')!=-1:
				PathStr=str(message.media.photo.id)		
		return "Photos/"+PathStr+"/"




	
	















