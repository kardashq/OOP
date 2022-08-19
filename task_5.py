class Person():
    def __init__(self, name, surname, age):
        """Конструктор класса, делающий значения приватными"""
        self.__name = name
        self.__surname = surname
        self.__age = age

    """Делаю возможность чтения приватных значений"""
    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        """Делаю возможность изменять приватное значение, но с условием не более чем на 1"""
        if (value - self.age > 1):
            print(f'Нельзя так изменять, значение остается: {self.age}')
            return

        self.__age = value

    @property
    def full_name(self):
        """Cвойство, возвращающее строку имя + фамилия"""
        return print(f'full name: {self.__name} {self.__surname}')

person = Person('Sergey', 'Kardash', 26)
person.full_name
print(person.age)
person.age +=1
print(person.age)
print('Проверка ошибки при изменении "age" более чем на 1: ')
person.age+=2