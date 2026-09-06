class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        self.hunger -= 1
        print("{} has been fed.".format(self.name))
        print("{}'s hunger level: {}".format(self.name, self.hunger))
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        

# Create a pet
my_pet = Pet("Fluffy")
my_pet.feed()
my_pet.feed()
my_pet.feed()
# TODO: Feed the pet three times
