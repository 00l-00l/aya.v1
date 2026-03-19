def hello(name):
   print(f"Добро Пожаловать! {name}", "Ая v.1 активирована")

def hundle_command(command):
        
       if command ==  "время":
         print("Функция времени в разработке")

       elif command =="погода":
         print("Функция погоды в разработке")

       elif command =="выход":
         print("До свидания")
         

       else:
         print("Команда не распознана")
  

aya_active = True
user_name = input("Как вас зовут? ")
if user_name == "Сэр":
    hello(user_name)
    while True:
     command = input("Введите команду ").lower()
     hundle_command(command)
     