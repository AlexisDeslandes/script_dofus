import pymouse
import pyscreenshot as ImageGrab
from time import sleep
from bot_dofus import *

x_debut = 0
x_fin = 960
y_debut = 220
y_fin = 777

couleur_boufton_blanc = (252,235,196)
couleur_bouftou = (228,212,177)
couleur_br = (0, 0, 255)
mouse = pymouse.PyMouse()

def attendre_un_tour():
    mouse.move(630,909)
    sleep(0.5)
    mouse.click(630,909)
    sleep(1)
    image = ImageGrab.grab()
    while not image.getpixel((121,367)) == (156,94,70):
        sleep(0.5)
        image = ImageGrab.grab()
    sleep(1)

def lancer_flamiche(position):
    mouse.move(688,865)
    sleep(0.5)
    mouse.click(688,865)
    sleep(0.7)
    mouse.click(position[0],position[1])
    sleep(0.2)
    mouse.move(200,200)
    sleep(1.0)


def marcher_droite_fond():
    pos_perso = trouve_joueur()
    mouse.move(pos_perso[0]+135,pos_perso[1])
    sleep(0.5)
    mouse.click(pos_perso[0]+135,pos_perso[1])
    sleep(1)

def lancer_feu(position):
    mouse.move(830,905)
    sleep(0.5)
    mouse.click(830, 905)
    sleep(0.7)
    mouse.click(position[0],position[1])
    sleep(0.2)
    mouse.move(200,200)
    sleep(1.0)

def trouver_mechant(couleur_mechant):
    image = ImageGrab.grab()
    for x in range(x_debut,x_fin):
        for y in range(y_debut,y_fin):
            if image.getpixel((x,y)) == couleur_mechant:
                return (x,y)
    return trouver_mechant(couleur_mechant)

def lancer_combat_boufton():
    position = trouver_mechant(couleur_boufton_blanc)
    mouse.click(position[0],position[1])
    sleep(2)
    if pas_en_combat():
        return lancer_combat_boufton()
    mouse.move(871, 713)
    sleep(0.3)
    mouse.click(871,713)
    print "combat verouille"
    sleep(1.5)

def lancer_combat_bouftou():
    position = trouver_mechant(couleur_bouftou)
    mouse.click(position[0],position[1])
    sleep(2)
    if pas_en_combat():
        return lancer_combat_bouftou()
    mouse.move(871, 713)
    sleep(0.3)
    mouse.click(871,713)
    print "combat verouille"
    sleep(1.5)

def typical_debut():
    lancer_combat_boufton()
    sleep(4)
    lance_pret()

def jouer_combat_1():
    for i in range(3):
        marcher_droite_fond()
        attendre_un_tour()
    jouer_combat()

def combat_1():
    lancer_combat_boufton()
    mouse.move(202,604)
    sleep(0.5)
    mouse.click(202,604)
    lance_pret()
    jouer_combat_1()

def jouer_combat_2():
    for i in range(3):
        marcher_droite_fond()
        attendre_un_tour()
    jouer_combat()

def combat_2():
    lancer_combat_boufton()
    mouse.move(244,694)
    sleep(0.5)
    mouse.click(244,694)
    sleep(0.5)
    lance_pret()
    jouer_combat_2()


def combat_3():
    lancer_combat_boufton()
    mouse.move(383,580)
    sleep(0.5)
    mouse.click(383,580)
    lance_pret()
    jouer_combat()

def combat_4():
    typical_debut()
    jouer_combat()

def combat_5():
    lancer_combat_boufton()
    mouse.move(483,570)
    sleep(0.5)
    mouse.click(483,570)
    lance_pret()
    mouse.move(447,552)
    sleep(0.5)
    mouse.click(447,552)
    lance_sort_1()
    mouse.move(516,517)
    sleep(0.5)
    mouse.click(516,517)
    sleep(1.5)
    jouer_combat()

def combat_6():
    lancer_combat_boufton()
    mouse.move(718,443)
    sleep(0.5)
    mouse.move(718,443)
    sleep(0.5)
    mouse.click(718,443)
    lance_pret()
    jouer_combat()

def jouer_combat_7():
    mouse.click(445,588)
    sleep(1.5)
    for i in range(2):
        lancer_flamiche((442,505))
    lancer_feu((442,505))
    attendre_un_tour()
    mouse.click(421, 553)
    sleep(1.5)
    jouer_combat()


def combat_7():
    lancer_combat_bouftou()
    mouse.move(309,658)
    sleep(0.5)
    mouse.click(309,658)
    lance_pret()
    jouer_combat_7()

def jouer_combat_8():
    marcher_droite_fond()
    attendre_un_tour()
    mouse.click(481,500)
    sleep(2)
    mouse.click(481,500)
    sleep(1.5)
    jouer_combat()

def combat_8():
    lancer_combat_bouftou()
    mouse.move(208,604)
    sleep(0.5)
    mouse.click(208,604)
    lance_pret()
    jouer_combat_8()

def combat_9():
    lancer_combat_bouftou()
    mouse.move(236,408)
    sleep(0.5)
    mouse.click(236,408)
    lance_pret()
    jouer_combat()

def jouer_combat_10():
    lance_sort_1()
    lance_sort_2()
    lance_sort_3()
    mouse.click(630,909)
    sleep(1)
    for i in range(5):
        attendre_un_tour()
    mouse.click(797,863)
    click_soi()
    finis = False
    image = ImageGrab.grab()
    pixel_avant = image.getpixel((733, 709))
    while (not finis):
        pos_click = 0
        pos = trouver_mechant(couleur_br)
        for i in range(2):
            lancer_flamiche((pos[0],pos[1]))
        lancer_feu((pos[0],pos[1]))
        sleep(4)
        image = ImageGrab.grab()
        pixel = image.getpixel((733, 709))
        finis = not (pixel == pixel_avant)
        if not finis:
            attendre_un_tour()
    enleve_fin_de_combat()

def equipe_atouin():
    equipe_monture()
    mouse.click(711,803)
    sleep(0.7)
    for y in range(4):
        for x in range(4):
            x_press = 774 + 40 * x
            y_press = 429 + 40 * y
            mouse.click(x_press,y_press)
            sleep(1)
            image = ImageGrab.grab()
            if image.getpixel((387,651)) == (74, 64, 36):
                mouse.click(x_press,y_press)
                mouse.click(x_press,y_press)
                sleep(0.5)
                mouse.click(932,265)
                sleep(0.5)
                return

def combat_10():
    equipe_atouin()
    lancer_combat_bouftou()
    sleep(0.8)
    lance_pret()
    sleep(8)
    jouer_combat_10()

def equipe_pierre():
    mouse.click(711,803)
    sleep(0.7)
    for y in range(4):
        for x in range(4):
            x_press = 774 + 40 * x
            y_press = 429 + 40 * y
            mouse.click(x_press,y_press)
            sleep(1)
            image = ImageGrab.grab()
            if image.getpixel((396,628)) == (164,154,186):
                mouse.press(x_press,y_press)
                mouse.release(611,334)
                sleep(0.5)
                mouse.click(932,265)
                sleep(0.5)
                return

def equipe_monture():
    mouse.click(896,808)
    sleep(0.7)
    mouse.click(552,630)
    sleep(0.4)
    mouse.click(927,413)

def sortir():
    mouse.click(579, 465)
    sleep(1)
    mouse.click(589,475)
    sleep(1)
    mouse.click(89, 537)
    sleep(1)

def rentrer():
    mouse.click(614, 419)
    sleep(1)
    mouse.click(624,429)
    sleep(1)
    mouse.click(151, 600)
    sleep(1)

def go_bonta():
    mouse.click(872, 898)
    sleep(0.1)
    mouse.click(872, 898)
    sleep(1)

def prendre_zappi():
    mouse.click(471, 467)
    sleep(1)
    mouse.click(523, 504)
    sleep(1)
    mouse.click(376, 319)
    sleep(1)
    mouse.click(317, 475)
    sleep(1)

def parcours_banque(pixel):
    pixel_bis = (0,0,0)
    while (pixel!=pixel_bis):
        mouse.click(730, 453)
        sleep(0.8)
        image = ImageGrab.grab()
        pixel_bis = image.getpixel((520, 496))
        sleep(1)
        if pixel == pixel_bis:
            return
        sleep(0.5)
        mouse.press(730, 453)
        sleep(0.5)
        mouse.release(44, 451)
        sleep(0.5)
        mouse.click(70, 441)
        sleep(0.5)
        mouse.click(205, 441)
        sleep(1)

def vide_banque():
    for i in range(3):
        click_x = 844 + i * 30
        mouse.click(click_x, 375)
        image = ImageGrab.grab()
        pixel = image.getpixel((520, 496))
        parcours_banque(pixel)
    mouse.click(844,375)
    sleep(0.5)
    mouse.click(45, 444)
    sleep(0.5)
    mouse.press(45, 444)
    sleep(0.5)
    mouse.release(732, 447)
    sleep(0.5)
    mouse.click(588, 434)
    sleep(0.5)
    mouse.click(715, 436)
    sleep(1)

    mouse.click(154,378)
    sleep(0.5)
    mouse.press(45, 444)
    sleep(0.5)
    mouse.release(732, 447)
    sleep(0.5)
    mouse.click(588, 434)
    sleep(0.5)
    mouse.click(715, 436)
    sleep(1)

    mouse.click(929, 344)
    sleep(1)

def banque():
    mouse.click(505, 414)
    sleep(6)
    mouse.click(483, 464)
    sleep(1)
    mouse.click(511, 467)
    sleep(1)
    mouse.click(221, 536)
    sleep(1)
    vide_banque()

def retourner_donjon():
    mouse.click(909, 901)
    sleep(0.1)
    mouse.click(909, 901)
    sleep(1)
    mouse.click(927, 446)
    sleep(4)
    mouse.click(511, 236)
    sleep(4)
    mouse.click(309, 236)
    sleep(7)



if __name__=='__main__':
    while True:
        for i in range(3):
            rentrer()
            equipe_pierre()
            equipe_monture()
            combat_1()
            combat_2()
            combat_3()
            combat_4()
            combat_5()
            combat_6()
            combat_7()
            combat_8()
            combat_9()
            assoir()
            while besoin_repos():
                repos()
            combat_10()
            if i!=3:
                assoir()
                while besoin_repos():
                    repos()
            sortir()
        go_bonta()
        prendre_zappi()
        banque()
        retourner_donjon()