class MyString():
    def __init__(self, value):
        self.value = str(value)
        """Создаю магические методы операторов сравнения '<,>,==,<=,>=',
        которые при вызове сравниют длину строк экзэмпляров класса MyString"""
    def __eq__(self, other):
        print(f"строка '{self.value}' равна строке '{other.value}':")
        return len(self.value) == len(other.value)
    def __lt__(self, other):
        print(f"строка '{self.value}' < строки '{other.value}':")
        return len(self.value) < len(other.value)
    def __gt__(self, other):
        print(f"строка '{self.value}' > строки '{other.value}':")
        return len(self.value) > len(other.value)
    def __le__(self, other):
        print(f"строка '{self.value}' <= строки '{other.value}':")
        return len(self.value) <= len(other.value)
    def __ge__(self,other):
        print(f"строка '{self.value}' >= строки '{other.value}':")
        return len(self.value) >= len(other.value)


st1 = MyString('Привет')
st2 = MyString('Пока')

res = st1 == st2
print(res)
