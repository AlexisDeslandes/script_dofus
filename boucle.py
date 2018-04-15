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
