JobTitle1 = input("Enter a job title: ") 
Name1 = input("Enter a name: ")
Place1 = input("Enter a place: ")
Food1 = input("Enter a food: ")
Number1 = int(input("Enter a positive number: "))

print(f"Once upon a time, there was a {JobTitle1}, called {Name1}.")
print(f"{Name1} went to {Place1} and ate {Food1}. The journey took {Number1} hours!")

Choice1 = input(f"Do you want {Name1} to explore further (E) or go home (H): ")

if Choice1 == "E":
    # ==> CONTINUE THE STORY WITH YOUR OWN SENTENCES - ADD MORE OF YOUR OWN VARIABLES ABOVE
    print("...")

elif Choice1 == "H":
    print(f"Okay, {Name1} has gone home.")