
import random


brand_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 120, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 35, "gladness_less": 1}
}


class Pet:
    def __init__(self, name="Murzyk"):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def eat(self):
        self.hunger = max(0, self.hunger - 30)
        print(f"{self.name} has eaten.")

    def play(self):
        self.happiness = min(100, self.happiness + 15)
        print(f"The human plays with {self.name}.")

    def live(self):
        self.hunger = min(100, self.hunger + 10)
        self.happiness = max(0, self.happiness - 5)

        if self.hunger >= 70:
            self.eat()

        if self.happiness < 50:
            self.play()


class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = None
        self.car = None
        self.home = None
        self.pet = None

    def get_home(self):
        self.home = House()
        print(f"{self.name} moved into a house.")

    def get_car(self):
        self.car = Auto(brand_of_car)
        print(f"{self.name} bought a {self.car.brand}.")

    def get_job(self):
        self.job = Job(job_list)
        print(
            f"{self.name} got a job as a "
            f"{self.job.job}."
        )

    def get_pet(self):
        self.pet = Pet()
        print(f"{self.name} got a pet named {self.pet.name}.")

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")

        if self.home.food > 0:
            self.home.food -= 1
            self.satiety = min(100, self.satiety + 20)
            print(f"{self.name} has eaten.")

    def work(self):
        self.money += self.job.salary
        self.gladness = max(
            0, self.gladness - self.job.gladness_less
        )
        self.satiety = max(0, self.satiety - 10)
        print(f"{self.name} is working and earning money.")

    def shopping(self, manage):
        if manage == "food":
            if self.money >= 20:
                self.money -= 20
                self.home.food += 5
                print("The human bought food.")
            else:
                print("Not enough money to buy food.")

        elif manage == "fuel":
            if self.money >= 30:
                self.money -= 30
                self.car.fuel += 50
                print("The human refueled the car.")
            else:
                print("Not enough money for fuel.")

    def chill(self):
        self.gladness = min(100, self.gladness + 10)
        self.home.mess += 5
        print(f"{self.name} is relaxing.")

    def clean_home(self):
        self.home.mess = 0
        self.gladness = max(0, self.gladness - 5)
        print("The house has been cleaned.")

    def to_repair(self):
        if self.money >= 30:
            self.money -= 30
            self.car.strength = min(150, self.car.strength + 30)
            print("The car has been repaired.")
        else:
            print("Not enough money for repairs.")

    def is_alive(self):
        if self.satiety <= 0:
            print(f"{self.name} is exhausted.")
            return False

        if self.gladness <= 0:
            print(f"{self.name} can no longer continue.")
            return False

        if self.money < -500:
            print(f"{self.name} is bankrupt.")
            return False

        return True

    def days_indexes(self, day):
        print(f"\n{' Day ' + str(day) + ' ':=^45}")
        print(f"Name: {self.name}")
        print(f"Money: {self.money}")
        print(f"Satiety: {self.satiety}")
        print(f"Gladness: {self.gladness}")
        print(f"Food at home: {self.home.food}")
        print(f"Mess: {self.home.mess}")
        print(f"Car: {self.car.brand}")
        print(f"Fuel: {self.car.fuel}")
        print(f"Car strength: {self.car.strength}")
        print(f"Job: {self.job.job}")
        print(f"Pet: {self.pet.name}")
        print(f"Pet hunger: {self.pet.hunger}")
        print(f"Pet happiness: {self.pet.happiness}")

    def live(self, day):
        if not self.is_alive():
            return False

        if self.home is None:
            self.get_home()

        if self.car is None:
            self.get_car()

        if self.job is None:
            self.get_job()

        if self.pet is None:
            self.get_pet()

        self.days_indexes(day)

        if self.satiety < 30:
            self.eat()

        elif self.gladness < 30:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()

        elif self.money < 0:
            self.work()

        elif self.car.strength < 20:
            self.to_repair()

        else:
            action = random.randint(1, 4)

            if action == 1:
                self.chill()
            elif action == 2:
                self.work()
            elif action == 3:
                self.clean_home()
            else:
                self.shopping("food")

        print("\nTaking care of the pet:")
        self.pet.live()

        return self.is_alive()


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True

        print("The car cannot move.")
        return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 10


class Job:
    def __init__(self, jobs):
        self.job = random.choice(list(jobs))
        self.salary = jobs[self.job]["salary"]
        self.gladness_less = jobs[self.job]["gladness_less"]



vasya_man = Human(name="Vasya")


for day in range(1, 8):
    if not vasya_man.live(day):
        print("Simulation ended.")
        break
else:
    print("\nThe simulation is complete. The human survived all 7 days.")
