

def PutInmySQL(List):
	from getpass import getpass
	from mysql.connector import connect, Error

	import re #Для работы со строками

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
				print("Checking existence of TouristPlaces db...")
				IsTableExist=0
				show_db_query = "SHOW DATABASES"
				with connection.cursor() as cursor:
					cursor.execute(show_db_query)
					for db in cursor:
						temp=re.split('\'', str(db))[1]
						if temp=='TouristPlaces':
							IsTableExist=1
						#print(db)
				#print('IsTableExist=', IsTableExist)

				#Если базы данных нет, то создаем её и создаем в ней таблицу.
				if IsTableExist==0:				
					print("TouristPlaces db does not exist. Creating TouristPlaces db...")
					create_db_query = "CREATE DATABASE IF NOT EXISTS TouristPlaces" 
					with connection.cursor() as cursor:
						cursor.execute(create_db_query)

					use_db_query = "USE TouristPlaces"
					with connection.cursor() as cursor:
						cursor.execute(use_db_query)





					create_Places_table_query = """
					CREATE TABLE Places(
						id INT AUTO_INCREMENT PRIMARY KEY,
						name VARCHAR(2047),
						tag VARCHAR(2047),
						description VARCHAR(10239),
						latitude DECIMAL(9,6),
						longitude DECIMAL(9,6)
					)
					"""
					with connection.cursor() as cursor:
						cursor.execute(create_Places_table_query)
						connection.commit()
						print("TouristPlaces db has been created")
				else:
					print("TouristPlaces db exists.")


	#ловим необработанные исключения при работе с соединением
	except Error as e:
		print(e)

List=[]

PutInmySQL(List)




