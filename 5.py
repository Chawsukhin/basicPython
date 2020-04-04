
class House :
     def __init__(self, brick, wood):
         self.brick = brick
         self.wood = wood
     def built ( self ) :
           print ( "We built a house with", self.brick, "bricks and", self.wood, "woods." )
h1 = House( 30000, 1000)
h2 = House( 20000, 500 )

h1.built()
h2.built()

h1.brick += 1000
h1.built()
