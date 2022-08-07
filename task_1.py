class Nobody():
    def __init__(self, name):
        if name.lower() == 'nobody':
            self.name = name
        else:
            self.name = "I'm not nobody, " + " " + str(name)
people = Nobody('Nobody')
print(people.name)
