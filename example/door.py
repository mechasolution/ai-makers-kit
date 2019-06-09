class Door:
    total_open_count = 0

    def __init__(self, location, color, is_locked, is_open):
        self.location = location
        self.color = color
        self.is_locked = is_locked
        self.is_open = is_open
        print("인스턴스가 초기화 되었습니다!")

    def open(self):
        print("%s 문을 엽니다" % self.location)
        self.is_open = True
        Door.total_open_count = Door.total_open_count + 1

    def close(self):
        print("%s 문을 닫습니다" % self.location)
        self.is_open = False

    def lock(self):
        print("%s 문을 잠금니다" % self.location)
        self.is_locked = True

    def unlock(self):
        print("%s 문을 잠금 해제합니다" % self.location)
        self.is_locked = False

    def set_location(self, location):
        if location == "산속":
            return
        self.location = location

    def set_color(self, color):
        if color == "transparent":
            return
        self.color = color

    def get_location(self):
        if self.location == None:
            return "모름"
        return self.location


door1 = Door('부엌', 'Red', False, False)
door2 = Door('거실', 'White', True, False)

door1.open()

door2.open()
door2.close()
door2.open()

print('문들이 열린 횟수:', Door.total_open_count)

class Person:
    def __init__(self, name, age, address):
        self.name = name        # 이름
        self.age = age          # 나이
        self.address = address  # 주소

    def introduce(self):
        print('안녕하세요, 제 이름은 %s이고,' % self.name)
        print('나이는 %d세, %s에서 살고 있습니다.' % (self.age, self.address))

class Student(Person):
    def __init__(self, name, age, address, grade):
        super().__init__(name, age, address)
        self.grade = grade      # 학년

    def introduce(self):
        super().introduce()
        print('저는 %d 학년입니다.' % self.grade)


class Teacher(Person):
    def __init__(self, name, age, address, subject):
        super().__init__(name, age, address)
        self.subject = subject  # 담당 과목

    def introduce(self):
        super().introduce()
        print('제 담당과목은 %s입니다.' % self.subject)

class Parent(Person):
    def __init__(self, name, age, address, child):
        super().__init__(name, age, address)
        self.child = child      # 자식 인스턴스

    def introduce(self):
        super().introduce()
        print('제 자식은 %s 입니다.' % self.child)

t = Teacher("홍길동", 34, "대구광역시 달서구", "컴퓨터 과학")
t.introduce()