class student:
    def __init__(self ,name ,id):
        self.studName =name
        self.studId =id

x =student("卡卡" , "109021009")
print(x.studName, "\t", x.studId)