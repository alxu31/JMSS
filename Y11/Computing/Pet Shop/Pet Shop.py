#Imports external modules
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#Class for shop's inventory database
class ShopInventory:
    def __init__(self):
        self.inventory = list()
    #Prints current inventory list
    def inventoryList(self):
        inventoryNames = []
        for pet in self.inventory:
            inventoryNames.append(pet.name)
        print("Inventory: ",end = "")
        print(", ".join(inventoryNames))
    #Adds an animal to the inventory
    def add(self, animal):
        self.animal = animal
        self.inventory.append(self.animal)
    def remove(self, animal):
        self.animal = animal
        self.inventory.remove(self.animal)
    #Runs the pet shop for a month
    def runMonth(self,monthNum):
        shopSold.networth-=1000
        changes=[]
        #Pets have a certain chance to be bought
        customers = random.randint(500,1500)
        for i in range(customers):
            for pet in self.inventory:
                if random.randint(1,pet.chance) == 1:
                    shopInventory.remove(pet)
                    shopSold.add(pet)
                    changes.append(pet.name)
                    shopSold.networth += int((7/5)*pet.cost)
                    petNames.remove(pet.name)
        #Adds networth at that time to the list of values
        x.append(totalMonths)
        y.append(shopSold.networth)
        #Prints changes that occured during that month
        print(f"Changes (M{monthNum}): ",end = "")
        print(", ".join(changes))


#Class for shop's sold database
class ShopSold:
    def __init__(self,originalNetworth):
        self.sold = list()
        self.networth = originalNetworth
    #Prints list of all sold animals
    def soldList(self):
        sold = []
        for pet in self.sold:
            sold.append(pet.name)
        print("Sold: ",end = "")
        print(", ".join(sold))
    #Adds an animal to the sold list
    def add(self, animal):
        self.animal = animal
        self.sold.append(self.animal)
    #Plots a graph of networth($) vs time(no. months)
    def plot(self):
        fig, ax = plt.subplots()
        ax.scatter(x,y)
        #Sets tick frequency to 1 for x axis and 1000 for y axis
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1000))
        #Sets starting values of axes to 0
        ax.set_ylim(ymin=0)
        ax.set_xlim(xmin=0)
        plt.show()
        
#Class for animals
class Animal:
    def __init__(self,name,species,cost):
        self.name = name
        self.species = species
        self.cost = cost
        self.allSpecies = ["Bird","Cat","Dog","Fish","Lizard","Rabbit","Hamster"]
        #Randomly generates number for the animal's attributes, depending on that attributes impact
        #(lower numbers mean the animal is more desirable)
        self.noise = random.randint(2,7)
        self.size = random.randint(1,5)
        self.nocolour = random.randint(1,5)
        self.aggression = random.randint(4,8)
        self.notexture = random.randint(2,6)
        self.birdAttributes = [self.noise,self.size,self.nocolour]
        self.cat_dogAttributes = [self.noise,self.size,self.aggression]
        self.rabbit_hamsterAttributes = [self.size,self.aggression,self.notexture]
        self.lizardAttributes = [self.size,self.aggression,self.notexture]
        self.fishAttributes = [self.size,self.nocolour,self.aggression]
        
        self.totalValue = 0
        self.chance = 0
        
        #Sets the animal's attributes to a list of random numbers for each attribute of that species
        if self.species == self.allSpecies[0]:
            self.attributes = self.birdAttributes
        elif self.species == self.allSpecies[1] or self.species == self.allSpecies[2]:
            self.attributes = self.cat_dogAttributes
        elif self.species == self.allSpecies[5] or self.species == self.allSpecies[6]:
            self.attributes = self.rabbit_hamsterAttributes
        elif self.species == self.allSpecies[3]:
            self.attributes = self.fishAttributes
        elif self.species == self.allSpecies[4]:
            self.attributes = self.lizardAttributes
        #Adds up the value of all attributes
        for num in self.attributes:
            self.totalValue += num
        chance = 0
        #Determines chance of the animal being bought (1/...)
        if self.totalValue <= 8:
            self.chance = 1000
        elif self.totalValue <= 11:
            self.chance = 1400
        elif self.totalValue <= 14:
            self.chance = 1800
        elif self.totalValue <= 17:
            self.chance = 2200
        else:
            self.chance = 2600

#Sets starting values
originalNetworth = 10000
#Lists for points on networth graph
x=[0]
y=[originalNetworth]
totalMonths = 0
shopInventory = ShopInventory()
shopSold = ShopSold(originalNetworth)
count = 0
allPets={}
petNames=[]
fullBreak=False

while True:
    while True:
        #Ends program if networth becomes negative            
        if shopSold.networth < 0:
            print("Your shop went bankrupt.")
            fullBreak=True
            break
        print(f"Networth: {shopSold.networth}")
        #Asks user if they want to buy more pets
        yesno=input("Buy More? (y/n): ")
        #If the user wants to buy a pet, they decide the name and species
        if yesno=="y":
            while True:
                name=input("Name: ")
                if name in petNames:
                    print("Already used that name. Choose another.")
                else:
                    break
            while True:
                species=input("Species(Bird,Cat,Dog,Fish,Lizard,Rabbit,Hamster): ")
                if species not in ["Bird","Cat","Dog","Fish","Lizard","Rabbit","Hamster"]:
                    print("That is not an option. Choose another species.")
                else:
                    break
        else:
            break
        #Animal is created with a random cost
        allPets[name]=Animal(name,species,random.randint(500,3000))
        print(allPets[name])
        #Tells user the cost and chance of the animal being bought
        print(f"Cost: {allPets[name].cost}, Chance: 1/{allPets[name].chance}")
        #User can accept or decline the animal (if they decline it still costs some money)
        acceptdecline=input("Accept or decline (a/d): ")
        #If the user accepts the animal, it is added to the inventory
        if acceptdecline == "a":
            shopInventory.add(allPets[name])
            shopSold.networth-=allPets[name].cost
            petNames.append(name)
        #Otherwise some money is deducted from the networth
        else:
            subtracted=int((1/random.randint(50,100))*allPets[name].cost)
            shopSold.networth-=subtracted
            print(f"Subtracted ${subtracted} from income.")
    if fullBreak:
        break
    monthCount = int(input("How many months?: "))
    
    
    #Runs the shop for k months
    for k in range(monthCount):
        totalMonths += 1
        shopInventory.runMonth(k+1)
    #Prints inventory and sold lists
    if len(shopInventory.inventory) > 0:
        shopInventory.inventoryList()
    if len(shopSold.sold) > 0:
        shopSold.soldList()
    #Plots networth graph
    shopSold.plot()
    
"""
Testing:
Jerry = Animal("Jerry","Bird",1300)
Barry = Animal("Barry","Dog",1300)
shopInventory.add(Jerry)
print(Jerry.cost)
print(Barry.chance)
shopInventory.inventory.remove(Barry)

print(shopSold.networth)
shopInventory.runMonth()

shopInventory.inventoryList()
shopSold.soldList()

x=[0,1,2,3,4]
y=[10000,9000,6000,8000,3000]

fig, ax = plt.subplots()
ax.scatter(x,y)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1000))
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)
plt.show()

"""










        
