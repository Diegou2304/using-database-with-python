class PartyAnimal:
    _x = 0
    _name = ""

    def __init__(self, name):
        _name = name

    def party(self):
        self._x = self._x + 1
        print("So far", self._x)


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 1
        self.party()
        print(self._name, "points", self.points)
