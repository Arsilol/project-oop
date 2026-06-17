import random


class Disaster:
    def __init__(self, name):
        self.name = name


class FoodStorage:
    def __init__(self):
        self.sushi = 0
        self.bread = 0
        self.popcorn = 0

    def show(self):
        print("\n=== FOOD STORAGE ===")
        print(f"Sushi: {self.sushi}")
        print(f"Bread: {self.bread}")
        print(f"Popcorn: {self.popcorn}")


class Grain:
    def __init__(self, name, description, recommended_water):
        self.name = name
        self.description = description
        self.recommended_water = recommended_water
        self.quality = 100

    def grow(self):
        print(f"\nGrowing {self.name}")
        print(self.description)
        print(f"Recommended water: {self.recommended_water}%")

        water = int(input("Enter water percentage: "))

        self.quality = 100 - abs(self.recommended_water - water)

        print(f"Quality: {self.quality}%")

        if self.quality < 70:
            print("Quality too low. Harvest failed.")
            return False

        return True

    def harvest(self):
        print(f"{self.name} harvested successfully!")

    def make_food(self, storage):
        raise NotImplementedError

    def handle_disaster(self, disaster):
        raise NotImplementedError


class Rice(Grain):
    def __init__(self):
        super().__init__(
            "Rice",
            "Rice grows well in wet conditions.",
            70
        )

    def make_food(self, storage):
        print("Rice is being turned into Sushi.")
        storage.sushi += 1

    def handle_disaster(self, disaster):
        if disaster.name == "Flood":
            print("Rice likes water. Small damage!")
            self.quality -= 5

        elif disaster.name == "Drought":
            print("Rice suffers badly from drought!")
            self.quality -= 30

        elif disaster.name == "Storm":
            print("Rice is slightly damaged by the storm.")
            self.quality -= 15


class Wheat(Grain):
    def __init__(self):
        super().__init__(
            "Wheat",
            "Wheat is commonly used for bread.",
            40
        )

    def make_food(self, storage):
        print("Wheat is being turned into Bread.")
        storage.bread += 1

    def handle_disaster(self, disaster):
        if disaster.name == "Flood":
            print("Wheat suffers from flooding!")
            self.quality -= 25

        elif disaster.name == "Drought":
            print("Wheat survives drought reasonably well.")
            self.quality -= 10

        elif disaster.name == "Storm":
            print("Wheat is damaged by the storm.")
            self.quality -= 20


class Corn(Grain):
    def __init__(self):
        super().__init__(
            "Corn",
            "Corn is a tall grain plant.",
            90
        )

    def make_food(self, storage):
        print("Corn is being turned into Popcorn.")
        storage.popcorn += 1

    def handle_disaster(self, disaster):
        if disaster.name == "Flood":
            print("Corn suffers moderate flood damage.")
            self.quality -= 15

        elif disaster.name == "Drought":
            print("Corn suffers from drought.")
            self.quality -= 20

        elif disaster.name == "Storm":
            print("Corn withstands the storm fairly well.")
            self.quality -= 5


class Farm:
    def __init__(self):
        self.crops = []

    def add_crop(self, crop):
        self.crops.append(crop)

    def show_crops(self):
        if not self.crops:
            print("No crops.")
            return False

        print("\nCurrent crops:")

        for i, crop in enumerate(self.crops, start=1):
            print(f"{i}. {crop.name} ({crop.quality}% quality)")

        return True

    def make_food(self, storage):
        if not self.show_crops():
            return

        choice = int(input("Choose crop number: "))

        if 1 <= choice <= len(self.crops):
            crop = self.crops.pop(choice - 1)

            
            crop.make_food(storage)

        else:
            print("Invalid choice.")


def random_disaster(crop):
    disasters = [
        Disaster("Flood"),
        Disaster("Drought"),
        Disaster("Storm")
    ]

    if random.randint(1, 100) <= 30:
        disaster = random.choice(disasters)

        print(f"\nDISASTER OCCURRED: {disaster.name}")

       
        crop.handle_disaster(disaster)

        if crop.quality < 0:
            crop.quality = 0

        print(f"New quality: {crop.quality}%")


def test_rice_food():
    storage = FoodStorage()
    rice = Rice()

    rice.make_food(storage)

    assert storage.sushi == 1
    assert storage.bread == 0
    assert storage.popcorn == 0

    print("Rice food test passed")


def test_wheat_food():
    storage = FoodStorage()
    wheat = Wheat()

    wheat.make_food(storage)

    assert storage.sushi == 0
    assert storage.bread == 1
    assert storage.popcorn == 0

    print("Wheat food test passed")


def test_corn_food():
    storage = FoodStorage()
    corn = Corn()

    corn.make_food(storage)

    assert storage.sushi == 0
    assert storage.bread == 0
    assert storage.popcorn == 1

    print("Corn food test passed")


def test_rice_drought():
    rice = Rice()

    rice.quality = 100

    drought = Disaster("Drought")

    rice.handle_disaster(drought)

    assert rice.quality == 70

    print("Rice drought test passed")


def test_wheat_drought():
    wheat = Wheat()

    wheat.quality = 100

    drought = Disaster("Drought")

    wheat.handle_disaster(drought)

    assert wheat.quality == 90

    print("Wheat drought test passed")


def test_corn_storm():
    corn = Corn()

    corn.quality = 100

    storm = Disaster("Storm")

    corn.handle_disaster(storm)

    assert corn.quality == 95

    print("Corn storm test passed")


def test_farm_storage():
    farm = Farm()

    farm.add_crop(Rice())
    farm.add_crop(Wheat())

    assert len(farm.crops) == 2

    print("Farm storage test passed")


def test_polymorphic_food_creation():
    storage = FoodStorage()

    crops = [
        Rice(),
        Wheat(),
        Corn()
    ]

    for crop in crops:
        crop.make_food(storage)

    assert storage.sushi == 1
    assert storage.bread == 1
    assert storage.popcorn == 1

    print("Polymorphism test passed")


def run_tests():
    print("\n=========================")
    print("RUNNING TESTS")
    print("=========================\n")

    test_rice_food()
    test_wheat_food()
    test_corn_food()

    test_rice_drought()
    test_wheat_drought()
    test_corn_storm()

    test_farm_storage()

    test_polymorphic_food_creation()

    print("\n=========================")
    print("ALL TESTS PASSED")
    print("=========================\n")

run_tests()

farm = Farm()
storage = FoodStorage()

while True:
    print("\n=== GRAIN GAME ===")
    print("1 - Grow crops")
    print("2 - Make food")
    print("3 - Show food storage")
    print("4 - Exit")

    choice = input("Choice: ")

    if choice == "1":

        while True:
            print("\nChoose grain:")
            print("1 - Rice")
            print("2 - Wheat")
            print("3 - Corn")
            print("4 - Back")

            grain_choice = input("Choice: ")

            if grain_choice == "1":
                crop = Rice()

            elif grain_choice == "2":
                crop = Wheat()

            elif grain_choice == "3":
                crop = Corn()

            elif grain_choice == "4":
                break

            else:
                print("Invalid choice.")
                continue

            if crop.grow():
                random_disaster(crop)

                if crop.quality >= 70:
                    crop.harvest()
                    farm.add_crop(crop)
                else:
                    print("Crop quality became too low after the disaster.")

    elif choice == "2":
        farm.make_food(storage)

    elif choice == "3":
        storage.show()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")