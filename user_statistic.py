def show_stat(u_stat):
	print(f"Имя: {u_stat['Имя']}")
	print(f"Возраст: {u_stat['Возраст']}")
	print(f"Бюджет: {u_stat['Бюджет']}")
	print(f"Здоровье: {u_stat['Здоровье']}")
	print(f"Сила: {u_stat['Сила']}")
	print(f"Удача: {u_stat['Удача']}")
	print(f"Инвентарь:")
	for item in u_stat['Инвентарь']:
		print(" •", item)
	print("")
