def greet_user():
    name = input("What's your name?: ")

    time = int(input("Which hour of the day are you on right now?(0-23): "))
    
    while True:
        if 0 <= time <= 23:
            break
        else:
            time = int(input("Which hour of the day are you on right now?(0-23): "))
    
    if 0 <= time <= 12:
        print(f"Good morning, {name}!")
    elif 13 <= time <= 17:
        print(f"Good afternoon, {name}!")
    else 18 <= time <= 23:
        print(f"Good evening, {name}!")

greet_user()
