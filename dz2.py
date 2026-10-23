import random


class CatLife:
    def __init__(self):
        self.age = random.randint(1, 8)
        self.health = 100
        self.hunger = 0
        self.happiness = 70
        self.alive = True
        self.days_alive = 0

    def simulate_day(self, day):
        if not self.alive:
            return

        self.days_alive += 1
        events = []

        self.hunger += random.randint(5, 20)

        if random.random() < 0.75:
            self.hunger = max(0, self.hunger - random.randint(10, 30))
            events.append("Знайшов їжу та поїв.")
        else:
            events.append("Не зміг знайти їжу.")

        if random.random() < 0.8:
            events.append("Більшу частину дня спав.")

        event = random.random()

        if event < 0.10:
            self.happiness = min(100, self.happiness + 10)
            events.append("Грався та досліджував територію.")
        elif event < 0.15:
            self.health -= random.randint(5, 20)
            events.append("Потрапив у неприємність і отримав травму.")
        elif event < 0.22:
            self.health -= random.randint(1, 10)
            events.append("Почувався погано.")
        elif event < 0.30:
            self.happiness = max(0, self.happiness - 10)
            events.append("Злякався гучного шуму.")

        if self.hunger > 70:
            self.health -= 5
            events.append("Сильно зголоднів, здоров'я погіршилося.")

        # Природне відновлення
        if random.random() < 0.10:
            self.health = min(100, self.health + 5)
            events.append("Самопочуття покращилося.")

        self.health = max(0, min(100, self.health))

        if self.health <= 0:
            self.alive = False
            events.append("Кіт помер.")

        print(f"День {day}: " + " ".join(events))

    def simulate_year(self):
        print("\nПочинається новий рік життя кота.")
        print(f"Вік на початку року: {self.age} років")
        print("-" * 50)

        for day in range(1, 366):
            if not self.alive:
                break

            self.simulate_day(day)

        if self.alive:
            self.age += 1
            print("\nКіт пережив цей рік!")
        else:
            print("\nКіт не дожив до кінця року.")

        print("\nПІДСУМОК ЖИТТЯ")
        print(f"Вік: {self.age} років")
        print(f"Прожито днів у симуляції: {self.days_alive}")
        print(f"Здоров'я: {self.health}/100")
        print(f"Щастя: {self.happiness}/100")
        print(f"Статус: {'Живий' if self.alive else 'Помер'}")


cat = CatLife()

while cat.alive:
    input("\nНатисни Enter, щоб змоделювати наступний рік...")
    cat.simulate_year()

    if cat.alive:
        answer = input("\nПродовжити симуляцію? (так/ні): ").lower()
        if answer != "так":
            break

print("\nСимуляцію завершено.")
