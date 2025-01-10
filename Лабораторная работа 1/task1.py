import doctest

class Table:
    def __init__(self, height: float, width: float, length: float):
        """
        :param height: Высота стола
        :param width: Ширина стола
        :param length: Длина стола

        table = Table(1, 1.4, 1.8)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError
        if height <= 0:
            raise ValueError
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError
        if width <= 0:
            raise ValueError
        self.width = width

        if not isinstance(length, (int, float)):
            raise TypeError
        if length <= 0:
            raise ValueError
        self.length = length

    def get_volume(self) -> float:
        """
        Вычисление объема стола

        :return: Объем стола

        table = Table(1, 1.4, 1.8)
        table.get_volume()
        """
        ...

    def calculate_surface_area(self) -> float:
        """
        Вычисление площади поверхности стола

        :return: Площадь поверхности стола

        table = Table(1, 1.4, 1.8)
        table.calculate_surface_area()
        """
        ...

    def add_legs(self, number_of_legs: int) -> None:
        """
        Добавление ножек к столу
        :param number_of_legs: Количество ножек
        :raise ValueError: Если количество ножек меньше 3 или больше 4

        table = Table(1, 1.4, 1.8)
        table.add_legs(4)
        """

        if not isinstance(number_of_legs, int):
            raise TypeError
        if not (3 <= number_of_legs <= 4):
            raise ValueError
        ...

class Tree:
    def __init__(self, height: float, crown_diameter: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param height: Высота дерева
        :param crown_diameter: Диаметр кроны
        :param age: Возраст дерева

        Примеры:
        tree = Tree(13, 8, 75)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError
        if height <= 0:
            raise ValueError
        self.height = height

        if not isinstance(crown_diameter, (int, float)):
            raise TypeError
        if crown_diameter <= 0:
            raise ValueError
        self.crown_diameter = crown_diameter

        if not isinstance(age, int):
            raise TypeError
        if age <= 0:
            raise ValueError
        self.age = age

    def get_volume(self) -> float:
        """
        Вычисление объема дерева

        :return: Объем дерева

        Примеры:
        tree = Tree(13, 8, 75)
        tree.get_volume()
        """
        ...

    def calculate_leaf_area(self) -> float:
        """
        Вычисление площади листьев

        :return: Площадь листьев

        Примеры:
        tree = Tree(10, 5, 50)
        tree.calculate_leaf_area()
        """
        ...

class Student:
    def __init__(self, name: str, year_of_birth: int, year_of_study: int):
        """
        Создание и подготовка к работе объекта "Студент"

        :param name: Имя студента
        :param year_of_birth: Год рождения
        :param year_of_study: Курс обучения

        Примеры:
        >>> student = Student("Alice", 2006, 1)
        """
        if not isinstance(name, str):
            raise TypeError
        self.name = name

        if not isinstance(year_of_birth, int):
            raise TypeError
        if year_of_birth < 0:
            raise ValueError
        self.year_of_birth = year_of_birth

        if not isinstance(year_of_study, int):
            raise TypeError
        if year_of_study < 1:
            raise ValueError
        self.year_of_study = year_of_study

    def get_age(self) -> int:
        """
        Вычисление возраста студента

        :return: Возраст студента
        Примеры:
        student = Student("Alice", 2006, 1)
        student.get_age()
        """
        ...

    def get_grade(self) -> str:
        """
        Определение текущего курса обучения

        :return: Курс обучения
        Примеры:
        student = Student("Alice", 2006, 1)
        student.get_grade()
        """
        ...

    def progress_to_next_year(self) -> None:
        """
        Переход студента на следующий курс
        """
        ...

if __name__ == "__main__":
    doctest.testmod()