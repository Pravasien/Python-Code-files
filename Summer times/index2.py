User_season = input("Enter the season (summer, winter, spring, autumn): ")
season=User_season.lower()

if season=="winter":
    print("Wear a coat.")
elif season=="autumn":
    print("Wear a sweater.")
elif season=="spring":
    print("Wear light clothes.")
elif season=="summer":
    print("Wear very light and comfortable clothes.")
else:
    print("Invalid season entered. Please enter summer, winter, spring, or autumn.")