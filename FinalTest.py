

                                                                                        #Title: TRAVEL AGENT
                                                                                        #Name: SHRUTHI NATARAJAN

def domchosen():
    print("")
    budget = input("What is your budget, in USD, for your trip?: ")
    numslst = ["1","2","3","4","5","6","7","8","9","0"]
    finbudget = ""
    for i in budget:
        if i in numslst:
            finbudget+=i
    finbudget = int(finbudget)
    city = domfinal.var
    airfaredom = {'Los Angeles': 400 , 'Miami': 130 , 'Chicago': 210, 'Charleston': 180, 'Seattle': 540,'Houston': 360}
    staydompernight = {'Los Angeles': 230 , 'Miami': 150 , 'Chicago': 170, 'Charleston': 130, 'Seattle': 190,'Houston': 120}
    transporationdom = {'Los Angeles':  250, 'Miami': 190 , 'Chicago': 230, 'Charleston': 220, 'Seattle': 250,'Houston': 180}
    Los_Angeles = {"The Getty":0, "Griffith Observatory":0, "Los Angeles County Museum of Art": 25, "Universal Studios Hollywood":114, "The Broad":0, "Natural History Museum of Los Angeles County":15, "Petersen Automotive Museum":20, "Santa Monica Pier":0, "Hollywood Sign":0}
    Miami = {"Wynwood Walls":12, "Vizcaya Museum & Gardens":25, "Phillip & Patricia Frost Museum of Science":30, "Bayfront Park":0, "Everglades National Park":15, "Venetian Pool":16, "Fairchild Tropical Botanic Garden": 26, "Miami Zoo":23}
    Chicago = {"The Art Institute of Chicago":25, "Navy Pier":0, "Lincoln Park Zoo":0, "Millennium Park":0, "Shedd Aquarium":36, "360 Chicago":30, "Adler Planetarium":19, "Willis Tower":30, "Field Museum":28}
    Charleston = {"Rainbow Row":0, "The Battery":0, "Drayton Hall":28, "Fort Sumter National Monument":35, "Magnolia Plantation and Gardens":29, "The Charleston Museum":12, "Charleston City Market":0, "Joe Riley Waterfront Park":0}
    Seattle ={"Woodland Park Zoo":27, "Space Needle":33, "Seattle Aquarium":30, "Pike Place Market":0, "Seattle Art Museum":30, "The Seattle Great Wheel":17, "Museum of Pop Culture":25, "Washington Park Arboretum":0}
    Houston = {"Downtown Aquarium":25, "McGovern Centennial Gardens":0, "Space Center Houston":30, "The Museum of Fine Arts":19, "Houston Zoo":26, "Houston Museum of Natural Science":25, "The Galleria":0, "Children's Museum Houston":17}
    print("Now let's budget and plan your trip!")
    people = int(input("How many people, including youself, will be traveling?: "))
    if city == "Los Angeles":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfaredom['Los Angeles'], ", stay per night will be $",staydompernight['Los Angeles'], ", and a car rental for all 4 days will be $",transporationdom['Los Angeles'])
        finbudget = finbudget -(people*airfaredom['Los Angeles'])- staydompernight['Los Angeles']-transporationdom['Los Angeles']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    elif city == "Miami":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfaredom['Miami'], ", stay per night will be $",staydompernight['Miami'], ", and a car rental for all 4 days will be $",transporationdom['Miami'])
        finbudget = finbudget -(people*airfaredom['Miami'])- staydompernight['Miami']-transporationdom['Miami']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    elif city == "Chicago":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfaredom['Chicago'], ", stay per night will be $",staydompernight['Chicago'], ", and a car rental for all 4 days will be $",transporationdom['Chicago'])
        finbudget = finbudget -(people*airfaredom['Chicago'])- staydompernight['Chicago']-transporationdom['Chicago']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    elif city == "Charleston":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfaredom['Charleston'], ", stay per night will be $",staydompernight['Charleston'], ", and a car rental for all 4 days will be $",transporationdom['Charleston'])
        finbudget = finbudget -(people*airfaredom['Charleston'])- staydompernight['Charleston']-transporationdom['Charleston']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    elif city == "Seattle":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfaredom['Seattle'], ", stay per night will be $",staydompernight['Seattle'], ", and a car rental for all 4 days will be $",transporationdom['Seattle'])
        finbudget = finbudget -(people*airfaredom['Seattle'])- staydompernight['Seattle']-transporationdom['Seattle']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    elif city == "Houston":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfaredom['Houston'], ", stay per night will be $",staydompernight['Houston'], ", and a car rental for all 4 days will be $",transporationdom['Houston'])
        finbudget = finbudget -(people*airfaredom['Houston'])- staydompernight['Houston']-transporationdom['Houston']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    print("")
    if finbudget<=200:
        print("Oh no! It looks like you don't have much money left in your budget for tourist attractions, food, and daily spendings for the rest of the trip.")
        while True:
            try:
                retry = input("Would you like to re-enter a new budget? If so, please enter yes. Otherwise you could always come back another time to plan yout trip. Please enter no if you would like to come back another time: ")
                if retry == "YES" or retry == "Yes" or retry == "yes":
                    print("Great!")
                    break
                elif retry == "NO" or retry == "No" or retry == "no":
                    print("Thank you so much for coming in! We hope to see you again!")
                    return
                else:
                    print("Sorry, I didn't understand that")
            except:
                print("Sorry, I didn't understand that, please try again")
                pass
        domchosen()
    print("")
    print("Now is the fun part! Let's put together an itinerary for your trip.", city, "has a number of renowned tourist attractions.\nHere is a list of those attractions part of our travel package!")
    if city == "Los Angeles":
        places = ""
        for i, j in Los_Angeles.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Los_Angeles.items():
            print(i, "costs $",j)
    elif city == "Miami":
        places = ""
        for i, j in Miami.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Miami.items():
            print(i, "costs $",j)
    elif city == "Chicago":
        places = ""
        for i, j in Chicago.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Chicago.items():
            print(i, "costs $",j)
    elif city == "Charleston":
        places = ""
        for i, j in Charleston.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Charleston.items():
            print(i, "costs $",j)
    elif city == "Seattle":
        places = ""
        for i, j in Seattle.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Seattle.items():
            print(i, "costs $",j)
    elif city == "Houston":
        places = ""
        for i, j in Houston.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Houston.items():
            print(i, "costs $",j) 
    itinerary = {}
    print("")
    print("Please pick 2 places to visit each day to make the most our of your trip. You will see one in the morning and one in the afternoon.")
    print("Let's start with Day 1")
    while True:
        try:
            loc_1 = int(input("Please enter the number of the first location you would like to visit on Day 1, with 1 being the first location in the above list and 8 being the last: "))
            if loc_1 == 1 or loc_1 == 2 or loc_1 == 3 or loc_1 == 4 or loc_1 == 5 or loc_1 == 6 or loc_1 == 7 or loc_1 == 8:
                a = ((loc_1)-1)
                itinerary["Day 1 morning"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass                      
    while True:
        try:
            loc_2 = int(input("Please enter the number of the second location you would like to visit on Day 1, with 1 being the first location in the above list and 8 being the last: "))
            if loc_2 == 1 or loc_2 == 2 or loc_2 == 3 or loc_2 == 4 or loc_2 == 5 or loc_2 == 6 or loc_2 == 7 or loc_2 == 8:
                a = ((loc_2)-1)
                itinerary["Day 1 afternoon"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass                      
    print("Now let's plan Day 2")
    while True:
        try:
            loc_1 = int(input("Please enter the number of the first location you would like to visit on Day 2, with 1 being the first location in the above list and 8 being the last: "))
            if loc_1 == 1 or loc_1 == 2 or loc_1 == 3 or loc_1 == 4 or loc_1 == 5 or loc_1 == 6 or loc_1 == 7 or loc_1 == 8:
                a = ((loc_1)-1)
                itinerary["Day 2 morning"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass                      
    while True:
        try:
            loc_2 = int(input("Please enter the number of the second location you would like to visit on Day 2, with 1 being the first location in the above list and 8 being the last: "))
            if loc_2 == 1 or loc_2 == 2 or loc_2 == 3 or loc_2 == 4 or loc_2 == 5 or loc_2 == 6 or loc_2 == 7 or loc_2 == 8:
                a = ((loc_2)-1)
                itinerary["Day 2 afternoon"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass   
    print("Next up is Day 3")
    while True:
        try:
            loc_1 = int(input("Please enter the number of the first location you would like to visit on Day 3, with 1 being the first location in the above list and 8 being the last: "))
            if loc_1 == 1 or loc_1 == 2 or loc_1 == 3 or loc_1 == 4 or loc_1 == 5 or loc_1 == 6 or loc_1 == 7 or loc_1 == 8:
                a = ((loc_1)-1)
                itinerary["Day 3 morning"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass                      
    while True:
        try:
            loc_2 = int(input("Please enter the number of the second location you would like to visit on Day 3, with 1 being the first location in the above list and 8 being the last: "))
            if loc_2 == 1 or loc_2 == 2 or loc_2 == 3 or loc_2 == 4 or loc_2 == 5 or loc_2 == 6 or loc_2 == 7 or loc_2 == 8:
                a = ((loc_2)-1)
                itinerary["Day 3 afternoon"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass   
    print("Finally, let's plan Day 4")
    while True:
        try:
            loc_1 = int(input("Please enter the number of the first location you would like to visit on Day 4, with 1 being the first location in the above list and 8 being the last: "))
            if loc_1 == 1 or loc_1 == 2 or loc_1 == 3 or loc_1 == 4 or loc_1 == 5 or loc_1 == 6 or loc_1 == 7 or loc_1 == 8:
                a = ((loc_1)-1)
                itinerary["Day 4 morning"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("2Sorry, I didn't understand that, please try again")
            pass                      
    while True:
        try:
            loc_2 = int(input("Please enter the number of the second location you would like to visit on Day 4, with 1 being the first location in the above list and 8 being the last: "))
            if loc_2 == 1 or loc_2 == 2 or loc_2 == 3 or loc_2 == 4 or loc_2 == 5 or loc_2 == 6 or loc_2 == 7 or loc_2 == 8:
                a = ((loc_2)-1)
                itinerary["Day 4 afternoon"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass
    print("")
    print("Here is your final itinerary!")
    for i in itinerary:
        print(i, ":", itinerary[i])
    if city == "Los_Angeles":
        goodbye = "City of Angels!"
    elif city == "Miami":
        goodbye = "Magic City!"
    elif city == "Chicago":
        goodbye = "Windy City!"
    elif city == "Charleston":
        goodbye = "Holy City!"
    elif city == "Seattle":
        goodbye = "Emerald City!"
    elif city == "Houston":
        goodbye = "Bayou City!"
    print("")
    print("We are so happy that you have been able to successfully plan your trip with our travel agency! \nThank you so much for coming in! \nWe hope you enjoy your trip to the", goodbye, "Goodbye!")
    print("")  
    print("")
    print("")
    print("")
    print("")
    print("")
    while True:
        try:
            end = input("Please enter STOP if you would like to end the program and CONTINUE if you would like to exit: ")
            if end == "stop" or end == "STOP" or end == "Stop":
                quit()
            elif end == "CONTINUE" or end == "Continue" or end == "continue":
                begin()
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass

def intchosen():
    print("")
    budget = input("What is your budget, in USD, for your trip?: ")
    numslst = ["1","2","3","4","5","6","7","8","9","0"]
    finbudget = ""
    for i in budget:
        if i in numslst:
            finbudget+=i
    finbudget = int(finbudget)
    city = intfinal.var
    airfareint = {'Cairo': 1100, 'London': 900 , 'Rome': 1010, 'Havana': 750, 'Hanoi': 840, 'Budapest': 1230}
    stayintpernight = {'Cairo': 270, 'London': 190 , 'Rome': 210, 'Havana': 180, 'Hanoi': 160, 'Budapest': 160}
    transporationint = {'Cairo': 210, 'London': 250 , 'Rome': 240, 'Havana': 180, 'Hanoi': 160, 'Budapest': 200}
    Cairo = {"Cairo Tower":0, "The Egyptian Museum in Cairo":7, "Great Sphinx of Giza":8, "Giza Necropolis":0, "Prince Mohamed Ali Palace":4, "Museum of Islamic Art in Cairo":4, "Mosque of Muhammad Ali":4, "Al-Azhar Park":2}
    London = {"Buckingham Palace":42, "Tower of London":38, "London Eye":39, "Tower Bridge":16, "Westminster Abbey":44, "Natural History Museum":0, "Big Ben":0, "The Shard": 36}
    Rome = {"Colosseum":21, "Trevi Fountain":0, "Pantheon":0, "Roman Forum":21, "Spanish Steps":0, "Sistine Chapel":25, "Piazza Navona":0, "Altar of the Fatherland":0}
    Havana = {"Old Havana":0, "Fusterlandia":15, "Museo Nacional de Bellas Artes":6, "National Capitol of Cuba":0, "Grand Theater of Havana":9, "Plaza de la Catedral":0, "Cuban Art Factory":12, "Fort of San Carlos of the Cabin":0}
    Hanoi = {"Hanoi Opera House":0, "Ngoc Son Temple":2, "Hoàn Kiếm Lake":0, "Temple Of Literature":2, "Hoa Lo Prison Relic":2, "Imperial Citadel of Thang Long":0, "Vietnam Museum of Ethnology":2, "Vietnam National Fine Arts Museum":2}
    Budapest = {"Hungarian Parliament Building":29, "Dohány Street Synagogue":27, "Széchenyi Chain Bridge":0, "Buda Castle":0, "Matthias Church":7, "Fisherman's Bastion":0, "Vajdahunyad Castle":2, "Hungarian State Opera":15}
    print("Now let's budget and plan your trip!")
    people = int(input("How many people, including youself, will be traveling?: "))
    if city == "Cairo":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfareint['Cairo'], ", stay per night will be $",stayintpernight['Cairo'], ", and a car rental for all 4 days will be $",transporationint['Cairo'])
        finbudget = finbudget -(people*airfareint['Cairo'])- stayintpernight['Cairo']-transporationint['Cairo']               
    elif city == "London":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfareint['London'], ", stay per night will be $",stayintpernight['London'], ", and a car rental for all 4 days will be $",transporationint['London'])
        finbudget = finbudget -(people*airfareint['London'])- stayintpernight['London']-transporationint['London']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    elif city == "Rome":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfareint['Rome'], ", stay per night will be $",stayintpernight['Rome'], ", and a car rental for all 4 days will be $",transporationint['Rome'])
        finbudget = finbudget -(people*airfareint['Rome'])- stayintpernight['Rome']-transporationint['Rome']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    elif city == "Havana":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfareint['Havana'], ", stay per night will be $",stayintpernight['Havana'], ", and a car rental for all 4 days will be $",transporationint['Havana'])
        finbudget = finbudget -(people*airfareint['Havana'])- stayintpernight['Havana']-transporationint['Havana']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    elif city == "Hanoi":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfareint['Hanoi'], ", stay per night will be $",stayintpernight['Hanoi'], ", and a car rental for all 4 days will be $",transporationint['Hanoi'])
        finbudget = finbudget -(people*airfareint['Hanoi'])- stayintpernight['Hanoi']-transporationint['Hanoi']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    elif city == "Budapest":
        print("I will automatically subtract the cost of airfare per person, stay, and transportation in" ,city, "from the budget. \nAirfare will be $",airfareint['Budapest'], ", stay per night will be $",stayintpernight['Budapest'], ", and a car rental for all 4 days will be $",transporationint['Budapest']) 
        finbudget = finbudget -(people*airfareint['Budapest'])- stayintpernight['Budapest']-transporationint['Budapest']
        print("You still have $",finbudget, "left to plan the rest of your trip.")
    print("")
    if finbudget<=250:
        print("Oh no! It looks like you don't have much money left in your budget for visiting tourist attractions, food, and other spending needs for the rest of the trip.")
        while True:
            try:
                retry = input("Would you like to re-enter a new budget? If so, please enter yes. Otherwise you could always come back another time to plan yout trip. Please enter no if you would like to come back another time: ")
                if retry == "YES" or retry == "Yes" or retry == "yes":
                    print("Great!")
                    break
                elif retry == "NO" or retry == "No" or retry == "no":
                    print("Thank you so much for coming in! We hope to see you again!")
                    return
                else:
                    print("Sorry, I didn't understand that")
            except:
                print("Sorry, I didn't understand that, please try again")
                pass
        intchosen()
    print("")
    print("Now is the fun part! Let's put together an itinerary for your trip.", city, "has a number of renowned tourist attractions.\nHere is a list of those attractions part of our travel package!")
    if city == "Cairo":
        places = ""
        for i, j in Cairo.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Cairo.items():
            print(i, "costs $",j)
    elif city == "London":
        places = ""
        for i, j in London.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in London.items():
            print(i, "costs $",j)
    elif city == "Rome":
        places = ""
        for i, j in Rome.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Rome.items():
            print(i, "costs $",j)
    elif city == "Havana":
        places = ""
        for i, j in Havana.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Havana.items():
            print(i, "costs $",j)
    elif city == "Hanoi":
        places = ""
        for i, j in Hanoi.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Hanoi.items():
            print(i, "costs $",j)
    elif city == "Budapest":
        places = ""
        for i, j in Budapest.items():
            places = places + i + "\n"
            placelst = places.splitlines()
        print(places)
        for i, j in Budapest.items():
            print(i, "costs $",j)
    itinerary = {}
    print("")
    print("Please pick 2 places to visit each day to make the most our of your trip. You will see one in the morning and one in the afternoon.")
    print("Let's start with Day 1")
    while True:
        try:
            loc_1 = int(input("Please enter the number of the first location you would like to visit on Day 1, with 1 being the first location in the above list and 8 being the last: "))
            if loc_1 == 1 or loc_1 == 2 or loc_1 == 3 or loc_1 == 4 or loc_1 == 5 or loc_1 == 6 or loc_1 == 7 or loc_1 == 8:
                a = ((loc_1)-1)
                itinerary["Day 1 morning"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass                      
    while True:
        try:
            loc_2 = int(input("Please enter the number of the second location you would like to visit on Day 1, with 1 being the first location in the above list and 8 being the last: "))
            if loc_2 == 1 or loc_2 == 2 or loc_2 == 3 or loc_2 == 4 or loc_2 == 5 or loc_2 == 6 or loc_2 == 7 or loc_2 == 8:
                a = ((loc_2)-1)
                itinerary["Day 1 afternoon"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass                      
    print("Now let's plan Day 2")
    while True:
        try:
            loc_1 = int(input("Please enter the number of the first location you would like to visit on Day 2, with 1 being the first location in the above list and 8 being the last: "))
            if loc_1 == 1 or loc_1 == 2 or loc_1 == 3 or loc_1 == 4 or loc_1 == 5 or loc_1 == 6 or loc_1 == 7 or loc_1 == 8:
                a = ((loc_1)-1)
                itinerary["Day 2 morning"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass                      
    while True:
        try:
            loc_2 = int(input("Please enter the number of the second location you would like to visit on Day 2, with 1 being the first location in the above list and 8 being the last: "))
            if loc_2 == 1 or loc_2 == 2 or loc_2 == 3 or loc_2 == 4 or loc_2 == 5 or loc_2 == 6 or loc_2 == 7 or loc_2 == 8:
                a = ((loc_2)-1)
                itinerary["Day 2 afternoon"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass   
    print("Next up is Day 3")
    while True:
        try:
            loc_1 = int(input("Please enter the number of the first location you would like to visit on Day 3, with 1 being the first location in the above list and 8 being the last: "))
            if loc_1 == 1 or loc_1 == 2 or loc_1 == 3 or loc_1 == 4 or loc_1 == 5 or loc_1 == 6 or loc_1 == 7 or loc_1 == 8:
                a = ((loc_1)-1)
                itinerary["Day 3 morning"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass                      
    while True:
        try:
            loc_2 = int(input("Please enter the number of the second location you would like to visit on Day 3, with 1 being the first location in the above list and 8 being the last: "))
            if loc_2 == 1 or loc_2 == 2 or loc_2 == 3 or loc_2 == 4 or loc_2 == 5 or loc_2 == 6 or loc_2 == 7 or loc_2 == 8:
                a = ((loc_2)-1)
                itinerary["Day 3 afternoon"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass   
    print("Finally, let's plan Day 4")
    while True:
        try:
            loc_1 = int(input("Please enter the number of the first location you would like to visit on Day 4, with 1 being the first location in the above list and 8 being the last: "))
            if loc_1 == 1 or loc_1 == 2 or loc_1 == 3 or loc_1 == 4 or loc_1 == 5 or loc_1 == 6 or loc_1 == 7 or loc_1 == 8:
                a = ((loc_1)-1)
                itinerary["Day 4 morning"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass                      
    while True:
        try:
            loc_2 = int(input("Please enter the number of the second location you would like to visit on Day 4, with 1 being the first location in the above list and 8 being the last: "))
            if loc_2 == 1 or loc_2 == 2 or loc_2 == 3 or loc_2 == 4 or loc_2 == 5 or loc_2 == 6 or loc_2 == 7 or loc_2 == 8:
                a = ((loc_2)-1)
                itinerary["Day 4 afternoon"] = placelst[a]
                break
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass
    print("")
    print("Here is your final itinerary!")
    for i in itinerary:
        print(i, ":", itinerary[i])
    if city == "Cairo":
        goodbye = "Ma'a El Salama."
    elif city == "London":
        goodbye = "Goodbye."
    elif city == "Rome":
        goodbye = "Arrivederci."
    elif city == "Havana":
        goodbye = "Adiós."
    elif city == "Hanoi":
        goodbye = "Tạm biệt."
    elif city == "Budapest":
        goodbye = "Viszontlátásra."
    print("")
    print("We are so happy that you have been able to successfully plan your trip with our travel agency! \nThank you so much for coming in! \nWe hope you enjoy your trip! Goodbye, or as they say in", city,",", goodbye)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    while True:
        try:
            end = input("Please enter STOP if you would like to end the program and CONTINUE if you would like to exit: ")
            if end == "stop" or end == "STOP" or end == "Stop":
                quit()
            elif end == "CONTINUE" or end == "Continue" or end == "continue":
                begin()
            else:
                print("Sorry, I didn't understand that")
        except:
            print("Sorry, I didn't understand that, please try again")
            pass
    


def domchoice():
    num = input("Please input the number of the city from the above list which you would like to view: ")
    if num == "1":
        print("Los Angeles is located on thw west coast on the U.S.\nIt is incredibly diverse\nPopular tourist attractions include The Hollywood Sign and Universal Studios Hollywood\n")
    elif num == "2":
        print("Miami is full of beautiful beaches\nThe city is visited by 14 million tourists every year\nPopular tourist destinations include the Bayside Marketplace and Vizcaya Museum and Gardens")
    elif num == "3":
        print("Chicago is commonly referred to as the 'Windy City'. It is the third largest city in the U.S.\nPopular spots of visit are The Art Institute ot Chicago and Millenium Park.\n")
    elif num == "4":
        print("Charleston is located on the east coast.\n Charleston has a rich history. The first shots of the civil were fired here.\nIt is known for the South Caroline Aquarium and Charleson City Market")
    elif num == "5":
        print("Seattle is known for its seafood.\nIt is located in the Northeast of the U.S.\nPopular tourist attractions are the Space Needle and the Seattle Waterfront")
    elif num == "6":
        print("Houston is a bustling city.\nIt is known for NASA's Johnson Space Center.\nIt also showcases one of the largest rodeos in the world.")
    else:
        print("Sorry I didn't quite get that. Please type BROWSE if you would like to look through the above cities or type STOP to make your final choice")
        domchoice()
        
def intchoice():
    num = input("Please input the number of the city from the above list which you would like to view: ")
    if num == "1":
        print("Cairo is the capital of Egypt and its largest city.\nThe Nile River, the longest river in the world, passes through the city.\nIt is home to incredibly the incredibly famous Pyramids of Giza and the Sphinx")
    elif num == "2":
        print("London is home to the infamous royal family.\n Popular tourist attractions include Buckingham Palace and the London Eye.")
    elif num == "3":
        print("Rome has an incredibly deep history.\nIt boasts the Colosseum and the Trevi Fountain.\n It is also known for its cuisine.")
    elif num == "4":
        print("Havana is the largest city in the Caribbean.\nIt is Cuba's capitol city.\nPopular tourist attractions include Castillo De Los Tres Reyes Del Morro and Museo Nacional de Bellas Artes")
    elif num == "5":
        print("Hanoi is the capitol of Vietnam.\nIts name means 'City of Lakes'.\nHanoi boasts many attractions such as the Temple of Literature and the Hanoi Opera House.")
    elif num == "6":
        print("Budapest is known for its beautiful architecture.\n It is the capitol of Hungary.\nIt is known for Buda Castle and Fisherman's Bastion.")
    else:
        print("Sorry I didn't quite get that. Please type BROWSE if you would like to look through the above cities or type STOP to make your final choice")
        intchoice()

def domfinal():
    done = False
    while not done:
        choice = input("Please type BROWSE if you would like to look through potential destinations. If you would like to make your final decision please type STOP: ")
        if choice == "BROWSE" or choice == "browse" or choice == "Browse":
            domchoice()               
        elif choice == "STOP" or choice == "stop" or choice == "Stop":
            print("We are so glad you have made your final decision!")
            final = input("What city would you like to travel to? Please enter the number associated with the city above: ")
            if final == "1":
                domfinal.var = "Los Angeles"
                print("Los Angeles is a wonderful choice!")
            elif final == "2":
                domfinal.var = "Miami"
                print("Miami is a wonderful choice!")
            elif final == "3":
                domfinal.var = "Chicago"
                print("Chicago is a wonderful choice")
            elif final == "4":
                domfinal.var = "Charleston"
                print("Charleston is a wonderful choice!")
            elif final == "5":
                domfinal.var = "Seattle"
                print("Seattle is a wonderful choice!")
            elif final == "6":
                domfinal.var = "Houston"
                print("Houston is a wonderful choice!")
            else:
                print("Sorry I didn't quite get that.")
                finaldestdom()
            done = True 
        else:
            print("Sorry I didn't quite get that. Please type BROWSE if you would like to look through the cities or type STOP to make your final choice")
            domfinal()
    domchosen()
            
def intfinal():
    done = False
    while not done:
        choice = input("Please type BROWSE if you would like to look through potential destinations. If you would like to make your final decision please type STOP: ")
        if choice == "BROWSE" or choice == "browse" or choice == "Browse":
            intchoice()               
        elif choice == "STOP" or choice == "stop" or choice == "Stop":
            print("We are so glad you have made your final decision!")
            final = input("What city would you like to travel to? Please enter the number associated with the city above: ")
            if final == "1":
                print("Cairo is a wonderful choice!")
                intfinal.var = "Cairo"
            elif final == "2":
                intfinal.var = "London"
                print("London is a wonderful choice!")
            elif final == "3":
                intfinal.var = "Rome"
                print("Rome is a wonderful choice")
            elif final == "4":
                intfinal.var = "Havana"
                print("Havana is a wonderful choice!")
            elif final == "5":
                intfinal.var = "Hanoi"
                print("Hanoi is a wonderful choice!")
            elif final == "6":
                intfinal.var = "Budapest"
                print("Budapest is a wonderful choice!")
            else:
                print("Sorry I didn't quite get that.")
                finaldestint()
            done = True
        else:
            print("Sorry I didn't quite get that. Please type BROWSE if you would like to look through the cities or type STOP to make your final choice")
            intfinal()
    intchosen()
    


def Destinations():
    int_or_dom = input("Would you like to travel domestically or internationally? Type 1 for domestic and 2 for international: ")
    if int_or_dom == "1":
        print("Great! We offer a number of domestic travel packages. Please keep in mind that all of our travel packages are four day trips.")
        print("Destinations in the United States include:\n1. Los Angeles, California\n2. Miami, Florida\n3. Chicago, Illinois\n4. Charleston, South Carolina\n5. Seattle, Washington\n6. Houston, Texas")
        domfinal()            
    elif int_or_dom == "2":
        print("Great! We offer a number of international travel packages. Please keep in mind that all of our travel packages are four day trips.")
        print("Destinations outside the United States include:\n1. Cairo, Egypt\n2. London, England\n3. Rome, Italy\n4. Havana, Cuba\n5. Hanoi, Vietnam\n6. Budapest, Hungary")
        intfinal()
    else:
        print("Sorry, I didn't understand that.")
        Destinations()

print("Hello! Welcome to the Natarajan Travel Agency!\nWe are so happy that you have chosen us to help you plan your dream vacation!")
def begin():
    decision = input("Are you ready to start planning your trip?: ")
    if decision == "YES" or decision == "yes" or decision == "Yes":
        print("That is great news!")
        Destinations()
    elif decision == "NO" or decision == "no" or decision == "No":
        print("Thank you for visiting us! Please come again soon!")
    else:
        print("Sorry, I didn't understand that. Please enter Yes or No")
        begin()

begin()
