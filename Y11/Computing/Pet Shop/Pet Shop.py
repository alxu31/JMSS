import random

#write comments
#must have evidence u tested it (check rubric) (some examples, have some objects) or having a function that just adds, removes, prints stuff out etc
class Animal:
    def __init__(self,name,species,cost):
        self.name = name
        self.species = species
        self.cost = cost
        birthDate = name.Date
        allSpecies = ["Bird","Cat","Dog","Fish","Lizard","Rabbit","Hamster"]
        noise = random.randint(1,5)
        size = random.randint(1,5)
        colour = random.randint(1,5)
        agression = random.randint(1,5)
        texture = random.randint(1,5)
        birdAttributes = [noise,size,colour]
        cat_dogAttributes = [noise,size,aggression]
        rabbit_hamsterAttributes = [size,aggression,texture]
        lizardAttributes = [size,aggression,texture]
        fishAttributes = [size,colour,aggression]

        
        #if specific species, set attributes that are randomly picked
        if self.species == allSpecies[0]:
            totalValue = 0
            for num in birdAttributes():
                totalValue += num
        elif self.species == allSpecies[1] or self.species == allSpecies[2]:
            totalValue = 0
            for num in cat_dogAttributes():
                totalValue += num
        elif self.species == allSpecies[5] or self.species == allSpecies[6]:
            totalValue = 0
            for num in rabbit_hamsterAttributes():
                totalValue += num
        elif self.species == allSpecies[3]:
            totalValue = 0
            for num in fishAttributes():
                totalValue += num
        elif self.species == allSpecies[4]:
            totalValue = 0
            for num in lizardAttributes():
                totalValue += num
        chance = 0
        if totalValue >= 8 and totalValue <= 10:
            chance = 10
        if totalValue < 8 and totalValue >= 6 or totalValue > 10 and totalValue <= 12:
            chance = 15
        if totalValue < 6 or totalValue > 12:
            chance = 20
    def chance():
        return chance
    def print():
        pass
    def cost():
        return self.cost

class ShopDatabase:
    def __init__(self):
        ShopDatabase = []
        animalCount = 0
    def add(self,animal):
        ShopDatabase.append(animal)
    def remove(animal):
        ShopDatabase.remove(animal)
    def printAll():
        print(ShopDatabase)

class ShopSold:
    def __init__(self,originalNetworth):
        income = 0
        netWorth = originalNetworth + income
        animalsSold = []
    def income():
        print(self.income)
    def add(animal):
        self.animal = animal
        animalsSold.append(self.animal)
        income = animal.cost() + 0.1*animal.cost()
class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
        dob = [self.day,self.month,self.year]
    def print():
        print(f"{self.day}/{self.month}/{self.year}")


Difficulty = input("Difficulty(Easy,Medium,Hard): ")
shopDatabase = ShopDatabase()
if Difficulty == "Easy":
    originalNetworth = 50000
elif Difficulty == "Medium":
    originalNetworth = 25000
elif Difficulty == "Hard":
    originalNetworth = 10000

shopSold = ShopSold(originalNetworth)

while True:
    while True:
        animalAdd = input("Add (Bird, Cat, Dog, Fish, Lizard, Rabbit, Hamster, None) to shop: ")
        if animalAdd == "None":
            break
        else:
            animalName = input("Name: ")
            animalCost = random.randint(500,3000)
            print(f"The pet costed {animalCost}. This has been deducted from your networth.")
            animal = Animal(animalName,animalAdd,animalCost)
            shopDatabase.add(animal)

            YN = input("Would you like to buy anymore animals (Y/N)? ")
            if YN == "Y":
                pass
            elif YN == "N":
                break
    #possible number of customers per month
    customers = random.randint(500,1500)
    for i in range(customers):
        for item in shopDatabase():
             if random.randint(1,item.chance)==1:
                 shopDatabase.remove(item)
                 shopSold.add(item)
       
        
    
    
        
        
        




        

    
        
        
        
        




    













