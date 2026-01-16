class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def diplay_details(self):
        print("student name:",self.name,)
        print("roll no:",self.roll_no)

student1=student("abhi", 143)
student2=student("sash",142)
student1.diplay_details()
student2.diplay_details()