from pet import Pet

def main():
    # Create a pet
    my_pet = Pet("Max")
    print("Creating pet: Max")

    # Interactions
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()

    # Teach tricks
    my_pet.train("roll over")
    my_pet.train("play dead")

    # Show status and tricks
    my_pet.get_status()

if __name__ == "__main__":
    main()

