class Courses(object):
    def __init__(self):
        self.courseStudents = {}
 
    def subscribe(self, subs, subject):
        if subject in self.courseStudents:
            self.courseStudents[subject].append(subs)    
        else :
            self.courseStudents[subject] = [subs]

        print('Subscribing: %s to subject: %s ' % (subs.name, subject))


    def unSubscribe(self, subs, subject):
        if subject in self.courseStudents:
            self.courseStudents[subject].remove(subs)    

        print('UnSubscribing: %s to subject: %s ' % (subs.name, subject))

 
    def notify(self, data, subject):
        if subject not in self.courseStudents:
            return
 
        print('Publishing: %s for subject %s ' %(data, subject))
        for Student in self.courseStudents[subject]:
            Student.update('%s for subject %s ' %(data, subject))


class Student(object):
    def __init__(self, name):
        self.name = name
 
    def update(self, data):
        print('Student %s got :: %s'%(self.name, data))


if __name__ == '__main__':
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



