username = input("Ваше ім'я: ")
email = input("Поштова скринька: ")

print(f"\nДякую! Акаунт для {username} успішно створено.")
print("-" * 40)

exercises = ["присідання", "віджимання", "підтягування", "стрибки"]
training_active = True

while training_active == True:
    print("\nДоступні вправи:")
    print(f"0 - {exercises[0]}, 1 - {exercises[1]}, 2 - {exercises[2]}, 3 - {exercises[3]}")
    
    exercise_number = int(input("\nВведи номер вправи (від 0 до 3): "))
    reps = int(input(f"Скільки разів ти зробив '{exercises[exercise_number]}'? "))
    
    if reps > 15:
        print("🔥 Крутий результат, так тримати!")
    else:
        print("💪 Хороша розминка, але наступного разу піднажмемо!")
        
    print(f"✅ Записано: {username} зробив {reps} повторень вправи '{exercises[exercise_number]}'")
    print("-" * 40)
    
    user_choice = input("Продовжуємо тренування? (так/ні): ")
    if user_choice == "ні":
        training_active = False

print("\nТренування завершено! Дані збережено. Гарного відпочинку! 🏆")
