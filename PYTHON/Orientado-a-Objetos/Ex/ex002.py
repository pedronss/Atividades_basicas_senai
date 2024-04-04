import os
import random
class Players:
    def __init__(self):
        global enemy
        self.x=0
        self.y=0
    def moveright(self):
        if self.x<=3:
            self.x+=1
    def moveleft(self):
        if self.x>=0:
            self.x-=1
    def moveup(self):
        if self.y<=3:
            self.y+=1
    def movedown(self):
        if self.y>=0:    
            self.y-=1
    def reset(self):
        player.pontos=0
        player.x=0
        player.y=0
    def collision(self,enemy):
        dead=False
        if self.x==enemy.x and self.y==enemy.y:
            dead=True
        return dead
player=Players()
enemy = Players()
player.pontos=0
enemy.x = random.randint(0, 3)  
enemy.y = random.randint(0, 3)
while True:
    os.system("cls")
    print(f"x= {player.x} y= {player.y}")
    print(f"Enemy x= {enemy.x} Enemy y= {enemy.y}")
    print(f"Pontos: {player.pontos}")
    command=input("")
    match command:
        case "d":
            player.moveright()
            if player.x<=3 and player.y<=3  and player.x > 0:
                player.pontos+=1
            else:
                player.reset()
            check=player.collision(enemy)
            if check :
                os.system("cls")
                input("Você morreu!!")
                break

        case "a":
            player.moveleft()
            if player.x<=3 and player.y<=3 and player.x > 0:
                player.pontos+=1
            else:
                player.reset()
            check=player.collision(enemy)
            if check :
                os.system("cls")
                input("Você morreu!!")
                break
        case "w":
            player.moveup()
            if player.x<=3 and player.y<=3 and player.y > 0:
                player.pontos+=1
            else:
                player.reset()
            check=player.collision(enemy)
            if check :
                os.system("cls")
                input("Você morreu!!")
                break
        case "s":
            player.movedown()
            if player.x<=3 and player.y<=3 and player.y > 0:
                player.pontos+=1
            else:
                player.reset()
            check=player.collision(enemy)
            if check :
                os.system("cls")
                input("Você morreu!!")
                break
