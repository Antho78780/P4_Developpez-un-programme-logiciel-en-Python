from controller import Controller
from models import Players
from models import Tournaments
from models import Rounds
from view import View
from tinydb import TinyDB
from tinydb import Query


controller = Controller(Players, Tournaments, Rounds, View, TinyDB, Query)
controller.run()


