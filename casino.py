import os
import random
import user_statistic


def show_location(u_stat):
	is_busy = True
	u_bet = 0
	u_score = 0
	while is_busy:
		os.system("cls")
		user_statistic.show_stat(u_stat)
		print("А вот и казино - место где проигрывают жизнь, зато вкусная еда).")
		print("1 — Сделать ставку")
		print("2 — Уйти пока всё хорошо")
		u_stat["Выбор"] = input("Что делать? ")

		if u_stat["Выбор"] == "1":
			u_bet = int(input("Сколько поставишь на игру? "))
			if u_bet > u_stat["Бюджет"]:
				print(f'Прости {u_stat["Имя"]} я не могу предоставить тебе кредит. Возвращяйся когда ты станешь... М-м-м... побогаче') #"Прости", u_stat["Имя"], "я не могу предоставить тебе кредит. Возвращяйся когда ты станешь... М-м-м... побогаче"
			elif u_bet < 1 or type(u_bet) == str:
				print(f"Чел... ты...")
			else:
				u_score = random.randint(2, 12)
				casino_score = random.randint(2, 12)
				print(u_stat["Имя"], f"выбросил", {u_score})
				print(f"У казино {casino_score}")

				if u_score > casino_score:
					u_stat["Бюджет"] += u_bet
					print("Опа!", u_stat["Имя"], f"выиграл {u_bet}!")
				elif u_score < casino_score:
					u_stat["Бюджет"] -= u_bet
					print("Молодец!", u_stat["Имя"], f"проиграл {u_bet}! Иди на завод!")
				else:
					print("Ничья!")
		
		elif u_stat["Выбор"] == "2":
			is_busy = False
			print(u_stat["Имя"], "убежал куда подальше.")		
		else:
			print("Мне кажется ты что-то не понял.")

		input("ENTER — дальше")
