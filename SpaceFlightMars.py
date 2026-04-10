import time
import random
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
time.sleep(1)
print("Parrot games")
print("  ______      ")
time.sleep(0.5)
print("/ =    = \    ")
time.sleep(0.5)
print("| |    | |-\  ")
time.sleep(0.5)
print("| |    | |--| ")
time.sleep(0.5)
print("| |    | |-/  ")
time.sleep(0.5)
print("\________/    ")
time.sleep(3)
print("                ")
time.sleep(2)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("      Space Flight Mars    ")
print("")
print(" Copyright 2023 Parrot Games")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(3)
str(input("Press Enter to Start Your Flight"))
time.sleep(2)
print("Note: the game will look better in fullscreen")
code = str(input("Please enter a code in order to contune"))
print("Welcome to Space Flight Mars")
time.sleep(1)
print("The interactive space-RPG game!")
time.sleep(0.5)
print("Building spacecraft")
time.sleep(2)
print("Gathering samples")
time.sleep(2)
print("Training crew")
time.sleep(1)
day = 0 + 375  
fuel = 100
bad = 0
damage = 200
name = str(input("Enter your name"))
cap = (f"Misson Commader {name}")
n = str(input("Enter another name"))
name2 = (f"Mars Module ploit {n}")
n1 = str(input("Enter another name"))
name3 = (f"Commad ploit {n1}")
n2 = str(input("Enter another name"))
name4 = (f"Engineer {n2}")
n3 = str(input("Enter another name"))
name5 = (f"Civlain {n3}")
crew = (f"{cap}, {name2}, {name3}, {name4} and {name5}")
time.sleep(1)
print(f"you mission starts now, {cap}")
time.sleep(1)
time.sleep(1)
print("Your rocket is now ready")
time.sleep(1)
flight = str(input("Name your space flight"))
ship = str(input("Name your boat"))
print("You are with four other astronauts")
time.sleep(1)
print("This is a map of your mission")
print(f"                                          Flight map of {flight} misson					        ")
print("											                                ")
print("        ______________            /-------------------------------------------------------------------------\	")
print("       /     o        \          /          (||)  moon                                           /-----\     \  	")
print("       |{  }        ^(|         /                                                                |     |     /	")
print("       | {   }    X------------/                                                            mars \-----/    /	")
print("       |   {O    ^{  \|       /                                                                            /	")
print("       |     \  ------------------------------------------------------------------------------------------/      ")
print("       |     \\    \|)| earth								                        ")
print(f"       \_____________/                                                      O = Current location of the {flight}")
print("                                                                                    X = Estimated touchdown point")
print("                                                                                    - = Flight path		")
time.sleep(5)
print("Can i get a go or no go")
time.sleep(0.5)
print("CAPCOM")
time.sleep(0.5)
print("go")
time.sleep(0.5)
print("FDO")
time.sleep(0.5)
print("go")
time.sleep(0.5)
print("GPO")
time.sleep(0.5)
print("go")
time.sleep(0.5)
print("Booster")
time.sleep(0.5)
print("go")
time.sleep(0.5)
print("EECOM")
time.sleep(0.5)
print("go")
time.sleep(0.5)
print("INCO")
time.sleep(0.5)
print("go")
time.sleep(0.5)
print("MMACS")
time.sleep(0.5)
print("go")
time.sleep(0.5)
print("FLIGHT")
time.sleep(0.5)
print("go")
time.sleep(1)
print(f"{flight} crew")
time.sleep(2)
print("go")
time.sleep(3)
print("Godspeed")
time.sleep(5)
username = str(input("Enter Lauch code here"))
time.sleep(1)
while username != (code):
    pass
    print("Incorrect Lauch code")
    time.sleep(1)
    username = str(input("Re-enter lauch code"))
if username == ("code"):
    pass
print("We are go for launch in t-minus")
print("10")
time.sleep(1)
print("9")
time.sleep(1)
print("8")
time.sleep(1)
print("7")
time.sleep(0.8)
print("Main engine start")
time.sleep(0.2)
print("6")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(0.2)
print("Ignition")
time.sleep(0.8)
print("1")
time.sleep(1)
print("Liftoff")
fuel = fuel - 9
time.sleep(1)
print(f"And we have liftoff of the {flight} misson")
time.sleep(3)
print("Pressure looks stable")
time.sleep(4)
print(f"Houston to {flight}, you are now exiting the earth's atmosphere")
time.sleep(2)
print("Do you use fuel to accelerate or do you not?")
launch = str(input("yes or no"))
time.sleep(2)
if launch == ("yes"):
    pass
    print("You choose to use fuel")
    fuel = fuel - 3
    time.sleep(1)
    print(f"Houston to {flight}, we are now using fuel to get to Mars faster")
    time.sleep(1)
    print("You will get to Mars a few days faster")
if launch == ("no"):
    pass
    print("You choose to save fuel")
    time.sleep(1)
    print(f"Houston to {flight}, we will save fuel")
    print("The cost is a few extra days")
    time.sleep(1)
    print(f"{name3} holds off on the fuel")
    day = day + 3
time.sleep(3)
print(f"Houston to {flight}, You are now on line with the flight path")
time.sleep(2)
print(f"Houston to {flight}, Please copy")
time.sleep(1)
print("What do you want to say?")
houston = str(input("Enter here"))
time.sleep(0.5)
houstonfeed = (f"{flight} to Houston, {houston}")
print(houstonfeed)
time.sleep(1)
print(f"Houston to {flight}, thank you for advising")
time.sleep(3)
print("You are on track to mars")
time.sleep(1)
print(f"Houston to {flight}, please give a go or no go for stopping at the ISS")
print("You are now heading towards the ISS")
print("yes or no")
space2 = str(input("Enter input here"))
if space2 == ("yes"):
    pass
    day = day + 1
    print("You choose to stop at the ISS")
    time.sleep(1)
    print(f"Houston to {flight}, where are now docking")
    time.sleep(1)
    print("You board the ISS")
    day = day + 3
    print(f"{cap}, {name2}, {name3}, {name4}, and {name5} are now resting")
    time.sleep(3)
    print("Your crew is now rested")
if space2 == ("no"):
    pass
    print(f"Houston to {flight}, we will keep going")
print("You are now on your way to Mars")
time.sleep(1)
print("You are now out of Earth orbit")
time.sleep(1)
print("It will take less time to get to Mars")
time.sleep(1)
day = day + 1
fuel = fuel - 3
print("You will need to follow certain directions in order to succeed")
time.sleep(3)
print("Warning")
time.sleep(0.5)
print("Warning")
time.sleep(0.5)
print(f"Collision up ahead, 27 degrees, mass unknown, {name3} takes over")
time.sleep(2)
print("Warning")
time.sleep(0.5)
print(f"Collison, {cap}, where've hit something")
time.sleep(2)
print("Warning")
time.sleep(1)
print(f"Hydrogen leak in tank2, {name3} calculates quickly")
time.sleep(2)
print(f"{name3} finds out that the only way to fix it is to do a spacewalk.")
time.sleep(2)
print("Select who you want to go out")
time.sleep(1)
print(f"1= {cap} 2= {name2} 3= {name3} 4= {name4} 5= {name5}")
space = int(input("Enter Input Here"))
if space == ("1"):
    pass
    space3 = (cap)
if space == ("2"):
    pass
    spac3 = (name2)
if space == ("3"):
    pass
    space3 = (name3)
if space == ("4"):
    pass
    space3 = (name4)
if space == ("5"):
    pass
    space3 = (name5)
    time.sleep(1)
    print(f"{space3} prepares for the spacewalk")
time.sleep(1)
print("In order to succeed, you will need to enter certain commands as fast as possible")
input("Press Enter to start")
start_time = time.time()
print("1= left 2=stay 3= right")
time.sleep(1)
print("Go left")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go right")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("3"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go left")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Stay")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("2"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go right")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("3"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10
    
print("Go left")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go right")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("3"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Stay")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("2"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go left")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go right")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("3"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10
time.sleep(0.5)
print("Now, complete these tasks")
time.sleep(1)
print("1= turn 2= hammer 3= twist 4=close")
time.sleep(5)
print("Turn")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 12

print("Turn")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 12

print("Twist")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("3"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 12

print("Turn")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 12

print("Hammer")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("2"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 12
    
print("Twist")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("3"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 12

print("Close")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("4"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 12
print("Now it's time to go back")
time.sleep(1)
print("You have completed the tasks, now go back!!!")
print("Go left")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go right")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("3"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10
print("Go left")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Stay")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("2"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go right")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("3"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go left")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go right")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("3"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Stay")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("2"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go left")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("1"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10

print("Go right")
time.sleep(0.5)
walk = str(input("Enter Here"))
time.sleep(1)
if walk == ("3"):
    pass
    print("Correct!")
    time.sleep(1)
else:
    pass
    print("Incorrect")
    time.sleep(1)
    fuel = fuel - 2
    bad = bad + 1
    damage = damage - 10
print(f"Good job, you successfully completed the mission")
time.sleep(1)
input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
day = day + 2
time.sleep(1)
print("Now that you ship is fixed, you will continue on your mission")
time.sleep(3)
print("You are now entering Mars orbit")
time.sleep(1)
print(f"{cap} takes charge")
time.sleep(3)
print("We have now begun the seven minutes of terror")
str(input("Press Enter to Begin"))
time.sleep(1)
print("Heat Shield activated")
time.sleep(1)
print("10000 feet")
str(input("Press enter to deploy parucute"))
time.sleep(0.5)
print("Deploying parucute")
time.sleep(1)
print("Were approcing 7000 feet")
time.sleep(1)
print("6000 feet")
time.sleep(1)
print("5000 feet")
time.sleep(1)
print("4000 feet")
time.sleep(1)
print("3000 feet")
time.sleep(1)
print("2000 feet")
time.sleep(1)
print("1000 feet")
print("Thusters Engaged")
time.sleep(1)
print("700 feet")
time.sleep(1)
print("500 feet")
time.sleep(1)
print("200 feet")
time.sleep(1)
print("100 feet")
time.sleep(1)
print("50 feet")
time.sleep(1)
print("25 feet")
time.sleep(5)
print(f"Touchtown of the {flight} misson!")
time.sleep(1)
print(f"                                          Flight map of {flight} misson					        ")
print("											                                ")
print("        ______________            /-------------------------------------------------------------------------\	")
print("       /     o        \          /          (||)  moon                                           /-----\     \  	")
print("       |{  }        ^(|         /                                                                |   O |     /	")
print("       | {   }    X------------/                                                            mars \-----/    /	")
print("       |   {     ^{  \|       /                                                                            /	")
print("       |     \  ------------------------------------------------------------------------------------------/      ")
print("       |     \\    \|)| earth								                        ")
print(f"       \_____________/                                                      O = Current location of the {flight}")
print("                                                                                    X = Estimated touchdown point")
print("                                                                                    - = Flight path		")     
time.sleep(1)
feed = str(input("What do you want to say"))
print(f"{flight} to Houston, {feed}")
time.sleep(1)
print(f"Houston to {flight}, thank you for advising")
time.sleep(1)
print("you get your space suit on")
time.sleep(4)
print("One small step for man, one giant leap for mankind")
time.sleep(5)
print("you step back into the rocket")
print(f"{name4} gives you basic stats")
time.sleep(1)
print(f" you have {fuel}% left of your fuel")
print(f" you have taken {day} days to get to Mars")
time.sleep(1)
str(input("Press enter to launch"))
print("Houston, We are go for  Mars launch in t-minus")
print("10")
time.sleep(1)
print("9")
time.sleep(1)
print("8")
time.sleep(1)
print("7")
time.sleep(0.8)
print("Main engine start")
time.sleep(0.2)
print("6")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(0.2)
print("Ignition")
time.sleep(0.8)
print("1")
time.sleep(1)
print("Liftoff")
fuel = fuel - 1
time.sleep(1)
print(f"And we have liftoff of the {flight} mission, again")
time.sleep(5)
day = day + 175
fuel = fuel - 25
print(f"Enter yes or no if the number is above zero: {fuel}")
fuel_dec = str(input("Enter input here (only yes or no)"))
time.sleep(1)
print(f"Enter yes or no if the number is above zero: {damage}")
damage_dec = str(input("Enter input here (only yes or no)"))
if day == ("no"):
    print("Game Over")
    time.sleep(1)
    print("you ran out of fuel and got lost")
    print(f"Astronauts {cap}, {name2}, {name3}, {name4}, {name5} are lost after {flight} mission")
    time.sleep(1)
    print(f"Breaking news: Astronauts {cap}, {name2}, {name3}, {name4}, {name5} are lost after {flight} misson due to lack of fuel")
    time.sleep(2)
    print("The first people on Mars...")
    time.sleep(3)
    print("Grapics by Callum Chang")
    time.sleep(1)
    print("Programing by Callum Chang")
    time.sleep(1)
    print("Facts and Info from nasa.gov")
    time.sleep(0.5)
    print("Made for the Game Design merit badge")
if fuel_dec == ("0"):
    print("Game Over")
    time.sleep(1)
    print("you ran out of fuel and got lost")
    print(f"Astronauts {cap}, {name2}, {name3}, {name4}, {name5} are lost after {flight} mission")
    time.sleep(1)
    print(f"Breaking news: Astronauts {cap}, {name2}, {name3}, {name4}, {name5} are lost after {flight} misson due to severe damage")
    time.sleep(2)
    print("The first people on Mars...")
    time.sleep(3)
    print("Grapics by Callum Chang")
    time.sleep(1)
    print("Programing by Callum Chang")
    time.sleep(1)
    print("Facts and Info from nasa.gov")
    time.sleep(0.5)
    print("Made for the Game Design merit badge")
if fuel_dec or damage_dec == ("yes"):
    pass
    print("You are now near earth")
    print(f"{name5} takes over")
    print("You are now just about near the blackout zone")
    time.sleep(1)
    print("We expect----------------")
    print("-------------------------")
    print("-------------------------")
    print("-------------------------")
    print("-------------------------")
    print("-------------------------")
    print("-------------------------")
    print("You are in the blackout zone")
    time.sleep(1)
    print("You have no choice but to wait")
    time.sleep(1)
    print("Deploying heat sleid")
    time.sleep(1)
    print("10000 feet")
    time.sleep(1)
    print("80000 feet")
    time.sleep(1)
    print("60000 feet")
    time.sleep(0.5)
    print("Deploing parichute")
    time.sleep(0.5)
    print("4000 feet")
    time.sleep(1)
    print("3000 feet")
    time.sleep(1)
    print("2500 feet")
    time.sleep(1)
    print("2000 feet")
    time.sleep(0.5)
    print("Buoy inflate")
    print("1000 feet")
    time.sleep(0.5)
    print("500 feet")
    time.sleep(1)
    print("250 feet")
    time.sleep(1)
    print("100 feet")
    time.sleep(1)
    print("50 feet")
    time.sleep(5)
    print("Water landing succsessfull")
    time.sleep(1)
    print(f"The {ship} has picked up our five astronauts.")
    time.sleep(4)
    print(f"Astronauts {cap}, {name2}, {name3}, {name4}, {name5} are safe after {flight} misson and are being sent back to parrotland")
    time.sleep(5)
    print(f"Your trip lasted {day} days and you had {fuel}% fuel left")
    time.sleep(1)
    print(f"Breaking news: Astronauts {cap}, {name2}, {name3}, {name4}, {name5} are safe after {flight} misson")
    time.sleep(2)
    print("The first people on Mars...")
    time.sleep(3)
    print("Grapics by Callum Chang")
    time.sleep(1)
    print("Programing by Callum Chang")
    time.sleep(1)
    print("Facts and Info from nasa.gov")
    time.sleep(0.5)
    print("Made for the Game Design merit badge")
    time.sleep(1)
    print("Thanks for playing!")
    time.sleep(1)
    print("Copyright 2023 parrot games")
    time.sleep(10)

