aya_active = True
user_name = input("Как вас зовут? ")
if user_name == "Сэр":
    print(f"Добро Пожаловать! {user_name}",  "Ая v.1 активирована")
    command_count = 0
    while True:
     command = input("Введите команду ").lower() 
     command_count = command_count + 1
     if command ==  "время":
         print("Функция времени в разработке")

     elif command =="погода":
         print("Функция погоды в разработке")

     elif command =="выход":
         print("Выполнено команд:" f"{command_count}")
         print("До свидания")
         break

     else:
         print("Команда не распознана")
         

elif user_name == "Напарник":
   print(f"Добро пожаловать {user_name}",  "Ая v.1 активирована")
   
else:
 print("Доступ Запрещён!")
print("---")  