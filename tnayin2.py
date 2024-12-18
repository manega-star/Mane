
class Plant:
   def __init__(self, name, scientific_name):
       self.name = name
       self.scientific_name = scientific_name
   def photosynthesize(self):
       return f"{self.name} is photosynthesizing."

class Tree(Plant):
   def __init__(self, name, scientific_name, tree_type):
       super().__init__(name, scientific_name)  
       self.tree_type = tree_type
   def grow(self):
       return f"{self.name} the {self.tree_type} tree is growing taller."

class Flower(Plant):
   def __init__(self, name, scientific_name, color):
       super().__init__(name, scientific_name)  
       self.color = color
   def bloom(self):
       return f"{self.name} the {self.color} flower is blooming."

class Oak(Tree):
   def __init__(self, name, scientific_name, tree_type, age):
       super().__init__(name, scientific_name, tree_type) 
       self.age = age
   def grow(self):
       return f"{self.name} the Oak tree is {self.age} years old and growing taller."

class Rose(Flower):
   def __init__(self, name, scientific_name, color, fragrance):
       super().__init__(name, scientific_name, color)  
       self.fragrance = fragrance
   def bloom(self):
       return f"{self.name} the {self.color} Rose blooms and smells {self.fragrance}."

oak = Oak("Mighty Oak", "Quercus robur", "Deciduous", 50)
rose = Rose("Red Rose", "Rosa", "red", "sweet")

print(oak.photosynthesize())  
print(oak.grow())  
print(rose.photosynthesize())  
print(rose.bloom())  