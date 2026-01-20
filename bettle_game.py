class Fighter:
    def __init__(self,name,health,strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    def attack(self,enemy):      
        enemy.health -= self.strength
        print(f"{self.name} attack on {enemy.name} give {self.strength} damage")
        print(f"{enemy.name}'s health remains {enemy.health}")
        
fighter1 = Fighter("Alpha" , 100 , 20)
fighter2 = Fighter("Gamma",100 , 10)

fighter1.attack(fighter2)
fighter2.attack(fighter1)