class Student:
    # initialize
    def __init__(
        self,
        school_address="None",
        school="None",
        major="None",
        chair="None",
        student="None",
        ID="None",
        personal_address="None",
        credit="None",
        gpa="None",
    ):
        self.school_address = school_address
        self.school = school
        self.major = major
        self.chair = chair
        self.student = student
        self.ID = ID
        self.personal_address = personal_address
        self.credit = credit
        self.gpa = gpa

    # print out
    def __str__(self):
        return f"School_address: {self.school_address}\nSchool: {self.school}\nMajor: {self.major}\nChair: {self.chair}\nStudent: {self.student}\nID: {self.ID}\nPersonal_address: {self.personal_address}\nCredit: {self.credit}\nGPA: {self.gpa}"

    # down below are get and set function
    def set_school_address(self, adr):
        self.school_address = adr

    def getANDset_school_address(self, adr):
        self.set_school_address(adr)

    def set_school(self, name):
        self.school = name

    def getANDset_school(self, name):
        self.set_school(name)

    def set_major(self, mjr):
        self.major = mjr

    def getANDset_major(self, mjr):
        self.set_major(mjr)

    def set_chair(self, dm):
        self.chair = dm

    def getANDset_chair(self, dm):
        self.set_chair(dm)

    def set_student(self, name):
        self.student = name

    def getANDset_student(self, name):
        self.set_student(name)

    def set_ID(self, id):
        self.ID = id

    def getANDset_ID(self, id):
        self.set_ID(id)

    def set_personal_address(self, adr):
        self.personal_address = adr

    def getANDset_personal_address(self, adr):
        self.set_personal_address(adr)

    def set_credit(self, cdt):
        self.credit = cdt

    def getANDset_credit(self, cdt):
        self.set_credit(cdt)

    def set_GPA(self, sc):
        self.gpa = sc

    def getANDset_GPA(self, sc):
        self.set_GPA(sc)


# initialize
print("-----------Before edit-----------")
info = Student()
print(info)

print("-----------After edit------------")

school_adr = "Tainan city yongkang district"
school = "STUST"
major = "CSE"
chair = "Gwo-Jiun Horng"
student = "Jason"
id = "4B0G----"
personal_adr = "Tainan city yongkang district"
credit = "97"
gpa = "4.1"

# get and set all information
info.getANDset_school_address(school_adr)
info.getANDset_school(school)
info.getANDset_major(major)
info.getANDset_chair(chair)
info.getANDset_student(student)
info.getANDset_ID(id)
info.getANDset_personal_address(personal_adr)
info.getANDset_credit(credit)
info.getANDset_GPA(gpa)

print(info)
