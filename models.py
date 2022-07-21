class Players:
    """Modèle représentant les joueurs"""

    def __init__(self, first_name, name, date_birth, sex, ranking):
        """Initialise les détails relatifs au joueur"""
        self.first_name = first_name
        self.name = name
        self.date_birth = date_birth
        self.sex = sex
        self.ranking = ranking
        self.score = 0.0

    def __str__(self):
        player_presentation = f"prenom: {self.first_name}, nom: {self.name}, date_de_naissance: {self.date_birth}," \
                              f" sexe: {self.sex}, classement: {self.ranking}, score: {self.score}"
        return player_presentation


class Tournaments:
    """Modèle représentant le tournoi"""
    def __init__(self, name, lieu, date, time, number_round=4):
        """Initialise les détails relatifs au tournoi"""
        self.name = name
        self.lieu = lieu
        self.date = date
        self.time = time
        self.number_round = number_round
        self.add_player = []
        self.description = ""

    def __str__(self):
        tournament_presentation = f"nom: {self.name}, lieu: {self.lieu}, date: {self.date}, temps: {self.time}," \
                                  f" players: {self.add_player}"
        return tournament_presentation


class Rounds:
    def __init__(self, name, start_round, end_round):
        self.name = name
        self.start_round = start_round
        self.end_round = end_round



