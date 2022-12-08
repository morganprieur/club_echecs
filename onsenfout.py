
from abc import ABC, abstractmethod
from dataclasses import dataclass


class DbInterface(ABC):
    @abstractmethod
    def __setitem__(self, key, value):
        """Define the method to store in the database"""
        pass

    @abstractmethod
    def __getitem__(self, key):
        """Define the method to get data from the database"""
        pass


class AbstractModel(ABC):
    db: DbInterface = None

    @classmethod
    def init_db(cls, db):
        cls.db = db

    def __init__(self):
        self._class_name = self.__class__.__name__

    @property
    def cname(self):
        return self._class_name

    def to_dict(self, exclude=None):
        exclude = exclude or []
        return {
            key: getattr(self, key)
            for key in dir(self)
            if not key.startswith("_")
            and key not in exclude
            and not callable(getattr(self, key))
            and isinstance(getattr(self, key), (str, int, float))
        }

    def __str__(self):
        build_str = [f"{key}: {value}" for key, value in self.to_dict().items()]
        return ",".join(build_str)

    @abstractmethod
    def serialize(self):
        """Abstract method which must be overridden"""
        pass


@dataclass
class School(AbstractModel):
    name: str
    address: str = None
    all_students: list = None
    classes: list = None

    def __post_init__(self):
        super().__init__()
        self.all_students = []
        self.classes = []

    def serialize(self):
        assert self.db
        self.db[f"{self.cname}_{self.name}"] = self.to_dict()

    def add_student(self, student):
        student.school = self
        self.all_students.append(student)

    def add_classe(self, classe):
        self.classes.append(classe)

    def new_class(self, name: str, level: int):
        new_class = Classe(self, name=name, level=level)
        self.classes.append(new_class)


@dataclass
class Classe(AbstractModel):
    school: School
    name: str
    level: int
    students: list = None

    def __post_init__(self):
        super().__init__()
        self.students = []

    def serialize(self):
        try:
            self.db[f"classe_{self.name}"] = self.to_dict()
        except TypeError:
            raise TypeError(
                f"The dabase must be defined before being able to serialize. ({self.db})"
            )

    def add_student(self, student):
        student.classe = self
        self.students.append(student)
        self.school.add_student(student)


class Student2(AbstractModel):

    def __init__(self, first_name: str, last_name: str, age: list, school: School = None, classe: Classe = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.school = school
        self.classe = classe
        super().__init__()


@dataclass
class Student(AbstractModel):
    first_name: str
    last_name: str
    age: list
    school: School = None
    classe: Classe = None

    def __post_init__(self):
        super().__init__()

    def __str__(self):
        value_str = super().__str__()
        if self.classe:
            value_str = f"{value_str}, classe: {self.classe.name}"
        if self.school:
            value_str = f"{value_str}, school: {self.school.name}"
        return value_str

    def serialize(self):
        assert self.db
        self.db[f"classe_{self.name}"] = self.to_dict()


if __name__ == "__main__":
    AbstractModel.db = {}
    my_school = School("Big school")
    print(my_school)
    my_school.new_class("6e 01", 6)
    my_class = Classe(my_school, "5e B1", 5)
    my_school.add_classe(my_class)
    for classe in my_school.classes:
        print(classe)
    student1 = Student("bob", "Student", 11)
    print(student1)
    my_class.add_student(student1)
    print(student1)
    student2 = Student("jenny", "Whisley", 12)
    my_school.add_student(student2)
    print(student2) 




    data = [{1: 1}, {2: 2}]
    for i in range(len(data)):
        print(i, data[i])
    for i, _ in enumerate(data):
        print(i, _, data[i])
    for elem in data:
        print(elem)



