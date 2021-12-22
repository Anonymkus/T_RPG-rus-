import os
import user_statistic
from random import choice


def show_location(u_stat):
	is_busy = True
	while is_busy:
		os.system("cls")
		user_statistic.show_stat(u_stat)
		print(f"{u_stat['Имя']} вошел на арену.")
		print("1 — Сражаться")
		print("2 — Вернуться в лагерь")
		user_choice = input("Что делать? ")
		if user_choice == "1":
			enemy_first_names = ["Поц", "Клоун", "Чертилла"]
			enemy_second_names = ["Тупой", "Обыкновенный", "Обоссаный"]
			enemy_name = choice(enemy_first_names) + " " + choice(enemy_second_names)
			enemy_hp = 100
			is_fighting = True
			while is_fighting:
				os.system("cls")
				user_statistic.show_stat(u_stat)
				print(f"Погоняло твоего соперника: {enemy_name}")
				print(f"Здоровья только: {enemy_hp}")
				print("GLHF")
				print("")
				print("1 - Атаковать")
				print("2 - Защищаться")
				if "боярышник" in u_stat["Инвентарь"]:
					print("3 - Выпить зелье")
				u_choice = input("Что делать? ")

				if u_choice == "1":
					enemy_hp -= 10
					print(f"{enemy_name} коцан на 10")
				elif u_choice == "2":
					u_stat['Здоровье'] -= 10
					print(f"{u_stat['Имя']} поймал маслину 10")
				elif u_choice == "3" and "зелье" in u_stat["Инвентарь"]:
					print(f"{u_stat['Имя']} подвыпил и похилился")
					u_stat["Инвентарь"].remove("боярышник")
					u_stat["Имя"] = 100
				else:
					print("Ты опять не догоняешь, и опять меня разачаровываешь.")

				input("ENTER — продолжить")

		elif user_choice == "2":
			is_busy = False
			print(f"{u_stat['Имя']} стикал с села.")
		else:
			print(f"Давай по новой {u_stat['Имя']}, все плохо.")

		input("ENTER — дальше")
