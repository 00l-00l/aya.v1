import os
if os.path.exists("memory.txt"):
 with open("memory.txt", "r", encoding="utf-8") as f:
    user_name = f.read()
else:
    user_name = input("КАК К ВАМ ОБРАЩАТЬСЯ? ").lower()
    with open("memory.txt", "w", encoding="utf-8") as f:
        f.write(user_name)

def hello(name, aya_config):
  print("Версия:", aya_config["version"])
  print("Владелец:", aya_config["owner"])
  print("Активен:", aya_config["active"])
  print(f"ДОБРО ПОЖАЛОВАТЬ {name}")

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



aya_config = {
       "version": "V 1.0",
       "owner": user_name,
       "active": True       
}
if check_user(user_name):
      hello(user_name, aya_config)
      while True:
       command = input("ВВЕДИТЕ КОМАНДУ ").lower()
       if  hundle_command(command) == False:
            break
else:
   print("ДОСТУП ЗАПРЕЩЁН!")

