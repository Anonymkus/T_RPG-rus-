import os
import user_statistic


def show_market_place(u_stat):
	is_busy = True
	potion_prise = 100
	while is_busy:
		os.system("cls")
		user_statistic.show_stat(u_stat)
		print(f"1 — Купить боярышник за {potion_prise}.")
		print("2 — Пойти выключить несуществующий утюг.")
		u_stat["Выбор"] = input("Что делать? ")

		if u_stat["Выбор"] == "1" and u_stat["Бюджет"] >= potion_prise:
			u_stat["Бюджет"] -= potion_prise
			u_stat["Инвентарь"].append("боярышник")
			print(u_stat["Имя"], "купил боярышник.")
		elif u_stat["Выбор"] == "1" and u_stat["Бюджет"] < potion_prise:
			print("У", u_stat["Имя"], "маловато рупий... Ой это не оттуда.")
		elif u_stat["Выбор"] == "2":
			is_busy = False
			print(u_stat["Имя"], "решил не отдавать вещь и пошёл в бан.")
		else:
			print("У меня ощущение, что ты что-то не догоняешь.")

		input("ENTER — дальше")
