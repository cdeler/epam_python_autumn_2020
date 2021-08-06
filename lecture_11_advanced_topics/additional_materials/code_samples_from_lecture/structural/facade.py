import time


class WaterBoiler:
    def __init__(self):
        self.temperature = 0
    
    def boil(self):
        print("Boiling the cold water")
        while self.temperature < 100:
            self.temperature += 10
            time.sleep(0.1)
        print("Hot water is ready!")
        return True


class CoffeeGrinder:
    def grind(self):
        print("Grinding fresh beans...Done!")
        return

class WaterProcessor:
    def __init__(self):
        self.input_tank_level = 100
    
    def process_hot_water(self):
        print("Run hot water through blended coffee...")
        while self.input_tank_level > 0:
            self.input_tank_level -= 10
            time.sleep(0.1)
        print("Coffee is Ready")
        return True


class CoffeeMaker:
    def __init__(self):
        self.boiler = WaterBoiler()
        self.water_proc = WaterProcessor()
        self.grinder = CoffeeGrinder()

    def make(self):
        self.boiler.boil()
        self.grinder.grind()
        self.water_proc.process_hot_water()
        print("Done!")

if __name__ == "__main__":
    CoffeeMaker().make()