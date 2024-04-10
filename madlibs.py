def mad_libs():
    # Prompt the user for input
    name = input("Enter a name: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    # Print the story with user input
    print(f"\nOnce upon a time, there was a {adjective} {noun} named {name}.")
    print(f"{name} loved to {verb} in the park every day.")
    print(f"One day, while {name} was {verb}ing, a magical {noun} appeared out of nowhere!")
    print(f"{name} couldn't believe their eyes and {verb}ed away happily ever after.")

# Call the function to play the game
mad_libs()