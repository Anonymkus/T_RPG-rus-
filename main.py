import os 
import casino
import user_statistic
import market
import arena
import save_load
import os.path


game = True
u_stat = {
	"Имя" : 0,
	"Возраст" : 0,
	"Бюджет" : 500,
	"Здоровье" : 100,
	"Сила" : 10,
	"Инвентарь" : ["чупик"],
	"Выбор" : 0,
	"Удача" : 1
}
print("Привет обитатель интернета, добро пожаловать в примитивную игрушку на Python")
print("Чтобы у тебя было ощущение выбора хоть где-то, ")
print("напиши сам данные своего персонажа, не забудь нажать на ENTER")
u_stat["Возраст"] = input("Сколько тебе лет милок? ")
u_stat["Имя"] = input("А звать тeбя то как? ") 
print("Ты прoснулся где-тo, а главнoе зачем-тo. Гoлoва твoя бoлит, а пoп-ита как назлo нет")
print("И тут тебя посещает гениальная мысль пойти по 1-ой из 3 дорожек (или сделать плохой поступок)")
print("По странной и непонятной причине ты знаешь куда ведут дорожки")
input("ENTER - продолжить")


while game:	
	os.system("cls")
	user_statistic.show_stat(u_stat)
	print("Ты на развилке и тут есть три дорожки.")
	print("1 — Дорожка ведет в магаз. Я надеюсь что там есть что похавать")
	print("2 — Дорожка ведёт в казино, деньги есть, так что можно и сходить.")
	print("3 — Дорожка ведёт на махач с кем-то, сразу помянем.")
	print("4 — Сохранить игру")
	if os.path.isfile("save"):
		print("5 — Загрузить игру")
	print("0 — Выйти из игры")
	u_choice = input("Что делать? ")

	if u_choice == "1":
		market.show_market_place(u_stat)
	elif u_choice == "2":
		casino.show_location(u_stat)
	elif u_choice == "3":
		arena.show_location(u_stat)
	elif u_choice == "4":
		save_load.save(u_stat)
	elif u_choice == "5" and os.path.isfile("save"):
		save_load.load(u_stat)
	elif u_choice == "0":
		game = False
	else:
		print("Такого варианта нет, попробуйте другой.")
		input("ENTER — дальше")

print("Конец.")
