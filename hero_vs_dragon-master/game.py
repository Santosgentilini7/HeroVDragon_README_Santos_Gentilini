import random

# import random is a simple library that implements the random number generator behavior

# Please read into the variables below the correct numbers. Use try and except to catch error.
# a simple example would be:
# hero_hp = int(input("how many hp does the hero have?"))

response = input("Would you like to start a new game?\n")

while response != "no" or response != "yes":
    if response != "no":
        print("Welcome!")
        break
    if response != "yes":
        print("See you later!")
        exit()

Class = input("What is your class? You can choose Knight(1), Archer(2) or Wizard(3).\n")
if Class == "1":
    Weapon = "Sword"
    print("You shall wield a " + Weapon)
elif Class == "2":
    Weapon = "Bow"
    print("You shall wield a " + Weapon)
else:
    Weapon = "Wand"
    print("You shall wield a " + Weapon)

hero_hp = int(input("How much hp does the hero have?\n"))
dragon_hp = int(input("How much hp does the dragon have?\n"))
hero_max_dmg = 20
dragon_max_dmg = 10
health_potion = 1


hero_name = input("What shall the legends call you, brave hero?\n")

print("You venture deep into the caves which legends rumour to be swarmed in monsters, but you've only come for one. The vicious dragon terrorizing your village. Good luck hero")
print("The dragon with", dragon_hp, "hp attacks our hero with", hero_hp, "hp")

# add a While for an infinite block
while True:
    dragon_attack = random.randint(1, dragon_max_dmg)
    # here you need to update the hero hp, you need to subtract the damage that the dragon did
    hero_hp = hero_hp - dragon_attack


    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")
    if dragon_attack == dragon_max_dmg:
        print("CRITICAL HIT")
    # add an if condition to check if the hero was killed by the dragon
    if hero_hp <= 0:
        print("Unfortunately the dragon killed our hero. RIP sir", hero_name)



    hero_attack = random.randint(1, hero_max_dmg)
    # here you need to update the dragon hp, you need to subtract the damage that the hero did
    dragon_hp = dragon_hp - hero_attack
    if hero_hp < 10:
        hero_attack = random.randint(10, hero_max_dmg)
        print("Hero! Your health is low! NEAR DEATH BONUS")

    attack = input("Will you attack or use a potion?\n")
    if attack == "attack":
            print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")
            if hero_attack == hero_max_dmg:
                print("CRITICAL HIT")
    # add an if condition to check if the dragon was killed by the hero
            if dragon_hp <= 0:
                print("Our valiant hero", hero_name, "has slain the dragon!")
                break
    elif attack == "potion":
            if health_potion > 0:
                hero_hp = hero_hp + 10
                print("No potions left.")
            else:
                print("You don't have any potions. You wasted your turn.")




input("Round over. Press any key")
