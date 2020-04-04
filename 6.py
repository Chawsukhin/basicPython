#parent
class House :
    def __init__(self, brick, wood):
        self.brick = brick
        self.wood = wood
    def built ( self ) :
        print ( "We built a house with", self.brick, "bricks and", self.wood, "woods." )
#child
class Beautiful_house(House):
    def __init__(self, brick, wood, garden):
      House.__init__(self, brick, wood)
      self.garden = garden

    def special_built(self):
       self.built()
       print("We built beautifully with", self.garden, "garden.")

h1 = Beautiful_house( 30000, 1000, 1)
h1.special_built()

#super
#parent
class House :
   def __init__(self, brick, wood):
       self.brick = brick
       self.wood = wood
   def built ( self ) :
       print ( "We built a house with", self.brick, "bricks and", self.wood, "woods." )
#child
class Beautiful_house(House):
   def __init__(self, brick, wood, garden):
     super().__init__(brick, wood)
     self.garden = garden
   def special_built(self):
     self.built()
     print("We built beautifully with", self.garden, "garden.")

h1 = Beautiful_house( 30000, 1000, 1)
h1.special_built()
