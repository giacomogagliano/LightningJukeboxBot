# Definiamo alcune strategie (algoritmi) per un gioco di combattimento


class SwordAttack:
    def execute(self):
        return "Attacco con la spada!"


class BowAttack:
    def execute(self):
        return "Attacco con l'arco!"


class MagicAttack:
    def execute(self):
        return "Attacco magico!"


# La classe Character utilizza una strategia specifica per l'attacco


class Character:
    def __init__(self, name, attack_strategy):
        self.name = name
        self.attack_strategy = attack_strategy

    def attack(self):
        return f"{self.name} dice: {self.attack_strategy.execute()}"


# Creiamo alcuni personaggi con diverse strategie di attacco

sword_character = Character("Guerriero", SwordAttack())
bow_character = Character("Arciere", BowAttack())
magic_character = Character("Mago", MagicAttack())

# Testiamo le strategie

print(
    sword_character.attack()
)  # Output: "Guerriero dice: Attacco con la spada!"
print(
    bow_character.attack()
)  # Output: "Arciere dice: Attacco con l'arco!"
print(
    magic_character.attack()
)  # Output: "Mago dice: Attacco magico!"
