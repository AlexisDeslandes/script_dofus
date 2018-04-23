from pymouse import PyMouse
import pyscreenshot as ImageGrab
from time import sleep
from bouf_bot import *

mouse = PyMouse()
position = 0
compte_combat = 0
couleur_sans_sort = (190, 185, 152)

def trouver_mechant_nb(limite):
    if limite == 2:
        return (0,0)
    couleur_voulue = (159,89,170)
    couleur_voulue_2 = (46,33,52)
    couleur_voulue_3 = (141,45,150)
    image = ImageGrab.grab()
    for y in range(200, 800):
        for x in range(100, 1000):
            pixel = image.getpixel((x,y))
            if pixel == couleur_voulue or pixel == couleur_voulue_2 or pixel == couleur_voulue_3:
                return (x,y)
    limite += 1
    return trouver_mechant_nb(limite)

def lancer_combat(position_mechant):
    mouse.click(position_mechant[0],position_mechant[1])
    sleep(4)
    position_mechant = trouver_mechant_nb(0)
    mouse.click(position_mechant[0],position_mechant[1])
    sleep(4)

def trouve_joueur():
    return trouve_joueur_aux(0)

def trouve_joueur_aux(compte):
    if compte == 5:
        return (0,688)
    couleur_perso = (255, 204, 0)
    image = ImageGrab.grab()
    for y in range(200, 800):
        for x in range(100, 1000):
            if (image.getpixel((x,y)) == couleur_perso):
                return (x,y)
    compte += 1
    return trouve_joueur_aux(compte)

def besoin_repos():
    image = ImageGrab.grab()
    for x in range(100,1000):
        for y in range(200,800):
            if image.getpixel((x,y)) == (255,255,102):
                return True
    return False


def repos():
    print "Repos pour 5 secondes"
    sleep(5)

def click_soi():
    position_perso = trouve_joueur()
    pos_x = position_perso[0]
    pos_y = position_perso[1] + 10
    mouse.click(pos_x,pos_y)

def lance_sort_1():
    image = ImageGrab.grab()
    pixel_reconnais_sort_1 = image.getpixel((687,896))
    while (not (pixel_reconnais_sort_1 == (119,119,119))):
        mouse.click(687,900)
        sleep(0.5)
        click_soi()
        sleep(1.0)
        mouse.click(300,300)
        image = ImageGrab.grab()
        pixel_reconnais_sort_1 = image.getpixel((687,896))

def lance_sort_2():
    image = ImageGrab.grab()
    pixel_reconnais_sort_2 = image.getpixel((723,896))
    while (not (pixel_reconnais_sort_2 == (120,120,119))):
        mouse.click(723,896)
        sleep(0.5)
        click_soi()
        sleep(1.0)
        mouse.click(300,300)
        image = ImageGrab.grab()
        pixel_reconnais_sort_2 = image.getpixel((723,896))

def lance_sort_3():
    image = ImageGrab.grab()
    pixel = image.getpixel((688,866))
    while (trouve_joueur()[1]<687):
        mouse.click(757,910)
        sleep(0.5)
        click_soi()
        mouse.move(300,300)
        sleep(1)
        image = ImageGrab.grab()
        pixel = image.getpixel((688,866))
        if pixel == couleur_sans_sort:
            return

def attendre_debut():
    image = ImageGrab.grab()
    while not image.getpixel((121,367)) == (156,94,70):
        sleep(0.5)
        image = ImageGrab.grab()
    sleep(1)

def lance_pret():
    sleep(1)
    mouse.move(875,747)
    sleep(0.5)
    mouse.click(875,747)
    attendre_debut()

def lance_fin_de_tour():
    mouse.click(630,909)
    compte = 0
    while not pas_en_combat():
        image = ImageGrab.grab()
        if image.getpixel((121,367)) == (156,94,70):
            if compte > 4:
                position_ennemi = trouver_mechant(couleur_br)
                for i in range(2):
                    lancer_feu((position_ennemi[0],position_ennemi[1]))
            mouse.click(630,909)
            compte += 1

def enleve_fin_de_combat():
    x_to_click = 742
    mouse.click(480,553)
    sleep(0.2)
    mouse.click(480,553)
    sleep(0.2)
    mouse.click(480,553)
    for y in range(520,780,20):
        mouse.click(x_to_click,y)
        sleep(0.2)

def jouer_combat():
    lance_sort_1()
    lance_sort_2()
    lance_sort_3()
    lance_fin_de_tour()
    enleve_fin_de_combat()

def pas_en_combat():
    image = ImageGrab.grab()
    pixel = image.getpixel((688,866))
    couleur_gain_niveau = (171, 166, 137)
    return pixel == couleur_sans_sort or pixel == couleur_gain_niveau

def assoir():
    mouse.click(63,786)

def supprime_items():
    mouse.click(771,435)
    sleep(0.5)
    image = ImageGrab.grab()
    while image.getpixel((435,686)) == (255,97,0):
        mouse.click(771,435)
        sleep(0.5)
        mouse.click(424,687)
        sleep(0.5)
        mouse.click(502,766)
        sleep(0.5)
        mouse.click(348,750)
        sleep(0.5)
        mouse.click(478,748)
        sleep(0.5)
        mouse.click(396,538)
        sleep(0.5)
        mouse.click(771,435)
        sleep(0.5)
        image = ImageGrab.grab()

def supprime_objets():
    mouse.click(708,807)
    sleep(1)
    mouse.click(825,340)
    supprime_items()
    mouse.click(853,339)
    supprime_items()
    mouse.click(928,258)

if __name__=='__main__':
    supprime_objets()
    while(True):
        if pas_en_combat():
            assoir()
            while besoin_repos():
                repos()
            if compte_combat == 10:
                supprime_objets()
                compte_combat = 0
            position_mechant = trouver_mechant_nb(0)
            if (position_mechant != (0,0)):
                lancer_combat(position_mechant)
                jouer_combat()
                compte_combat += 1
                print "Compteur de combat a " + str(compte_combat)
            else:
                if position == 0:
                    mouse.click(30,480)
                    position = 1
                else:
                    mouse.click(927,484)
                    position = 0
        else:
            jouer_combat()
            compte_combat += 1
            print "Compteur de combat a " + str(compte_combat)

        sleep(5.0)
