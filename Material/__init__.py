# this file contains the basic data about a material
class Unit:
    metro = "metro"
    centimetro = "centimetro"
    gramo = "gramo"
    kilogramo = "kilogramo"
class Material:
    def __init__(self,name,weight,weightunity,longitud,longitudunity):
        self.name=name
        self.weight = weight
        self.weightunity = weightunity
        self.longitud = longitud
        self.longitudunity = longitudunity

class materials:
        water = Material("agua",1,Unit.gramo,1,Unit.centimetro)



