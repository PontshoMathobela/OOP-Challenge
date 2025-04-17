class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"🍽️ {self.name} is eating... Hunger: {self.hunger}, Happiness: {self.happiness}")


    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"💤 {self.name} is sleeping... Energy: {self.energy}")


    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"🎾 {self.name} is playing... Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"😴 {self.name} is too tired to play. Let them sleep!")

    def train(self, trick):
        if isinstance(trick, str) and trick.strip():
            self.tricks.append(trick.strip())
            print(f"🎓 {self.name} learned a new trick: {trick.strip()}!")
        else:
            print("❌ Invalid trick. Please provide a non-empty string.")

    def show_tricks(self):
        if self.tricks:
            print(f"🐾 {self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"🐾 {self.name} hasn’t learned any tricks yet.")

    def get_status(self):
        print(f"\n📋 {self.name}'s Current Status:")
        print(f"  Hunger: {self.hunger}")
        print(f"  Energy: {self.energy}")
        print(f"  Happiness: {self.happiness}")
        print(f"  Tricks: {', '.join(self.tricks) if self.tricks else 'None'}\n")

