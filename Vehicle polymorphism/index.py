class Ferrari:
    def mileage(self):
        print("Ferrari mileage is 9km")
    def top_speed(self):
        print("Ferrari top speed is 210kmph")
    def seat_capacity(Self):
        print("Ferrari sea capacity is 2")
class BMW:
    def mileage(self):
        print("BMW mileage is 10km")
    def top_speed(self):
        print("BMW top speed is 208kmph")
    def seat_capacity(Self):
        print("BMW sea capacity is 3")
obj_ferrari = Ferrari()
obj_bmw = BMW()
for vehicle in (obj_ferrari, obj_bmw):
    vehicle.mileage()
    vehicle.top_speed()
    vehicle.seat_capacity()