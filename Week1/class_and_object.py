class PartyAnimal:
    _x = 0
    _name = ""

    def __init__(self,name):
        _name = name

    def party(self):
        self._x = self._x + 1
        print("So far", self._x)


an = PartyAnimal("Sully")

an.party()




# Type of the object
print("Type", type(an))

# It shows all the methods and attributes of a class
print("Dir", dir(an))
