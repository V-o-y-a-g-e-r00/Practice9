def PutInmySQL(List):
	from getpass import getpass
	from mysql.connector import connect, Error

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
				database="online_movie_rating",
		) as connection:
				print(connection)
			
				#Пошла работа с базами данных
				create_db_query = "CREATE DATABASE online_movie_rating"
				#with connection.cur>sor() as cursor:
				#	cursor.execute(create_db_query)

				show_db_query = "SHOW DATABASES"
				with connection.cursor() as cursor:
					cursor.execute(show_db_query)
					for db in cursor:
						print(db)

	#ловим необработанные исключения при работе с соединением
	except Error as e:
		print(e)

List=[]
PutInmySQL(List)