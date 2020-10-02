command = ""
started = False
stopped = False
#while command != 'quit':
while True:
    command = input("> ").lower()
    if command =="start":
        if started:
            print('the car is already started')
        else:
            started = True
            print("Car started.. Ready to go")
    elif command == "stop":
        if stopped:
            print('Car already stopped')
        else:
            stopped = True
            print("Car stopped..")
    elif command == "quit":
        break
    elif command == "help":
        print("""
        start - to start the car
        stop  - to stop the car
        quit  - to quit
        """)
    else:
        print("I don't understand that")
