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


