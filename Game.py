from pygame import *
import math as m

init()
font.init()

warna_text = (255,255,255)
font = font.Font(None,40)
win = font.render("YOU WIN,YOU ESCAPED",True, warna_text)

warna_textt = (255,0,0)
lose = font.render("YOU LOSE",True, warna_textt)

class karakter(sprite.Sprite): #sprite.sprite artinya install semua fungsi2 sprite di pygame. kyk: collision, klik char/tidak, dll

    #karakteristik dari char yg kita buat
    def __init__(self, player_image, x, y, width, height, speed):
        #install dari parent class
        super().__init__()
        
        #upload image karakter
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed

        #buat frame buat karakter
        self.rect = self.image.get_rect()

        #lokasiin frame char ke dalam x dan y
        self.rect.x = x
        self.rect.y = y

    #fungsi untuk tampilin char ke layar
    def show(self):
        #window adalah nama variabel screen.jadi
        screen.blit(self.image  , (self.rect.x, self.rect.y))

    def nabrak(self, karakter_lain):
        return self.rect.colliderect(karakter_lain)    


class player(karakter): #kelas player adalah anak class dari katakter

    #control player
    def control(self):

        #untuk tau key apa yg kita tekan
        keys = key.get_pressed()

        if keys[K_a] and self.rect.x > 5: #kalo keyboard a
            self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < width: #kalo keyboard d
            self.rect.x += self.speed

        if keys[K_w] and self.rect.y > 5: #kalo keyboard w (kalo di pygame yang ke atas Y nya -)
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < height: #kalo keyboard s  (kalo di pygame yang ke bawah Y nya +)
            self.rect.y += self.speed

class enemy(karakter):
    def move_towards_player(self, Player ):
        dx, dy = self.rect.x - Player.rect.x, self.rect.y - Player.rect.y
        dist = m.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist
        self.rect.x -= dx * self.speed
        self.rect.y-=dy*self.speed

#step 6: buat dinding
class dinding():
    #karakteristik dinding
    def __init__(self, x, y, width, height, warna):
        #cara bikin persegi
        self.rect = Rect(x,y,width,height)
        self.warna = warna

    #method dinding
    def show(self):
        draw.rect(screen, self.warna, self.rect)

    #method dinding untuk kena dinding/ngga
    def nabrak(self, karakter_lain):
        return self.rect.colliderect(karakter_lain)

#screen:
width = 500
height = 500
screen = display.set_mode((width, height))

#step 8: karna bg nya foto, di upload dulu
img_back = "backg.jpeg"
bg_image = transform.scale(image.load(img_back), (width, height))

#step 9: taruh bg image ke screen
screen.blit(bg_image,(0,0))

mc_width = 40
mc_height = 40
mc_speed = 2
img_mc = "plankton.png"
mc = player(img_mc, 430, 425, mc_width, mc_height, mc_speed)

kreb_width = 50
kreb_height = 50
kreb_speed = 1
img_kreb = "kreb.png"
kreb = enemy(img_kreb, 30, 425, kreb_width, kreb_height, kreb_speed)

kunci_width = 50
kunci_height = 50
kunci_speed = 0
img_kunci = "kunci.png"
kunci = karakter(img_kunci, 360, 425, kunci_width, kunci_height, kunci_speed)

fps = time.Clock()
gamestart = True
warna = (0,0,255)
merah = (255,0,0)
dinding1 = dinding(0,0,400,10,warna)
dinding2 = dinding(490,0,10,500,warna)
dinding3 = dinding(0,490,500,10,warna)
dinding4 = dinding(0,0,10,500,warna)
dindingtngh1 = dinding(70,40,10,250,warna)
dindingtngh2 = dinding(150,150,10,250,warna)
dindingtngh3 = dinding(80,400,150,10,warna)
dindingtngh4 = dinding(250,0,10,250,warna)
dindingtngh5 = dinding(300,100,100,10,warna)
dindingtngh6 = dinding(350,200,250,10,warna)
dindingtngh7 = dinding(270,330,10,250,warna)
dindingtngh8 = dinding(420,390,10,220,warna)
dindingtngh9 = dinding(340,390,90,10,warna)
dindingkunci = dinding(400,0,100,10,merah)

pegang_kunci = False
while gamestart:
    screen.blit(bg_image,(0,0))
    mc.show()
    kreb.show()
    kunci.show()
    dinding1.show()
    dinding2.show()
    dinding3.show()
    dinding4.show()
    dindingtngh1.show()
    dindingtngh2.show()
    dindingtngh3.show()
    dindingtngh4.show()
    dindingtngh5.show()
    dindingtngh6.show()
    dindingtngh7.show()
    dindingtngh8.show()
    dindingtngh9.show()
    dindingkunci.show()

    mc.control()
    kreb.move_towards_player(mc)



    #deteksi event = apa aja yg terjadi pas kita mainin gamenya. contoh pas kita pencet x, nanti keluar
    for e in event.get():
        #jika event = pencet tombol x
        if e.type == QUIT:
            gamestart = False
    if dinding1.nabrak(mc) or dinding2.nabrak(mc) or dinding3.nabrak(mc) or dinding4.nabrak(mc) or dindingtngh1.nabrak(mc) or dindingtngh2.nabrak(mc) or dindingtngh3.nabrak(mc) or dindingtngh4.nabrak(mc) or dindingtngh5.nabrak(mc) or dindingtngh6.nabrak(mc) or dindingtngh7.nabrak(mc) or dindingtngh8.nabrak(mc) or dindingtngh9.nabrak(mc) :
        mc.rect.x,mc.rect.y = 430,425
    if mc.nabrak(kunci):
        pegang_kunci = True 
        kunci.rect.x = 1000
        dindingkunci.rect.x = 1000
    if mc.nabrak(kreb) :
        mc.speed = 0 
        kreb.speed = 0
        screen.blit(lose,(150,250))
    if (mc.rect.x > 400 and mc.rect.x < 500) and mc.rect.y <= 20 :
        screen.blit(win,(100,250))
        mc.speed = 0
        kreb.speed = 0

    display.update()

    #set fps
    fps.tick(60)


