import sqlite3

class SQLighter:





	def __init__(self, database):
		"""Подключаемся к БД и сохраняем курсор соединения"""
		self.connection = sqlite3.connect(database)

		self.cursor = self.connection.cursor()

	def get_subscriptions(self, status = True):
		"""Получаем всех активных подписчиков бота"""
		with self.connection:
			return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

	def subscriber_exists(self, user_id):
		"""Проверяем, есть ли уже юзер в базе"""
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `subscriptions` WHERE `user_id` = ?', (user_id,)).fetchall()
			return bool(len(result))

	def add_subscriber(self, user_id, status = True):
		"""Добавляем нового подписчика"""
		with self.connection:
			return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES(?,?)", (user_id,status))

	def update_subscription(self, user_id, status):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

	def update_subscription_off(self, user_id, status = False):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))


	def update_status_car_on(self, user_id, status_car = True):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `status_car` = ? WHERE `user_id` = ?", (status_car, user_id))

	def update_status_car_off(self, user_id, status_car = False):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `status_car` = ? WHERE `user_id` = ?", (status_car, user_id))

	def close(self):
		"""Закрываем соединение с БД"""
		self.connection.close()
	

	def update_SCORE(self, nomber, user_id, ):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET nomber= ? WHERE `user_id` = ?", (nomber,user_id, ))

	def update_nomber_start(self, user_id, nomber ):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET nomber= ? WHERE `user_id` = ?", (nomber, user_id))



	def add_message(self, nomber: int, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `nomber` = ? WHERE  `user_id` = ? ", (nomber,user_id))


	def get_nomber(self, user_id):
		return self.cursor.execute("SELECT `nomber` FROM `subscriptions` WHERE  `user_id` = ? ", (user_id, )).fetchall()

		row = cursor.fetchone()

	def get_ID(self, user_id):
		return self.cursor.execute("SELECT `id` FROM `subscriptions` WHERE  `user_id` = ? ", (user_id, )).fetchall()

		row = cursor.fetchone()




	def get_nomber_min(self, status = True):
		return self.cursor.execute("SELECT `nomber` FROM `subscriptions` WHERE  `status` = ? ", (status, )).fetchall()



		results = self.cursor.fetchall()

	def get_allV2(self, status = True, status_car = False):
		"""Получаем всех активных подписчиков бота"""
		with self.connection:
			return self.cursor.execute("SELECT nomber FROM `subscriptions` WHERE `status` = ? AND status_car = ?", (status,status_car )).fetchall()

	def get_all(self, status = True):
		"""Получаем всех активных подписчиков бота"""
		with self.connection:
			return self.cursor.execute("SELECT nomber FROM `subscriptions` WHERE `status` = ?", (status, )).fetchall()

	def get_people(self, nomber: int):

		with self.connection:
		   return self.cursor.execute("SELECT id FROM `subscriptions` WHERE `nomber` = ?",(nomber, ) ).fetchall()


	def get_name_people(self, id: int):

		with self.connection:
		   return self.cursor.execute("SELECT text FROM `subscriptions` WHERE `id` = ?",(id, ) ).fetchall()



	def shange_time(self, time: int, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `time` = ? WHERE  `user_id` = ? ", (time,user_id))
	




	def get_all_time(self, status = True):

		with self.connection:
		   return self.cursor.execute("SELECT time FROM `subscriptions` WHERE status = ? ", (status, )).fetchall()


	def shange_nomber(self, nomber: int, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `nomber` = ? WHERE  `user_id` = ? ", (nomber,user_id))


	def get_all_car(self, time):

		with self.connection:
		   return self.cursor.execute("SELECT status FROM `subscriptions` WHERE time = ? ", (time, )).fetchall()

	def get_index_all_car(self, status = True):

		with self.connection:
		   return self.cursor.execute("SELECT text FROM `subscriptions` WHERE status = ? ", (status, )).fetchall()


	 # снизу всё про call #
	def shange_call(self, call: int, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `call` = ? WHERE  `user_id` = ? ", (call,user_id))
	
	def get_call(self, user_id):

		with self.connection:
		   return self.cursor.execute("SELECT call FROM `subscriptions` WHERE user_id = ? ", (user_id, )).fetchall()

	def get_call_with_min_nomber(self, nomber):

		with self.connection:
		   return self.cursor.execute("SELECT call FROM `subscriptions` WHERE nomber = ? ", (nomber, )).fetchall()


	def get_max_nomber_witch_all(self, call = 0, status = True):

		with self.connection:
		   return self.cursor.execute("SELECT nomber FROM `subscriptions` WHERE call = ? and status = ? ", (call,status )).fetchall()

	
	def shange_status(self, status = False):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? ", (status, ))

	def shange_status_car1(self, status_car = 0):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `status_car` = ? ", (status_car, ))

	def shange_calll(self, call = 0):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `call` = ? ", (call, ))

	def shange_wait(self, wait: int, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `wait` = ? WHERE  `user_id` = ? ", (wait,user_id))

	def shange_waits(self, wait: int, ):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `wait` = ? ", (wait, ))

	
	def get_all_time_(self, wait = True):

		with self.connection:
		   return self.cursor.execute("SELECT time FROM `subscriptions` WHERE wait = ? ", (wait, )).fetchall()

	def shange_nomber_of_time(self, nomber: int , time):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `nomber` = ? WHERE  `time` = ? ", (nomber,time))

	def update_statuss(self, time, status = True):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `time` = ?", (status, time))

	def get_time_minus(self, status = True, status_car = False):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("SELECT time_minus FROM `subscriptions` WHERE `status` = ? and status_car = ?", (status, status_car )).fetchall()
	

	def shange_time_minus(self, time_minus: int , user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `time_minus` = ? WHERE  `user_id` = ? ", (time_minus,user_id))

	def get_index_all_car_of_time_minus(self, time_minus, status = 1):

		with self.connection:
		   return self.cursor.execute("SELECT text FROM `subscriptions` WHERE time_minus = ? AND status = ?", (time_minus,status )).fetchall()

	def get_index_for_ifo_free(self, status = 1, status_car = 0):

		with self.connection:
		   return self.cursor.execute("SELECT text FROM `subscriptions` WHERE status = ? AND status_car = ?", (status,status_car )).fetchall()
	
	def get_index_for_ifo_pay(self, status = 1, status_car = 1):

		with self.connection:
		   return self.cursor.execute("SELECT text FROM `subscriptions` WHERE status = ? AND status_car = ?", (status,status_car )).fetchall()

	def get_nooomber(self, user_id):
		return self.cursor.execute("SELECT `nomber` FROM `subscriptions` WHERE  `user_id` = ? ", (user_id, )).fetchall()

	def get_time_minus__(self, status = True):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("SELECT time_minus FROM `subscriptions` WHERE `status` = ? ", (status, )).fetchall()


	def shange_night(self, night: int , user_id):
		with self.connection:
			return self.cursor.execute("UPDATE `subscriptions` SET `night` = ? WHERE  `user_id` = ? ", (night,user_id))


	def get_time_minus_for_me(self, user_id ):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("SELECT time_minus FROM `subscriptions` WHERE `user_id` = ? ", (user_id, )).fetchall()


	def get_time_minus_night_ON(self, status = True, night = True, status_car = False):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("SELECT time_minus FROM `subscriptions` WHERE `status` = ? AND night = ? AND status_car = ?", (status, night, status_car )).fetchall()
	def get_time_minus_night_OFF(self, status = True, night = False, status_car = False):
		"""Обновляем статус подписки пользователя"""
		with self.connection:
			return self.cursor.execute("SELECT time_minus FROM `subscriptions` WHERE `status` = ? AND night = ? AND status_car = ?", (status, night, status_car )).fetchall()




	

	



	


	
	


		
