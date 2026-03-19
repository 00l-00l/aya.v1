def hello(name):
    print(f"ДОБРО ПОЖАЛОВАТЬ! {name} Ая V.01 ГОТОВА К РАБОТЕ")

def check_user(name):
 if name == "сэр":
    return(True)
 else:
    return(False)
 
def hundle_command(command):
   if command == "время":
      print("ФУНКЦИЯ В РАЗРАБОТКЕ ОБРАТИТЕСЬ ПОЗЖЕ")
   elif command == "погода":
      print("ФУНКЦИЯ В РАЗРАБОТКЕ ОБРАТИТЕСЬ ПОЗЖЕ")
   elif command == "выход":
      print("ДО СВИДАНИЯ!")
      return False
   else: 
      print("ERROR")

aya_active = True
user_name = input("КАК К ВАМ ОБРАЩАТЬСЯ? ").lower()
if check_user(user_name):
      hello(user_name)
      while True:
       command = input("ВВЕДИТЕ КОМАНДУ ")
       hundle_command(command) == False
       break
else:
   print("ДОСТУП ЗАПРЕЩЁН!")