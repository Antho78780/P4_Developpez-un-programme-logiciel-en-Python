from controller import Controller
from models import Players
from models import Tournaments
from view import View
from tinydb import TinyDB
from tinydb import Query


controller = Controller(Players, Tournaments, View, TinyDB, Query)
controller.run()


