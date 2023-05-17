class Courses(object):
    def __init__(self):
        self.course_students = {}
 
    def subscribe(self, subs, subject):
        if subject in self.course_students:
            self.course_students[subject].append(subs)    
        else :
            self.course_students[subject] = [subs]

        print('Subscribing: %s to subject: %s ' % (subs.name, subject))


    def unsubscribe(self, subs, subject):
        if subject in self.course_students:
            self.course_students[subject].remove(subs)    

        print('UnSubscribing: %s to subject: %s ' % (subs.name, subject))

 
    def notify(self, data, subject):
        if subject not in self.course_students:
            return
 
        print('Publishing: %s for subject %s ' %(data, subject))
        for student in self.course_students[subject]:
            student.update('%s for subject %s ' %(data, subject))


class Student(object):
    def __init__(self, name):
        self.name = name
 
    def update(self, data):
        print('Student %s got :: %s'%(self.name, data))

# Client code.
courses = Courses()
john = Student('John')
eric = Student('Eric')
jack = Student('Jack')
print()
courses.subscribe(john, 'English')
courses.subscribe(eric, 'English')
courses.subscribe(eric, 'Maths')
courses.subscribe(jack, 'Science')
print()
courses.notify('Tomarrow class at 11', 'English')
print()
courses.notify('Tomarrow class at 1', 'Maths')

"""
Subscribing: John to subject: English 
Subscribing: Eric to subject: English 
Subscribing: Eric to subject: Maths 
Subscribing: Jack to subject: Science 

Publishing: Tomarrow class at 11 for subject English 
Student John got :: Tomarrow class at 11 for subject English 
Student Eric got :: Tomarrow class at 11 for subject English 

Publishing: Tomarrow class at 1 for subject Maths 
Student Eric got :: Tomarrow class at 1 for subject Maths 
"""