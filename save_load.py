def save(u_stat):
	with open("save", "w", encoding="utf-8") as file:
		file.write(u_stat["Имя"] + ",")
		file.write(str(u_stat["Возраст"]) + ",")
		file.write(str(u_stat["Бюджет"]) + ",")
		file.write(str(u_stat["Здоровье"]) + ",")
		file.write(str(u_stat["Удача"]) + ",")
		for item in u_stat["Инвентарь"]:
			file.write(item + ",")
			

def load(u_stat):
	with open("save", "r", encoding="utf-8") as file:
		hero_list = file.read().split(",")
		u_stat['Имя'] = hero_list[0]
		u_stat['Возраст'] = hero_list[1]
		u_stat['Бюджет'] = hero_list[2]
		u_stat['Здоровье'] = hero_list[3]
		u_stat['Удача'] = hero_list[4]
		u_stat['Инвентарь'] = hero_list[5:-1:1]
		input("pause")
	
	