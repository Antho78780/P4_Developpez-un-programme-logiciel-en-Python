class Controller:
    def __init__(self, Players, Tournaments, View, Tinydb, Query):
        # Models
        self.players = Players
        self.tournaments = Tournaments
        # View
        self.view = View

        # DATABASE
        self.tinydb = Tinydb
        self.Query = Query
        self.db = self.tinydb("db.json")
        self.players_table = self.db.table("players")
        self.tournaments_table = self.db.table("tournaments")

    def create_tournament(self):
        tournaments = self.tournaments(
            self.view.prompt_name_tournament(self.menu_tournament),
            self.view.prompt_lieu_tournament(self.menu_tournament),
            self.view.prompt_date_tournament(self.menu_tournament),
            self.view.prompt_time_tournament(self.menu_tournament),
        )
        self.view.prompt_add_player_tournament(self.get_players_tournament_database, tournaments.add_player)
        serialized_tournament = {
            "nom": tournaments.name,
            "lieu": tournaments.lieu,
            "date": tournaments.date,
            "temps": tournaments.time,
            "joueurs": tournaments.add_player
        }
        print(serialized_tournament)
        self.tournaments_table.insert(serialized_tournament)
        self.view.phrasing_create_tournament()
        self.return_menu()

    def prompt_player(self):
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

    def get_players_database(self):
        if self.players_table.all() == []:
            self.view.phrasing_none_players()
            self.return_menu()
        else:
            for player in self.players_table.all():
                first_name = player["prenom"]
                name = player["nom"]
                date_birth = player["date_de_naissance"]
                sex = player["sexe"]
                ranking = player["classement"]
                player = self.players(first_name=first_name, name=name, date_birth=date_birth, sex=sex, ranking=ranking)
                print(player)
            self.return_menu()

    def get_tournaments_database(self):
        if self.tournaments_table.all() == []:
            self.view.phrasing_none_tournaments()
            self.return_menu()
        else:
            for tournament in self.tournaments_table.all():
                name = tournament["nom"]
                lieu = tournament["lieu"]
                date = tournament["date"]
                time = tournament["temps"]
                add_player = tournament["joueurs"]
                tournament = self.tournaments(name=name, lieu=lieu, date=date, time=time, add_player=add_player)
                print(tournament)
            self.return_menu()

    def get_players_tournament_database(self):
        if not self.players_table.all() == []:
            self.view.phrasing_len_players(self.players_table.all)
            print(self.players_table.all())
        else:
            self.return_menu()

    def return_menu(self):
        self.view.return_menu(self.menu)

    def menu_player(self):
        self.view.menu_player(self.prompt_player, self.get_players_database, self.menu)

    def menu_tournament(self):
        self.view.menu_tournament(self.create_tournament, self.get_tournaments_database, self.menu)

    def menu(self):
        self.view.menu(self.menu_player, self.menu_tournament)

    def run(self):
        self.menu()
