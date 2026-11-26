class Student:
    def __init__(self, name, gradeC,gradeM,gradeE):
        self.name = name
        self.gradeC = gradeC
        self.gradeM = gradeM
        self.gradeE = gradeE
    def __str__(self):
        return f"name: {self.name} gradeC: {self.gradeC} gradeM: {self.gradeM} gradeE: {self.gradeE} sum {self.gradeC+self.gradeM+self.gradeE}"
    def updateScore(self,gradeC=None,gradeM=None,gradeE=None):
        if gradeC is not None:
            self.gradeC = gradeC
        if gradeM is not None:
            self.gradeM = gradeM
        if gradeE is not None:
            self.gradeE = gradeE
#try
if __name__=="__main__":
    s1=Student("YSW",90,88,92)
    print(s1)
    s1.updateScore(gradeC=82)
    print(s1)



class EDU:
    system_version="1.0"
    system_name="EDU"
    def __init__(self):
        self.student_list=[]
    def add_student(self,student):
        name=input("enter student name:")
        for f in self.student_list:
            if f.name == name:
                print("student already exist")
                return
        gradeC=int(input("enter student gradeC:"))
        gradeM=int(input("enter student gradeM:"))
        gradeE=int(input("enter student gradeE:"))
        if 0<=gradeC<=100 and 0<=gradeM<=100 and 0<=gradeE<=100:
            stu=Student(name,gradeC,gradeM,gradeE)
            self.student_list.append(stu)
            print("student added successfully")
        else:
            print("Grade error")