class Nobody():
    def __init__(self, name):
        """принимает параметр str и сохраняяет его как атрибут класса, если он равен 'Nobody', ежели нет,
         то в атрибут класса сохраняет другую написанную строку"""
        if name.lower() == 'nobody':
            self.name = name
        else:
            self.name = "I'm not nobody, " + " " + str(name)
people = Nobody('Nobody')
print(people.name)
