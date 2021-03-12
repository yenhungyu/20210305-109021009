class Hero:
    def __init__ (self,name,power,_property,weapons,level):
        self.heroName=name
        self.heroPower=power
        self.heroProperty=_property
        self.heroWeapons=weapons
        self.heroLevel=level
    def showinfo(self):
        print(self.heroName)
        print(self.heroPower)
        print(self.heroProperty)
        print(self.heroWeapons)
        print(self.heroLevel)

x1=Hero("小李","3500","木","武術","30")
x2=Hero("小靈","4000","光","弓箭","28")
x3=Hero("小刺","3000","暗","短刀","25")

x1.showinfo()
x2.showinfo()
x3.showinfo()