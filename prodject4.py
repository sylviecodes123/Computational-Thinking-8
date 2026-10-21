for i in range(10):
        #Lines  4 to 66 are contained in the loop

        answer1 = input("Hi would you like me to style you today?!")
        if answer1 == "Yes":
            print("Yay lets get started!")
        elif answer1 == "No":
            print("well you have nothing to wear so im going to anyways...")

        answer2 = input("Do you want to wear a Tank top, Long sleeve, or T-shirt")
        if answer2 == "Long sleeve":
            print("good choice")
            answer3 = input("Which color Black, White, Red, or Blue?")
            print("That is definetly your color!")
        elif answer2 == "Tank top":
            answer2 = input("Which color Black, White, Red, or Blue?")
            print("That is definetly your color!")
        if answer2 == "T-shirt":
            print("good choice")
            answer3 = input("Which color Black, White, Red, or Blue?")
            print("That is definetly your color!")

        print("Ok now lets pick your bottoms")
        answer3 = input("Do you want to wear a Pants, Shorts, or a Skirt")
        if answer3 == "Pants":
            print("ooh i like")
            answer4 = input("Which style, Jeans, Sweats, or Leggings?")
            print("you are very fashionable!")
        elif answer3 == "Shorts":
            answer3 = input("Which style jean Shorts, Sweat shorts, or Aethletic shorts")
            print("You are very fashionable!")
        if answer3 == "Skirt":
            print("ooh i like")
            answer4 = input("Which style, Flowy, Long, or Short")
            print("You are very fashionable!")

        print("Time for shoes")
        answer4 = input("Do you want to wear a Sneakers, Sandals, or a Boots")
        if answer4 == "Sneakers":
            print("i love that")
            answer5 = input("Would you like to wear jordans, nike, or addidas?")
            print("interesting!")
        elif answer4 == "Sandals":
            answer4 = input("would you like to wear birks, havanas, or crocs")
            print("i love that!")
        if answer4 == "Boots":
            print("i love that")
            answer5 = input("would you like to wear Brown, White, or Black boots?")
            print("You are very fashionable!")

        print("Lastly lets do accesories")
        answer5 = input("Do you want to wear a Jewerly, Purse, or Belt ")
        if answer5 == "Jewelry":
            print("very stylish")
            answer6 = input("Would you like to wear a Braclet, Necklace, or Earrings?")
            print("cute!")
        elif answer5 == "Purse":
            answer5 = input("would you like to wear Gucci, Louis v, or Chanel")
            print("fancy!")
        if answer5 == "Belt":
            print("very stylish!")
            answer6 = input("would you like to wear a Brown, White, or Black belt?")
            print("good choice!")
        print("ok your all done i LOVE your outfit! have a nice day!!")

        print("next day...")







