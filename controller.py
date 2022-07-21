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
        self.view.get_players_tournaments_database(self.get_players_tournament_database)
        self.view.prompt_add_player(self.Query, self.players_table, tournaments.add_player)
        serialized_tournament = {
            "nom": tournaments.name,
            "lieu": tournaments.lieu,
            "date": tournaments.date,
            "temps": tournaments.time,
            "joueurs": tournaments.add_player
        }
        self.tournaments_table.insert(serialized_tournament)
        self.view.phrasing_create_tournament()
        self.return_menu()

    """Ajout de joueur"""
    def add_player(self):
        players = self.players(
            self.view.prompt_userName_player(self.menu_player),
            self.view.prompt_name_player(self.menu_player),
            self.view.prompt_dateBirth_player(self.menu_player),
            self.view.prompt_sex_player(self.menu_player),
            self.view.prompt_ranking_player()
        )
        player_serialized = {
            "prenom": players.first_name,
            "nom": players.name,
            "date_de_naissance": players.date_birth,
            "sexe": players.sex,
            "classement": players.ranking
        }
        self.players_table.insert(player_serialized)
        self.view.phrasing_create_player()
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
                                      date_birth= player["date_de_naissance"],
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
                print(tournament)
                self.return_menu()

    """Information des joueurs qui sont dans la base des donnée dans les tournois"""
    def get_players_tournament_database(self):
        if len(self.players_table.all()) >= 8:
            for player in self.players_table.all():
                print(player)
            self.view.phrasing_len_players(self.players_table.all)
        else:
            self.view.phrasing_none_players_tournament(self.players_table.all)
            self.return_menu()

    def add_players_round(self):
        print("Les joueurs qui sonts au tournoi: ")

        for tournament in self.tournaments_table.all():
            for tr in tournament["joueurs"]:
                tr.pop("date_de_naissance")
                tr.pop("sexe")

            sup_moitie = tournament["joueurs"][4:]
            print(sup_moitie)
            inf_moitie = tournament["joueurs"][:4]
            print(inf_moitie)

            """
            match1 = (sup_moitie[0]["prenom"], inf_moitie[0]["prenom"])
            match2 = (sup_moitie[1]["prenom"], inf_moitie[1]["prenom"])
            match3 = (sup_moitie[2]["prenom"], inf_moitie[2]["prenom"])
            match4 = (sup_moitie[3]["prenom"], inf_moitie[3]["prenom"])
            round1 = [match1, match2, match3, match4]
            print(round1)
            """

    """Retour au menu"""
    def return_menu(self):
        self.view.return_menu(self.menu)

    """Visualisation du menu player"""
    def menu_player(self):
        self.view.menu_player(self.add_player, self.get_players_database, self.menu)

    """Visualisation du menu Tournoi"""
    def menu_tournament(self):
        self.view.menu_tournament(self.create_tournament, self.add_players_round, self.get_tournaments_database, self.menu)

    """Visualisation du menu général"""
    def menu(self):
        self.view.menu(self.menu_player, self.menu_tournament)

    """Lancer le code"""
    def run(self):
        self.menu()
