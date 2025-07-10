import config
import telebot
import logging
import sqlite3
import datetime
import time


from telebot import types
from sqlate import SQLighter
from aiogram import Bot, Dispatcher, executor, types


bots = telebot.TeleBot(config.API_TOKEN )





X_TIME = (time.strftime(" %X ", time.localtime()))



time_all = X_TIME.replace(':','')









logging.basicConfig(level=logging.INFO)

bot = Bot(token = config.API_TOKEN)
dp = Dispatcher(bot)

db = SQLighter('db.db')




@dp.message_handler(commands=['Я'])
async def subscribe(message: types.Message):
	db.update_status_car_off(message.from_user.id)
	max_int = db.get_max_nomber_witch_all()
	print (max_int)
	print ("53 TRUE")
	max_int_str = str(max_int)

	




	if max_int_str == "[]":
		score2 = db.get_nomber_min()
		if score2 is None:
			print("Eror 58str")
		else:
			score2.sort()
			X__TIME = (time.strftime(" %X ", time.localtime()))



			time_alll = X__TIME.replace(':','')

			db.shange_time_minus(time_alll,message.from_user.id)

			print ("68STR",score2)
			str11 = str(score2)
			if str11 == "[]":
				print ("error 64str")
			else:
							score3 = int(score2[0][0])

							db.get_max_nomber_witch_all()

							score1 = int(score3 - 1)
							print (score1)
							db.shange_nomber(score1, message.from_user.id)
	else:
		maxx = max(max_int)
		print (maxx)
		maxxx = str(maxx[0]) # Максимальное число с call=0 and status = 1
		max_maxx = int(maxxx) + 1
		db.shange_nomber(max_maxx, message.from_user.id)






	if(not db.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
		db.add_subscriber(message.from_user.id)
	else:

		db.update_subscription(message.from_user.id, True)

	await message.answer(
		"Вы приехали и встали в очередь")

	index_all2 = db.get_index_all_car() # текст всех мащин кто рабоатет
	index_all3 = (len(index_all2)) # количесво машин кто работат
	index_all = int(index_all3)

	if (index_all == 1):
						db.shange_nomber(1, message.from_user.id)




	db.update_status_car_off(message.from_user.id)


	print (index_all)

	# сверху код для продолжения робочего количества номера#


	X__TIME = (time.strftime(" %X ", time.localtime()))



	time_alll = X__TIME.replace(':','')

	db.shange_time_minus(time_alll,message.from_user.id)

	time_my = db.get_time_minus_for_me(message.from_user.id)
	time_my_str = str(time_my[0][0])
	index_MY_str = len(str(time_my_str))
	print (index_MY_str) # КОЛИЧЕСТВО ЦИФР В ЧИСЛЕ TIME_MINUS
	if index_MY_str < 6:
	   db.shange_night(1,message.from_user.id)
	else:
	   db.shange_night(0,message.from_user.id)

	time_int = int(time_alll)
	print (time_int)
	

	INDEX_ALL_123 = (len(str(time_int)))
	print ("111", INDEX_ALL_123)

	if INDEX_ALL_123 == 6:
		db.shange_all_night_off()



@dp.message_handler(commands=['Принял'])
async def subscribe(message: types.Message):


	index_all2 = db.get_index_all_car()  # текст всех мащин кто рабоатет
	index_all3 = (len(index_all2))  # количесво машин кто работат
	index_all = int(index_all3)
	db.update_status_car_on(message.from_user.id)

	allnomber_min1 = db.get_allV2()
	X__TIME = (time.strftime(" %X ", time.localtime()))

	time_alll = X__TIME.replace(':', '')

	db.shange_time_minus(time_alll, message.from_user.id)
	print (time_alll)

	time_int = int(time_alll)
	print (time_int)
	

	INDEX_ALL_123 = (len(str(time_int)))
	print ("111", INDEX_ALL_123)
	
	
	



	

	niight_off = db.get_time_minus_night_OFF() # все машины с night 0
	niight_off.sort()
	niight_off_str = str(niight_off)
	print (niight_off_str)
	if niight_off_str != "[]":


		if str(niight_off)== "[]":
			await message.answer("Нет машин")

		
		else:


			ttt = str(niight_off[0][0])
			print ("120", ttt)
			textoftime = db.get_index_all_car_of_time_minus(ttt)
			texttt = str(textoftime)
			print ("122", texttt)
			await message.answer("Cледующий" + texttt)
	else:

		niight_on = db.get_time_minus_night_ON() # все машины с night 1
		niight_on.sort()

		
		
		if str(niight_on)== "[]":
			await message.answer("Нет машин")

		
		else:
			ttt = str(niight_on[0][0])
			print ("120", ttt)
			textoftime = db.get_index_all_car_of_time_minus(ttt)
			texttt = str(textoftime)
			print ("122", texttt)
			await message.answer("Cледующий" + texttt)


	time_my = db.get_time_minus_for_me(message.from_user.id)
	time_my_str = str(time_my[0][0])
	index_MY_str = len(str(time_my_str))
	print (index_MY_str) # КОЛИЧЕСТВО ЦИФР В ЧИСЛЕ TIME_MINUS
	if index_MY_str < 6:
	   db.shange_night(1,message.from_user.id)
	else:
	   db.shange_night(0,message.from_user.id)

	if INDEX_ALL_123 == 6:
		db.shange_all_night_off()


@dp.message_handler(commands=['УЕХАЛ'])
async def subscribe(message: types.Message):
	db.update_status_car_off(message.from_user.id)
	db.update_subscription_off(message.from_user.id)
	time_miinus_all = db.get_time_minus()
	time_miinus_all.sort()
	ttt = time_miinus_all[0][0]
	textoftime = db.get_index_all_car_of_time_minus(ttt)
	texttt = str(textoftime)
	await message.answer("Cледующий" + texttt)












@dp.message_handler(commands=['1'])
async def unsubscribe(message: types.Message):
	db.shange_call(0, message.from_user.id)

	db.update_status_car_off(message.from_user.id)
	time_miinus_all = db.get_time_minus__()

	max_time_minus = min(time_miinus_all)
	

	ttt = max_time_minus[0]
	print("ЛОЖНЫЙ")
	INTTT = int(ttt) - 1

	db.shange_time_minus(INTTT, message.from_user.id)





@dp.message_handler(commands=['СВОБОДЕН'])
async def subscribe(message: types.Message):
	db.update_status_car_off(message.from_user.id)
	X__TIME = (time.strftime(" %X ", time.localtime()))



	time_alll = X__TIME.replace(':','')



	
	niight_off = db.get_time_minus_night_OFF() # все машины с night 0
	niight_off.sort()
	niight_off_str = str(niight_off)
	print (niight_off_str)
	if niight_off_str != "[]":
		time_my = db.get_time_minus_for_me(message.from_user.id)
		time_my_str = str(time_my[0][0])
		index_MY_str = len(str(time_my_str))
		print (index_MY_str) # КОЛИЧЕСТВО ЦИФР В ЧИСЛЕ TIME_MINUS
		if index_MY_str < 6:

			db.shange_night(1,message.from_user.id)
		else:
		    db.shange_night(0,message.from_user.id)

		db.shange_time_minus(time_alll,message.from_user.id)
		time_miinus_all = db.get_time_minus_night_OFF()

		print (time_miinus_all)
		time_miinus_all.sort()
		ttt = time_miinus_all[0][0]
		textoftime = db.get_index_all_car_of_time_minus(ttt)
		texttt = str(textoftime)
		await message.answer("Cледующий" + texttt)
		
	else:
		time_my = db.get_time_minus_for_me(message.from_user.id)
		time_my_str = str(time_my[0][0])
		index_MY_str = len(str(time_my_str))
		print (index_MY_str) # КОЛИЧЕСТВО ЦИФР В ЧИСЛЕ TIME_MINUS
		if index_MY_str < 6:

			db.shange_night(1,message.from_user.id)
		else:
			db.shange_night(0,message.from_user.id)
		db.shange_time_minus(time_alll,message.from_user.id)
		time_miinus_all = db.get_time_minus_night_ON()

		print (time_miinus_all)
		time_miinus_all.sort()
		ttt = time_miinus_all[0][0]
		textoftime = db.get_index_all_car_of_time_minus(ttt)
		texttt = str(textoftime)
		await message.answer("Cледующий" + texttt)

	time_my = db.get_time_minus_for_me(message.from_user.id)
	time_my_str = str(time_my[0][0])
	index_MY_str = len(str(time_my_str))
	print (index_MY_str) # КОЛИЧЕСТВО ЦИФР В ЧИСЛЕ TIME_MINUS
	if index_MY_str < 6:
	   db.shange_night(1,message.from_user.id)
	else:
	   db.shange_night(0,message.from_user.id)

	if INDEX_ALL_123 == 6:
		db.shange_all_night_off()





@dp.message_handler(commands=['ИНФОРМАЦИЯ'])
async def subscribe(message: types.Message):
	pay = db.get_index_for_ifo_pay()
	niight_off = db.get_time_minus_night_OFF() # все машины с night 0
	niight_off.sort()
	niight_off_str = str(niight_off)
	




	X__TIME = (time.strftime(" %X ", time.localtime()))

	time_alll = X__TIME.replace(':', '')

	time_miinus_all = db.get_time_minus()

	time_miinus_all.sort()
	for_update = str(time_miinus_all)
	if niight_off_str != "[]":

	 if for_update == "[]":
		 await message.answer("Свободный:" + "\nНа вызове:" + str(pay) + "\nСледующий: Нет машин")
	 else:
		 gg1 = db.get_time_minus_night_OFF()
		 gg1.sort()

		 gg2 = str(gg1[0][0])
		 textoftime = db.get_index_all_car_of_time_minus(gg2)
		 texttt = str(textoftime)

		 try1 = db.get_time_minus_night_OFF()
		 try1.sort()
		 print(try1)
		 try2 = (len(try1))

		 if try2 == 1:
			 f_1_free = str(try1[0][0])
			 text_1_free = db.get_index_all_car_of_time_minus(f_1_free)
			 await message.answer("Свободный:" + str(text_1_free) + "\nНа вызове:" + str(pay) + "\nСледующий:" + texttt)

		 elif try2 == 2:

			 f_1_free = str(try1[0][0])
			 text_1_free = db.get_index_all_car_of_time_minus(f_1_free)
			 print(text_1_free)
			 f_2_free = str(try1[1][0])

			 text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

			 await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)

		 elif try2 == 3:

			 f_1_free = str(try1[0][0])
			 text_1_free = db.get_index_all_car_of_time_minus(f_1_free)
			 print(text_1_free)
			 f_2_free = str(try1[1][0])

			 text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

			 f_3_free = str(try1[2][0])

			 text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

			 await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)



		 elif try2 == 4:

			 f_1_free = str(try1[0][0])
			 text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

			 f_2_free = str(try1[1][0])
			 text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

			 f_3_free = str(try1[2][0])
			 text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

			 f_4_free = str(try1[3][0])
			 text_4_free = db.get_index_all_car_of_time_minus(f_4_free)
			 await message.answer("Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(
				text_4_free) + "\nНа вызове:" + str(pay) + "\nСледующий:" + texttt)

		 elif try2 == 5:

			 f_1_free = str(try1[0][0])
			 text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

			 f_2_free = str(try1[1][0])
			 text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

			 f_3_free = str(try1[2][0])
			 text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

			 f_4_free = str(try1[3][0])
			 text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

			 f_5_free = str(try1[4][0])
			 text_5_free = db.get_index_all_car_of_time_minus(f_5_free)
			 await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + "\nНа вызове:" + str(pay) + "\nСледующий:" + texttt)

		 elif try2 == 6:

			 f_1_free = str(try1[0][0])
			 text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

			 f_2_free = str(try1[1][0])
			 text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

			 f_3_free = str(try1[2][0])
			 text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

			 f_4_free = str(try1[3][0])
			 text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

			 f_5_free = str(try1[4][0])
			 text_5_free = db.get_index_all_car_of_time_minus(f_5_free)

			 f_6_free = str(try1[5][0])
			 text_6_free = db.get_index_all_car_of_time_minus(f_6_free)
			 await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + str(text_6_free) + "\nНа вызове:" + str(pay) + "\nСледующий:" + texttt)


		 elif try2 == 7:

			 f_1_free = str(try1[0][0])
			 text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

			 f_2_free = str(try1[1][0])
			 text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

			 f_3_free = str(try1[2][0])
			 text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

			 f_4_free = str(try1[3][0])
			 text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

			 f_5_free = str(try1[4][0])
			 text_5_free = db.get_index_all_car_of_time_minus(f_5_free)

			 f_6_free = str(try1[5][0])
			 text_6_free = db.get_index_all_car_of_time_minus(f_6_free)

			 f_7_free = str(try1[6][0])
			 text_7_free = db.get_index_all_car_of_time_minus(f_7_free)
			 await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + str(text_6_free) + str(text_7_free) + "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)

		 elif try2 == 8:

			 f_1_free = str(try1[0][0])
			 text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

			 f_2_free = str(try1[1][0])
			 text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

			 f_3_free = str(try1[2][0])
			 text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

			 f_4_free = str(try1[3][0])
			 text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

			 f_5_free = str(try1[4][0])
			 text_5_free = db.get_index_all_car_of_time_minus(f_5_free)

			 f_6_free = str(try1[5][0])
			 text_6_free = db.get_index_all_car_of_time_minus(f_6_free)

			 f_7_free = str(try1[6][0])
			 text_7_free = db.get_index_all_car_of_time_minus(f_7_free)

			 f_8_free = str(try1[7][0])
			 text_8_free = db.get_index_all_car_of_time_minus(f_8_free)
			 await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + str(text_6_free) + str(text_7_free) + str(text_8_free) + "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)

		 elif try2 == 9:

			 f_1_free = str(try1[0][0])
			 text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

			 f_2_free = str(try1[1][0])
			 text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

			 f_3_free = str(try1[2][0])
			 text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

			 f_4_free = str(try1[3][0])
			 text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

			 f_5_free = str(try1[4][0])
			 text_5_free = db.get_index_all_car_of_time_minus(f_5_free)

			 f_6_free = str(try1[5][0])
			 text_6_free = db.get_index_all_car_of_time_minus(f_6_free)

			 f_7_free = str(try1[6][0])
			 text_7_free = db.get_index_all_car_of_time_minus(f_7_free)

			 f_8_free = str(try1[7][0])
			 text_8_free = db.get_index_all_car_of_time_minus(f_8_free)

			 f_9_free = str(try1[8][0])
			 text_9_free = db.get_index_all_car_of_time_minus(f_9_free)
			 await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + str(text_6_free) + str(text_7_free) + str(text_8_free) + str(text_9_free) + "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)

		 elif try2 == 10:

			 f_1_free = str(try1[0][0])
			 text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

			 f_2_free = str(try1[1][0])
			 text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

			 f_3_free = str(try1[2][0])
			 text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

			 f_4_free = str(try1[3][0])
			 text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

			 f_5_free = str(try1[4][0])
			 text_5_free = db.get_index_all_car_of_time_minus(f_5_free)

			 f_6_free = str(try1[5][0])
			 text_6_free = db.get_index_all_car_of_time_minus(f_6_free)

			 f_7_free = str(try1[6][0])
			 text_7_free = db.get_index_all_car_of_time_minus(f_7_free)

			 f_8_free = str(try1[7][0])
			 text_8_free = db.get_index_all_car_of_time_minus(f_8_free)

			 f_9_free = str(try1[8][0])
			 text_9_free = db.get_index_all_car_of_time_minus(f_9_free)

			 f_10_free = str(try1[9][0])
			 text_10_free = db.get_index_all_car_of_time_minus(f_10_free)
			 await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + str(text_6_free) + str(text_7_free) + str(text_8_free) + str(text_9_free) + str(text_10_free) + "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)
	else:


		if for_update == "[]":
			await message.answer("Свободный:" + "\nНа вызове:" + str(pay) + "\nСледующий: Нет машин")


		else:

		


			ttt = time_miinus_all[0][0]
			print(ttt)
			textoftime = db.get_index_all_car_of_time_minus(ttt)
			texttt = str(textoftime)

			try1 = db.get_time_minus_night_ON()
			try1.sort()
			print(try1)
			try2 = (len(try1))

			if try2 == 1:
				f_1_free = str(try1[0][0])
				text_1_free = db.get_index_all_car_of_time_minus(f_1_free)
				await message.answer("Свободный:" + str(text_1_free) + "\nНа вызове:" + str(pay) + "\nСледующий:" + texttt)

			elif try2 == 2:

				f_1_free = str(try1[0][0])
				text_1_free = db.get_index_all_car_of_time_minus(f_1_free)
				print(text_1_free)
				f_2_free = str(try1[1][0])

				text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

				await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)

			elif try2 == 3:

				f_1_free = str(try1[0][0])
				text_1_free = db.get_index_all_car_of_time_minus(f_1_free)
				print(text_1_free)
				f_2_free = str(try1[1][0])

				text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

				f_3_free = str(try1[2][0])

				text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

				await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)



			elif try2 == 4:

				f_1_free = str(try1[0][0])
				text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

				f_2_free = str(try1[1][0])
				text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

				f_3_free = str(try1[2][0])
				text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

				f_4_free = str(try1[3][0])
				text_4_free = db.get_index_all_car_of_time_minus(f_4_free)
				await message.answer("Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(
				text_4_free) + "\nНа вызове:" + str(pay) + "\nСледующий:" + texttt)

			elif try2 == 5:

				f_1_free = str(try1[0][0])
				text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

				f_2_free = str(try1[1][0])
				text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

				f_3_free = str(try1[2][0])
				text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

				f_4_free = str(try1[3][0])
				text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

				f_5_free = str(try1[4][0])
				text_5_free = db.get_index_all_car_of_time_minus(f_5_free)
				await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + "\nНа вызове:" + str(pay) + "\nСледующий:" + texttt)

			elif try2 == 6:

				f_1_free = str(try1[0][0])
				text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

				f_2_free = str(try1[1][0])
				text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

				f_3_free = str(try1[2][0])
				text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

				f_4_free = str(try1[3][0])
				text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

				f_5_free = str(try1[4][0])
				text_5_free = db.get_index_all_car_of_time_minus(f_5_free)

				f_6_free = str(try1[5][0])
				text_6_free = db.get_index_all_car_of_time_minus(f_6_free)
				await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + str(text_6_free) + "\nНа вызове:" + str(pay) + "\nСледующий:" + texttt)


			elif try2 == 7:

				f_1_free = str(try1[0][0])
				text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

				f_2_free = str(try1[1][0])
				text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

				f_3_free = str(try1[2][0])
				text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

				f_4_free = str(try1[3][0])
				text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

				f_5_free = str(try1[4][0])
				text_5_free = db.get_index_all_car_of_time_minus(f_5_free)

				f_6_free = str(try1[5][0])
				text_6_free = db.get_index_all_car_of_time_minus(f_6_free)

				f_7_free = str(try1[6][0])
				text_7_free = db.get_index_all_car_of_time_minus(f_7_free)
				await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + str(text_6_free) + str(text_7_free) + "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)

			elif try2 == 8:

				f_1_free = str(try1[0][0])
				text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

				f_2_free = str(try1[1][0])
				text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

				f_3_free = str(try1[2][0])
				text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

				f_4_free = str(try1[3][0])
				text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

				f_5_free = str(try1[4][0])
				text_5_free = db.get_index_all_car_of_time_minus(f_5_free)

				f_6_free = str(try1[5][0])
				text_6_free = db.get_index_all_car_of_time_minus(f_6_free)

				f_7_free = str(try1[6][0])
				text_7_free = db.get_index_all_car_of_time_minus(f_7_free)

				f_8_free = str(try1[7][0])
				text_8_free = db.get_index_all_car_of_time_minus(f_8_free)


				await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + str(text_6_free) + str(text_7_free) + str(f_8_free) + "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)

			elif try2 == 9:

				f_1_free = str(try1[0][0])
				text_1_free = db.get_index_all_car_of_time_minus(f_1_free)

				f_2_free = str(try1[1][0])
				text_2_free = db.get_index_all_car_of_time_minus(f_2_free)

				f_3_free = str(try1[2][0])
				text_3_free = db.get_index_all_car_of_time_minus(f_3_free)

				f_4_free = str(try1[3][0])
				text_4_free = db.get_index_all_car_of_time_minus(f_4_free)

				f_5_free = str(try1[4][0])
				text_5_free = db.get_index_all_car_of_time_minus(f_5_free)

				f_6_free = str(try1[5][0])
				text_6_free = db.get_index_all_car_of_time_minus(f_6_free)

				f_7_free = str(try1[6][0])
				text_7_free = db.get_index_all_car_of_time_minus(f_7_free)

				f_8_free = str(try1[7][0])
				text_8_free = db.get_index_all_car_of_time_minus(f_8_free)

				f_9_free = str(try1[8][0])
				text_9_free = db.get_index_all_car_of_time_minus(f_9_free)


				await message.answer(
				"Свободный:" + str(text_1_free) + str(text_2_free) + str(text_3_free) + str(text_4_free) + str(
					text_5_free) + str(text_6_free) + str(text_7_free) + str(f_8_free) + str(f_9_free) +  "\nНа вызове:" + str(
					pay) + "\nСледующий:" + texttt)


@dp.message_handler(commands=['БАРДЮР'])
async def subscribe(message: types.Message):

	index_all2 = db.get_index_all_car()  # текст всех мащин кто рабоатет
	index_all3 = (len(index_all2))  # количесво машин кто работат
	index_all = int(index_all3)
	db.update_status_car_on(message.from_user.id)

	allnomber_min1 = db.get_allV2()
	X__TIME = (time.strftime(" %X ", time.localtime()))

	time_alll = X__TIME.replace(':', '')

	db.shange_time_minus(time_alll, message.from_user.id)
	print (time_alll)

	time_int = int(time_alll)
	print (time_int)
	

	INDEX_ALL_123 = (len(str(time_int)))
	print ("111", INDEX_ALL_123)
	
	
	



	

	niight_off = db.get_time_minus_night_OFF() # все машины с night 0
	niight_off.sort()
	niight_off_str = str(niight_off)
	print (niight_off_str)
	if niight_off_str != "[]":


		if str(niight_off)== "[]":
			await message.answer("Нет машин")

		
		else:


			ttt = str(niight_off[0][0])
			print ("120", ttt)
			textoftime = db.get_index_all_car_of_time_minus(ttt)
			texttt = str(textoftime)
			print ("122", texttt)
			await message.answer("Cледующий" + texttt)
	else:

		niight_on = db.get_time_minus_night_ON() # все машины с night 1
		niight_on.sort()

		
		
		if str(niight_on)== "[]":
			await message.answer("Нет машин")

		
		else:
			ttt = str(niight_on[0][0])
			print ("120", ttt)
			textoftime = db.get_index_all_car_of_time_minus(ttt)
			texttt = str(textoftime)
			print ("122", texttt)
			await message.answer("Cледующий" + texttt)


	time_my = db.get_time_minus_for_me(message.from_user.id)
	time_my_str = str(time_my[0][0])
	index_MY_str = len(str(time_my_str))
	print (index_MY_str) # КОЛИЧЕСТВО ЦИФР В ЧИСЛЕ TIME_MINUS
	if index_MY_str < 6:
	   db.shange_night(1,message.from_user.id)
	else:
	   db.shange_night(0,message.from_user.id)

	if INDEX_ALL_123 == 6:
		db.shange_all_night_off()


# кто будет некст 

@dp.message_handler(commands=['ПЕРСОНАЛЬНЫЙ'])
async def subscribe(message: types.Message):
	index_all2 = db.get_index_all_car()  # текст всех мащин кто рабоатет
	index_all3 = (len(index_all2))  # количесво машин кто работат
	index_all = int(index_all3)
	db.update_status_car_on(message.from_user.id)

	allnomber_min1 = db.get_allV2()
	X__TIME = (time.strftime(" %X ", time.localtime()))

	time_alll = X__TIME.replace(':', '')

	db.shange_time_minus(time_alll, message.from_user.id)
	print (time_alll)

	time_int = int(time_alll)
	print (time_int)
	

	INDEX_ALL_123 = (len(str(time_int)))
	print ("111", INDEX_ALL_123)
	
	
	



	

	niight_off = db.get_time_minus_night_OFF() # все машины с night 0
	niight_off.sort()
	niight_off_str = str(niight_off)
	print (niight_off_str)
	if niight_off_str != "[]":


		if str(niight_off)== "[]":
			await message.answer("Нет машин")

		
		else:


			ttt = str(niight_off[0][0])
			print ("120", ttt)
			textoftime = db.get_index_all_car_of_time_minus(ttt)
			texttt = str(textoftime)
			print ("122", texttt)
			await message.answer("Cледующий" + texttt)
	else:

		niight_on = db.get_time_minus_night_ON() # все машины с night 1
		niight_on.sort()

		
		
		if str(niight_on)== "[]":
			await message.answer("Нет машин")

		
		else:
			ttt = str(niight_on[0][0])
			print ("120", ttt)
			textoftime = db.get_index_all_car_of_time_minus(ttt)
			texttt = str(textoftime)
			print ("122", texttt)
			await message.answer("Cледующий" + texttt)


	time_my = db.get_time_minus_for_me(message.from_user.id)
	time_my_str = str(time_my[0][0])
	index_MY_str = len(str(time_my_str))
	print (index_MY_str) # КОЛИЧЕСТВО ЦИФР В ЧИСЛЕ TIME_MINUS
	if index_MY_str < 6:
	   db.shange_night(1,message.from_user.id)
	else:
	   db.shange_night(0,message.from_user.id)

	if INDEX_ALL_123 == 6:
		db.shange_all_night_off()





if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)









