class Courses(object):
    def __init__(self):
        self._course_students = {}

    def subscribe(self, subject, student):
        if subject not in self._course_students:
            self._course_students[subject] = set()
        self._course_students[subject].add(student)

    def unsubscribe(self, subject, student):
        if subject in self._course_students:
            self._course_students[subject].discard(student)

    def publish(self, subject, message):
        if subject not in self._course_students:
            print(f"No subscribers for subject '{subject}'.")
            return
        for student in self._course_students[subject]:
            student.notify(subject, message)


class Student(object):
    def __init__(self, name):
        self.name = name

    def notify(self, subject, message):
        print(f"{self.name} received message on subject '{subject}': {message}")


# Client code.
courses = Courses()
john = Student('John')
eric = Student('Eric')
jack = Student('Jack')

courses.subscribe('English', john)
courses.subscribe('English', eric)
courses.subscribe('Maths', eric)
courses.subscribe('Science', jack)

courses.publish('English', 'Tomorrow class at 11')
courses.publish('Maths', 'Tomorrow class at 1')

# Unsubscribe Eric from English
courses.unsubscribe('English', eric)

courses.publish('English', 'Updated schedule for English')

"""
Eric received message on subject 'English': Tomorrow class at 11
John received message on subject 'English': Tomorrow class at 11
Eric received message on subject 'Maths': Tomorrow class at 1
John received message on subject 'English': Updated schedule for English
"""