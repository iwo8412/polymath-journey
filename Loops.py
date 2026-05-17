training_active = True

while training_active == True:
    reps = int(input("Скільки повторень ти зробив? "))
    
    if reps > 15:
        print("Крутий результат, так тримати!")
    else:
        print("Хороша розминка, але наступного разу піднажмемо!")
        
    user_choice = input("Продовжуємо тренування? (так/ні): ")
    if user_choice == "ні":
        training_active = False
