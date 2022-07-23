from operator import itemgetter
class Controller:
    def __init__(self, Players, Tournaments, Rounds, View, Tinydb, Query):
        # Models
        self.players = Players
        self.tournaments = Tournaments
        self.rounds = Rounds
        # View
        self.view = View

        # DATABASE
        self.tinydb = Tinydb
        self.Query = Query
        self.db = self.tinydb("db.json")
        self.players_table = self.db.table("players")
        self.tournaments_table = self.db.table("tournaments")

    """Créer un tournoi"""
    def create_tournament(self):
        tournaments = self.tournaments(
            self.view.prompt_name_tournament(self.menu_tournament),
            self.view.prompt_lieu_tournament(self.menu_tournament),
            self.view.prompt_date_tournament(self.menu_tournament),
            self.view.prompt_time_tournament(self.menu_tournament),
        )
        print(tournaments)
        self.view.get_players_tournaments_database(self.get_players_database)
        self.view.prompt_add_player(self.Query, self.players_table, tournaments.add_player)
        serialized_tournament = {
            "nom": tournaments.name,
            "lieu": tournaments.lieu,
            "date": tournaments.date,
            "temps": tournaments.time,
            "number_round": tournaments.number_round,
            "rounds": tournaments.rounds,
            "joueurs": tournaments.add_player
        }
        self.tournaments_table.insert(serialized_tournament)
        self.view.phrasing_create_tournament()
        self.return_menu()

    """Ajout de joueur"""
    def create_player(self):
        players = self.players(
            self.view.prompt_userName_player(self.menu_player),
            self.view.prompt_name_player(self.menu_player),
            self.view.prompt_dateBirth_player(self.menu_player),
            self.view.prompt_sex_player(self.menu_player),
            self.view.prompt_ranking_player()
        )
        print(players)
        player_serialized = {
            "prenom": players.first_name,
            "nom": players.name,
            "date_de_naissance": players.date_birth,
            "sexe": players.sex,
            "classement": players.ranking,
            "score": players.score
        }
        self.players_table.insert(player_serialized)
        self.view.phrasing_create_player()
        if self.return_menu() == "n" or "N":
            self.create_player()
        else:
            self.return_menu()

    """Informations des joueurs dans la base de donnée"""
    def get_players_database(self):
        if self.players_table.all() == []:
            self.view.phrasing_none_players()
            self.return_menu()
        else:
            for player in self.players_table.all():
                player = self.players(first_name=player["prenom"],
                                      name=player["nom"],
                                      date_birth=player["date_de_naissance"],
                                      sex=player["sexe"],
                                      ranking=player["classement"])

                print(player)
            self.view.phrasing_len_players(self.players_table.all)

            self.return_menu()

    """Informations des tournois dans la base de donnée"""

    def get_tournaments_database(self):
        if self.tournaments_table.all() == []:
            self.view.phrasing_none_tournaments()
            self.return_menu()
        else:
            for tournament in self.tournaments_table.all():
                tr = self.tournaments(
                    name=tournament["nom"],
                    lieu=tournament["lieu"],
                    date=tournament["date"],
                    time=tournament["temps"]
                )
                self.delete_date_birth_sex(tournament["joueurs"])
                tr.add_player = tournament["joueurs"]
                print(tr)
            self.return_menu()

    def delete_date_birth_sex(self, tournament_joueurs):
        for trt in tournament_joueurs:
            try:
                trt.pop("date_de_naissance")
                trt.pop("sexe")
            except:
                return KeyError

    def create_round(self):
        trt = self.Query()
        for tournament in self.tournaments_table.all():
            objetTr = {
                "Nom du tournoi": tournament["nom"]
            }
            print(objetTr)
        search_tournament = self.tournaments_table.search(trt.nom == self.view.prompt_phrasing_name_tournament())
        if search_tournament:
            search_tournament = self.tournaments_table.all()
            print("Vous venez d'accéder au tournoi")
            self.first_round(search_tournament)
            self.after_first_round(search_tournament)
        else:
            print("Tournoi introuvable")
            self.return_menu()

    """Trie des joueurs au premier round"""
    def first_round(self, search_tournament):
        trt = self.Query()
        self.players_table.remove(trt.score > 0.0)
        self.view.prompt_nRound()
        sup_moitie = search_tournament[0]["joueurs"][4:]
        inf_moitie = search_tournament[0]["joueurs"][:4]
        sup_moitie.sort(key=lambda x: x.get("classement"))
        inf_moitie.sort(key=lambda x: x.get("classement"))
        print("----------------classement-des-joueurs---------------------")
        self.delete_date_birth_sex(search_tournament[0]["joueurs"])
        all_Match = []
        for i in range(len(sup_moitie)):
            match = ([sup_moitie[i]["prenom"]] + [sup_moitie[i]["score"]], [inf_moitie[i]["prenom"]] + [inf_moitie[i]["score"]])
            print(match)
            all_Match.append(match)
        for Am in all_Match:
            print(Am)
            result_match_first_players = int(input(f"resultat du match pour {Am[0]}: "))
            self.players_table.update({"score": result_match_first_players}, trt.prenom == Am[0][0])
            result_match_last_players = int(input(f"resultat du match pour {Am[1]}: "))
            self.players_table.update({"score": result_match_last_players}, trt.prenom == Am[1][0])
        search_tournament[0]["joueurs"] = self.players_table.all()
        print("Round fini")

    def after_first_round(self, search_tournament):
        trt = self.Query()
        search_tournament[0]["joueurs"].sort(key=lambda x: (x.get("score"), x.get("classement")))
        print(search_tournament[0]["joueurs"])
        match1 = (
            [search_tournament[0]["joueurs"][0]["prenom"]] + [search_tournament[0]["joueurs"][0]["score"]],
            [search_tournament[0]["joueurs"][1]["prenom"]] + [search_tournament[0]["joueurs"][1]["score"]]
        )
        match2 = (
            [search_tournament[0]["joueurs"][2]["prenom"]] + [search_tournament[0]["joueurs"][2]["score"]],
            [search_tournament[0]["joueurs"][3]["prenom"]] + [search_tournament[0]["joueurs"][3]["score"]]
        )
        match3 = (
            [search_tournament[0]["joueurs"][4]["prenom"]] + [search_tournament[0]["joueurs"][4]["score"]],
            [search_tournament[0]["joueurs"][5]["prenom"]] + [search_tournament[0]["joueurs"][5]["score"]]
        )
        match4 = (
            [search_tournament[0]["joueurs"][6]["prenom"]] + [search_tournament[0]["joueurs"][6]["score"]],
            [search_tournament[0]["joueurs"][7]["prenom"]] + [search_tournament[0]["joueurs"][7]["score"]]
        )
        print(match1)
        print(match2)
        print(match3)
        print(match4)
        for i in match1, match2, match3, match4:
            result_match_first_players = int(input(f"resultat du match pour {i[0][0]}: "))
            self.players_table.update({"score": result_match_first_players}, trt.prenom == i[0][0])
        print(self.players_table.all())


    """Retour au menu"""
    def return_menu(self):
        self.view.return_menu(self.menu)

    """Visualisation du menu player"""
    def menu_player(self):
        self.view.menu_player(self.create_player, self.get_players_database, self.menu)

    """Visualisation du menu Tournoi"""
    def menu_tournament(self):
        self.view.menu_tournament(self.create_tournament, self.create_round, self.get_tournaments_database,
                                  self.menu)

    """Visualisation du menu général"""
    def menu(self):
        self.view.menu(self.menu_player, self.menu_tournament)

    """Lancer le code"""
    def run(self):
        self.menu()
