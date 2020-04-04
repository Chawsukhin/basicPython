class Employee:
    def __init__(self, developer, designer):
     self.developer=developer
     self.designer=designer

e1=Employee(5,3)
print("Company has ", e1.developer,"developer and", e1.designer,"designer.")
