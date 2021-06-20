class Chess:
    def __init__ (self,name,colar,power,step,level):
        self.heroName=name
        self.heroColar=colar
        self.heroPower=power
        self.heroStep=step
        self.heroLevel=level
    def showinfo(self):
        print(self.heroName)
        print(self.heroColar)
        print(self.heroPower)
        print(self.heroStep)
        print(self.heroLevel)

x1=Chess("帥","Red","8","1","100")
x2=Chess("將","Black","8","1","100")
x3=Chess("俥","Red","6","10","700")

x1.showinfo()
x2.showinfo()
x3.showinfo()
