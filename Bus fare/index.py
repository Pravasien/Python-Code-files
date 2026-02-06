class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity
    def fare(self):
        return self.seating_capacity * 100
class Bus(Vehicle):
    def fare(self):
        return self.seating_capacity * 100 * 1.1
school_bus = Bus("School Bus", 50)
print("Name:", school_bus.name, "Capacity:", school_bus.seating_capacity, "Fare:", school_bus.fare())