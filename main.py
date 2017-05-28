class Club:
    def __init__(self, name, country):
        self.name = name
        self.country = country

class Country:
    def __init__(self, name):
        self.name = name

class Position:
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, name, surname, age, country):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country

    def get_full_name(self):
        return '%s %s' % (self.name, self.surname)

class Player(Person):
    def __init__(self, name, surname, age, country, club, main_position, positions, skills):
        Person.__init__(self, name, surname, age, country)
        self.club = club
        self.main_position = main_position
        self.positions = positions
        self.skills = skills


n = Player('Leonardo', 'Bonucci', 29, 
           Country('Italy'), 
           Club('FC Juventus', 'Italy'), 
           Position('CB'),
           [Position('CB'), Position('RB')],
           {'speed': 91}
          )


print(n.__dict__)
