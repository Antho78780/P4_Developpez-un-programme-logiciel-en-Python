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
    def get_players_tournaments_database(get_players_database):
        print("Joueurs enregistré dans la base de donnée: ")
        get_players_database()
        print("Ajouter 8 joueurs: ")

    @staticmethod
    def prompt_add_player(query, players, add_player, menu1=None, menu2=None, menu3=None, menu4=None):
        player = query()
        for i in range(1, 9):
            first_name = input(f"Entrez le prenom du joueur{i}: ")
            name = input(f"Entrez le nom du joueur{i}: ")
            recupFirst_name = players.search(player.prenom == first_name)
            name = players.search(player.nom == name)
            if recupFirst_name and name:
                print(f"Joueur{i} ajouté")
                print(f"{i}/8")
                for rF in recupFirst_name:
                    add_player.append(rF)
            else:
                print("Joueur introuvable")
                View.menu_tournament(menu1, menu2, menu3, menu4)

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
    def menu_tournament(menu1, menu2, menu3, menu4,):
        print("MENU TOURNOI")
        print("1: Créer un tournoi")
        print("2: Accéder au tournoi")
        print("3: Voir les informations des tournois")
        print("4: Retour")
        question = int(input("Saisisez 1, 2, 3, 4: "))
        if question == 1:
            menu1()
        elif question == 2:
            menu2()
        elif question == 3:
            menu3()
        elif question == 4:
            menu4()
        else:
            print("Informations incorrect")
            View.menu_tournament(menu1, menu2, menu3, menu4)


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
        print("Il n'y a pas de tournois dans la base de donnée")

    @staticmethod
    def return_menu(menu, choice_menu):
        question = input("Retourner au menu: y/n ")
        if question == "y" or question == "Y":
            menu()
        elif question == "n" or question == "N":
            choice_menu()
        else:
            print("Informations incorrect")
            View.return_menu(menu)

    @staticmethod
    def phrasing_len_players(players_table_all):
        if len(players_table_all()) == 8:
            print(f"Il y a {len(players_table_all())} joueurs qui peuvent participer au tournoi")
        elif len(players_table_all()) < 8:
            print(f"Il n'y a que {len(players_table_all())} joueurs")
            print("Il n'y a pas assez de joueurs pour participer a un tournoi")
        else:
            print(f"Il y a que {len(players_table_all())} joueurs maximums qui peuvent participer à un tournoi")

    @staticmethod
    def prompt_round():
        round = input("Entrez le nom du round: ")
        return round

    @staticmethod
    def prompt_phrasing_name_tournament():
        tournament = input("Tapez le nom du tournoi: ")
        return tournament



    @staticmethod
    def prompt_heure_start_round():
        heure_start = input("Entrez l'heure du début du round: ")
        return heure_start


    @staticmethod
    def prompt_date_start_round():
        date_start = input("Entrez la date de début du round: ")
        return date_start

    @staticmethod
    def prompt_heure_end_round():
        heure_end = input("Entrez l'heure de fin du round: ")
        return heure_end

    @staticmethod
    def prompt_date_end_round():
        date_end = input("Entrez la date de fin du round: ")
        return date_end

    @staticmethod
    def prompt_nRound():
        print("Créer le round")
        nRound = int(input("Tapez le n° du round: "))
        return nRound

    @staticmethod
    def printNRound(number_round):
        if number_round == 0:
            print("Il n'y a pas de round créer")

        elif number_round == 1:
            print("Il y a deja un round qui a été créer")
        else:
            print("Il y a deja plusieurs rounds qui ont été créer")
















