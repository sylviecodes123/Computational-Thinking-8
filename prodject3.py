print("Hello!! i am going to be telling you what genre you like most! lets get started")
print("")
rap_points=0
pop_points=0
house_points=0
country_points=0

answer1 = input("Do you like A fast or B slow music")
if answer1 == "A" or answer1 == "a":
    rap_points += 2
    pop_points += 1
    house_points += 1

elif answer1 == "B":
    country_points += 2

print("")

answer2 = input("Do you prefer A Drake, B Sabrina carpentar, C John summit, or D Tyler childers")
if answer2 == "A":
    rap_points +=1
elif answer2 == "B":
    pop_points +=1
elif answer2 == "C":
    house_points +=1
elif answer2 == "D":
    country_points +=1

print("Choose a color out of these 4")
answer3=input("A pink, B teal, C blue, D yellow")
if answer3 == "A":
    pop_points +=1
elif answer3 == "B":
    rap_points +=1
elif answer3 == "C":
    country_points +=1
elif answer3 == "D":
    house_points +=1

answer4 = input("Do you prefer A Winter, B Spring, C Summer, or D Fall")
if answer4 == "A":
    rap_points +=1
elif answer4 == "B":
    pop_points +=1
elif answer4 == "C":
    house_points +=1
elif answer4 == "D":
    country_points +=1
     
print("Choose a person out of these 4")
answer5=input("A Sylvie, B Joseph, C Gavin, D Neriah")
if answer5 == "A":
    house_points += 1
elif answer5 == "B":
    rap_points +=1
elif answer5 == "C":
    country_points +=1
elif answer5 == "D":
    pop_points +=1


if house_points > pop_points and house_points > country_points and house_points > rap_points:
    #You get this ending if you choose the most for house
    print ("Your favorite genre is house!! lets go party!")
if pop_points > house_points and pop_points > rap_points and pop_points > country_points:
    #you get this ending by answering pop the most
    print ("Your favprote genre is Pop!!")
if country_points > pop_points and country_points > rap_points and country_points > house_points:
    #you get this ending by answering country the most
    print ("Your favorite genre is country!! go get your boots on!")
if rap_points > pop_points and rap_points > country_points and rap_points > house_points:
    #you get this ending by answering rap the most
    print ("Your favorite genre is rap!! yeet, skrtt!")
