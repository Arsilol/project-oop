class Grain:
    def     __init__(self, name, description, recommended_water):
        self.name = name
        self.description = description
        self.recommended_water = recommended_water
    
    def grow(self):
        print(f"\nGrowing {self.name}")
        print(f"Description: {self.description}")
        print(f"Recommended water: {self.recommended_water}%")

        water = int(input("Enter water percentage: "))

        quality = 100 - abs(self.recommended_water - water)

        if quality < 70:
            print(f"Quality: {quality}%")
            print("Quality too Low. Harvest failed.")
            return False
        
        print(f"Quality: {quality}%")
        return True
    
    def harvest(self):
        print(f"{self.name} harvested successfully!")
    
    def make_food(self):
        pass

class Rice(Grain):
    def __init__(self):
        super().__init__(
            "Rice",
            "Rice grows well in wet conditions.",
             70
        )
    def make_food(self):
        return "Sushi"
    
class Wheat(Grain):
    def __init__(self):
        super().__init__(
            "Wheat",
            "Wheat is a common grain used for bread.",
            40
        )
    def make_food(self):
        return "Bread"
    
class Corn(Grain):
    def __init__(self):
        super().__init__(
            "Corn",
            "Corn is a tall grain plant.",
            90
        )
    def make_food(self):
        return "Popcorn"

class Farm:
    def __init__(self):
        self.crops = []

        self.food = {
            "Sushi": 0,
            "Bread": 0,
            "Popcorn": 0
        }
    
    def add_crop(self, crop):
        self.crops.append(crop)
    
    def show_crops(self):
        if not self.crops:
            print("No crops available.")
            return
        
        print("\nAvailable Crops:")

        for i, crop in enumerate(self.crops, start=1):
            print(f"{i}. {crop.name}")

    def make_food(self):
        if not self.crops:
            print("No crops available to make food.")
            return
        self.show_crops()

        choice = int(input("Select a crop to make food (enter number): "))
        
        if 1 <= choice <= len(self.crops):
            selected_crop = self.crops.pop(choice - 1)
            food_item = selected_crop.make_food()
            self.food[food_item] += 1
            print(f"{food_item} made successfully!")
        else:
            print("Invalid choice. Please select a valid crop number.")
    def show_food_storage(self):
        print("\nFood Inventory:")
        has_food = False

        for food, amount in self.food.items():
            if amount > 0:
                print(f"{food}: {amount}")
                has_food = True
            if not has_food:
                print("No food items available.")

            
farm = Farm()

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
                crop.harvest()
                farm.add_crop(crop)

    elif choice == "2":
        farm.make_food()

    elif choice == "3":
        farm.show_food_storage()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

    