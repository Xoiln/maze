import pygame
import sys
v = 700
h = 500

pygame.font.init()
font = pygame.font.SysFont(None,70)
win = font.render("You Win!",True,(255,215,0))
lose = font.render("You Lose!",True,(255,215,0))


window = pygame.display.set_mode((v,h))
pygame.display.set_caption("Лабіринт")
bg = pygame.transform.scale(pygame.image.load("fon.png"),(v,h))


pygame.mixer.init()
pygame.mixer.music.load("Kahoot-music.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1) #гучнісьть фонової музики
game_key = pygame.mixer.Sound("key.ogg")
kick = pygame.mixer.Sound("window-false.ogg")
game_win = pygame.mixer.Sound("winn.ogg")
game_false = pygame.mixer.Sound("game_false.ogg")
kick.set_volume(0.1)
game_key.set_volume(0.1)
game_win.set_volume(0.1)
game_false.set_volume(0.1)


class Player(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image),(70,70))
        self.speed = player_speed
        self.rect = self.image.get_rect() #створити рамку навколо картинки спрайта
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self): #Функція для того щоб намалювати спрайт на екрані
        window.blit(self.image,(self.rect.x,self.rect.y))



class Enemy(Player):
    direction = "right"
    def update(self):
        if self.rect.x <= 250:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed



class Hero(Player):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys [pygame.K_s] and self.rect.y <= 425:
            self.rect.y += self.speed
        if keys [pygame.K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys [pygame.K_d] and self.rect.x <= 635:
            self.rect.x += self.speed
        


class Wall(pygame.sprite.Sprite):
    def __init__(self,width,height,color,wall_x,wall_y):
        super().__init__()
        self.width = width
        self.height = height
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

 

hero = Hero("Gost.png",10,400,7)
enemy = Enemy("enemy.png",500,150,5)
heart = Player("heart_game.png",500,10,0)
heeart = Player("heart_game.png",560,10,0)
heaart = Player("heart_game.png",620,10,0)
treasure = Player("treasure.png",400,400,0)
key = Player("ключ.png",570,400,0)
key1 = Player("ключ.png",20,30,0)
w1 = Wall(10,500,(255,0,0),0,0)
w2 = Wall(700,10,(255,0,0),0,0)
w3 = Wall(700,10,(255,0,0),0,490)
w4 = Wall(10,500,(255,0,0),690,0)
w5 = Wall(10,135,(255,0,0),100,0)
w6 = Wall(10,300,(255,0,0),100,250)
w7 = Wall(150,10,(255,0,0),100,250)
w8 = Wall(10,140,(255,0,0),250,120)
w9 = Wall(300,10,(255,0,0),250,120)
w10 = Wall(10,135,(255,0,0),540,120)
w11 = Wall(10,150,(255,0,0),540,370)
w12 = Wall(320,10,(255,0,0),225,370)
w13 = Wall(10,120,(255,0,0),400,250)
w14 = Wall(110,10,(255,0,0),0,130)
w15 = Wall(10,120,(255,0,0),220,370)


n = 0
game = True
finish = False
clock = pygame.time.Clock()
FPS = 60
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    window.blit(bg,(0,0))
    if finish != True:
        window.blit(bg,(0,0))
        hero.update() #змушуємо рухатисчя головного героя
        enemy.update()
        hero.reset() #оновлюємо головного героя на сцені
        enemy.reset()
        treasure.reset()
        key.reset()
        key1.reset()
        heart.update()
        heeart.update()
        heaart.update()
        heart.reset()
        heeart.reset()
        heaart.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        if pygame.sprite.collide_rect(hero,enemy):
            n +=1
            hero.rect.x = 10
            hero.rect.y = 400
            kick.play()
            if n == 1:
                heart.rect.x = -100
                heart.rect.y = -100
            if n == 2:
                heeart.rect.x = -100
                heeart.rect.y = -100
            if n == 3:
                heaart.rect.x = -100 
                heaart.rect.y = -100
                pygame.mixer.music.pause()
                finish = True
                FPS = FPS - 59
                window.blit(lose,(200,200))
                game_false.play
        if pygame.sprite.collide_rect(hero,w1) or pygame.sprite.collide_rect(hero,w2) or pygame.sprite.collide_rect(hero,w3) or pygame.sprite.collide_rect(hero,w4) or pygame.sprite.collide_rect(hero,w5) or pygame.sprite.collide_rect(hero,w6) or pygame.sprite.collide_rect(hero,w7) or pygame.sprite.collide_rect(hero,w8) or pygame.sprite.collide_rect(hero,w9) or pygame.sprite.collide_rect(hero,w10) or pygame.sprite.collide_rect(hero,w11) or pygame.sprite.collide_rect(hero,w12) or pygame.sprite.collide_rect(hero,w13) or pygame.sprite.collide_rect(hero,w14) or pygame.sprite.collide_rect(hero,w15):
            n +=1
            hero.rect.x = 10
            hero.rect.y = 400
            kick.play()
            if n == 1:
                heart.rect.x = -100
                heart.rect.y = -100
            if n == 2:
                heeart.rect.x = -100
                heeart.rect.y = -100
            if n == 3:
                heaart.rect.x = -100
                heaart.rect.y = -100
                pygame.mixer.music.pause()
                window.blit(lose,(200,200))
                game_false.play()
                finish = True
                FPS = FPS - 59
        if pygame.sprite.collide_rect(hero,treasure):
            FPS = FPS - 59
            window.blit(win,(200,200))
            finish = True
            pygame.mixer.music.pause()
            game_win.play()
        if pygame.sprite.collide_rect(hero,key):
            key.rect.x = -100
            key.rect.y = -100
            w14.rect.x = -100
            w14.rect.y = -100
            game_key.play()
        if pygame.sprite.collide_rect(hero,key1):
            key1.rect.x = -100
            key1.rect.y = -100
            w15.rect.x = -100
            w15.rect.y = -100
            game_key.play()
    pygame.display.update()
    clock.tick(FPS)