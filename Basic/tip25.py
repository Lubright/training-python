# namedtuple

students = [
    (1, "Amy", 90),
    (2, "Benny", 85),
    (3, "Cindy", 95)
]

for student in students:
    print( "id={}; name={}, score={:.2f}".format(*student) ) # 使用解構
    # 但有缺點，不能隨意調換位置，而且只能用 index 去存取，影響可讀性

print("-" * 50 + "\n")

from collections import namedtuple

Student = namedtuple("Student", "id, name, score")

students = [
    Student(1, "Amy", 90),
    Student(2, "Benny", 85),
    Student(3, "Cindy", 95)
]

print(students, type(students[0]))

# traverse

for student in students:
    print( "id={}; name={}, score={:.2f}".format(student.id, student.name, student.score) )
    print( "id={}; name={}, score={:.2f}".format(student[0], student.name, student.score) ) 
    # namedtuple 還保有原本 tuple 的特性，可以使用 index 去存取

print("-" * 50 + "\n")
