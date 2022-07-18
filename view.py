import re


class View:
    @staticmethod
    def prompt_userName_player(menu_player):
        first_name = input("Saisisez le prenom du joueur: ")
        pattern1 = "^[A-Za-z]+$"
        if re.match(pattern1, first_name):
            return first_name
        else:
            print("Information incorrect, recommencer")
            menu_player()

    @staticmethod
    def prompt_name_player(menu_player):
        name = input("Saisisez le nom du joueur: ")
        pattern1 = "^[A-Za-z]+$"
        if re.match(pattern1, name):
            return name
        else:
            print("Information incorrect, recommencer")
            menu_player()

    @staticmethod
    def prompt_dateBirth_player(menu_player):
        date_birth = input("Saisisez la date de naissance du joueur: ")
        pattern1 = "^[0-9-/]+$"
        if re.match(pattern1, date_birth):
            return date_birth
        else:
            print("Information incorrect, recommencer")
            menu_player()

    @staticmethod
    def prompt_sex_player(menu_player):
        sex = input("Saisisez la civilité du joueur: ")
        pattern1 = "^[e-oE-O]+$"
        if re.match(pattern1, sex):
            return sex
        else:
            print("Information incorrect, recommencer")
            menu_player()


    @staticmethod
    def prompt_ranking_player():
        ranking = int(input("Saisisez le classement du joueur: "))
        if ranking == 0:
            return ranking
        else:
            return ranking

    @staticmethod
    def prompt_name_tournament(menu_player):
        name = input("Saisisez le nom du tournoi: ")
        pattern1 = "^[A-Za-z-0-9]+$"
        if re.match(pattern1, name):
            return name
        else:
            print("Information incorrect, recommencer")
            menu_player()

    @staticmethod
    def prompt_lieu_tournament(menu_player):
        lieu = input("Saisisez le lieu du tournoi: ")
        pattern1 = "^[A-Za-z-0-9]+$"
        if re.match(pattern1, lieu):
            return lieu
        else:
            print("Information incorrect, recommencer")
            menu_player()

    @staticmethod
    def prompt_date_tournament(menu_player):
        date = input("Saisisez la date du tournoi: ")
        pattern1 = "^[0-9-/]+$"
        if re.match(pattern1, date):
            return date
        else:
            print("Information incorrect, recommencer")
            menu_player()

    @staticmethod
    def prompt_add_player_tournament(get_players_tournament_database, tournaments_add_player):
        print("Joueurs enregistré dans la base de donnée: ")
        get_players_tournament_database()
        print("Ajouter 8 joueurs")
        for i in range(1, 3):
            indice_player = int(input("Saisisez l'indice du joueur à 'ajouter au tournoi: "))
            print("Joueur", i, "ajouté")
            print(str(i)+"/2")
            players = "Joueur" + str(i)
            tournaments_add_player.append(players)
        return tournaments_add_player


    @staticmethod
    def prompt_time_tournament(menu_player):
        time = input("Saisisez le temps du tournoi(bullet, blitz, coup-rapide): ")
        if time == "bullet":
            return time
        elif time == "blitz":
            return time
        elif time == "coup-rapide":
            return time
        else:
            print("Information incorrect, recommencer")
            menu_player()

    @staticmethod
    def menu(menu1, menu2):
        print("MENU PRINCIPAL")
        print("1: Inscription joueurs")
        print("2: Tournois")
        print("3: Quitter")
        question = int(input("Saisisez 1, 2, 3: "))
        if question == 1:
            menu1()
        elif question == 2:
            menu2()
        elif question == 3:
            exit()
        else:
            print("Information incorrect")
            View.menu(menu1, menu2)

    @staticmethod
    def menu_player(menu1, menu2, menu3):
        print("MENU JOUEURS")
        print("1: Ajout d'un joueur")
        print("2: Joueurs dans la base de donnée")
        print("3: Retour")
        question = int(input("Saisisez 1, 2, 3: "))
        if question == 1:
            menu1()
        elif question == 2:
            menu2()
        elif question == 3:
            menu3()
        else:
            print("Information incorrect")
            View.menu_player(menu1, menu2, menu3)

    @staticmethod
    def menu_tournament(menu1, menu2, menu3):
        print("MENU TOURNOI")
        print("1: Créer un tournoi")
        print("2: Voir tout les tournois")
        print("3: Retour")
        question = int(input("Saisisez 1 ou 2: "))
        if question == 1:
            menu1()
        elif question == 2:
            menu2()
        elif question == 3:
            menu3()
        else:
            print("Informations incorrect")
            View.menu_tournament(menu1, menu2, menu3)


    @staticmethod
    def phrasing_create_tournament():
        print("Tournoi créer")

    @staticmethod
    def phrasing_create_player():
        print("Joueur créer")

    @staticmethod
    def phrasing_none_players():
        print("Aucun joueurs dans la base de données")

    @staticmethod
    def phrasing_none_tournaments():
        print("Aucun tournois dans la base de données")

    @staticmethod
    def return_menu(menu):
        question = input("Retourner au menu: y ")
        if question == "y":
            menu()
        else:
            print("Informations incorrect")
            View.return_menu(menu)

    @staticmethod
    def phrasing_len_players(players_table_all):
        print("Il y a", len(players_table_all()), "joueurs qui peuvent participer au tournoi")








