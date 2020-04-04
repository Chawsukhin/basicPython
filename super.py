#using super
#parent
class Employee:
    def __init__(self, developer, designer):
        self.developer=developer
        self.designer=designer
    def run(self):
        print("Compamy run with", self.developer,"developer and", self.designer,"designer.")

#child
class Talent_Employee(Employee):
    def __init__(self, developer, designer, team):
      super().__init__(developer, designer)
      self.team=team
    def special_run(self):
        self.run()
        print("Company has ",self.team,"talent team.")

e1=Talent_Employee(100,50,10)
e1.special_run()
