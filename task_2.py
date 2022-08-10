highest_scholarship_st = 500
lower_scholarship_st = 150
highest_scholarship_as = 700
lower_scholarship_as = 250
class Student():
    def __init__(self, first_name: str, last_name: str, group: str, marks: list):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.marks = marks
    def __str__(self):
        """Приведение к строке"""
        return f"Студент {self.first_name} {self.last_name} обучается в группе {self.group}"

    def add_mark(self, mark):
        """Принимает оценки студента/аспиранта, проверяя их на соответствие условию"""
        if 0 <= mark <= 10:
            self.marks.append(mark)
            print('Добавлена оценка:', mark)
        else:
            print('Неверная оценка, ничего не добавлено')
    def get_average_mark(self):
        """Принимает список оценок и возвращает средний балл"""
        return sum(self.marks)/len(self.marks)
    def get_scolarship(self):
        """Возвращает размер стипендии исходя из среднего балла"""
        return highest_scholarship_st if self.get_average_mark() >= 5 else lower_scholarship_st

class Aspirant(Student):

    def __init__(self, first_name: str, last_name: str, group: str, marks: list, scientific_publications: list):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.marks = marks
        self.scientific_publication = scientific_publications
    def __str__(self):
        """Приведение к строке"""
        return f"Аспирант {self.first_name} {self.last_name} обучается в группе {self.group} и имеет научные работы:\n{self.scientific_publication}"
    def get_scolarship(self):
        """Возвращает размер стипендии исходя из среднего балла"""
        return highest_scholarship_as if self.get_average_mark() >= 5 else lower_scholarship_as



me = Student('Sergey', 'Kardash', 'z28-Onl', [1, 10])
aspirant = Aspirant('Alex', 'Ivanov', 'z28-off', [8,8,8], ['test publication 1, test publication 2' ])
print(me)
me.add_mark(1)
print('Оценки студента: ', me.marks)
print('Стипендия студента: ', me.get_scolarship())
print('Средний балл: ', me.get_average_mark())
print(aspirant)
aspirant.add_mark(13)
print('Оценки аспиранта: ', aspirant.marks)
print('Стипендия аспиранта: ', aspirant.get_scolarship())
print('Средний балл: ', aspirant.get_average_mark())
