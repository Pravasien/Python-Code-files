def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city=="Banglore":
        return 750
    elif city=="Chennai":
        return 300
    elif city=="Hyderabad":
        return 450
    elif city=="Dheli":
        return 650
def rental_car_cost(days):
    if days>=7:
        return days*40-30
    elif days>=3:
        return days*40-15
    else:
        return days*40
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
print("cost of car rental for 5 days:",rental_car_cost(5))
print("cost of plane ride to Banglore:",plane_ride_cost("Banglore"))
print("cost of hotel for 5 nights:",hotel_cost(5))
print(trip_cost("Banglore",5,600))