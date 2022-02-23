class Person():

    #Constructor
    def __init__(self,fname,lname): 

        #First and last name instances
        self.fname = fname 
        self.lname = lname 


    #Method gettin the full name
    def getName(self):

        #Construct and return name string
        return " ".join((self.fname,self.lname))
    
    
class Teacher(Person):
    
    def __init__(self,fname,lname,course):
        
        self.course = course
        
        super().__init__(fname,lname)
        
    def printNameCourse(self):
            
            name = self.getName()
            
            course = self.course
            
            nameCourse = " ".join((name,course))

            print(nameCourse)


class Student(Person): 

    #Constructor of student 
    def __init__(self,fname,lname,subject): 

        #Subject instance 
        self.subject = subject

        #Call super constructor 
        super().__init__(fname,lname)
        
    def printNameSubject(self):
        
        name = self.getName()
        
        subject = self.subject
        
        nameSubject = " ".join((name,subject))

        print(nameSubject)