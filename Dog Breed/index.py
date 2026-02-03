class Dogs:
    def __init__(self,colour,breed):
        self.colour = colour
        self.breed = breed
dog1 = Dogs("Brown", "Labrador")
dog2 = Dogs("Golden", "Golden Retriever")
print("Dog 1: ", dog1.colour,dog1.breed)
print("Dog 2: ", dog2.colour,dog2.breed)