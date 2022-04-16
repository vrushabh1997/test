
class animal:

    
    def __init__(self,name,colour,height):
        self.name = name;
        self.colour = colour;
        self.height = height;


    def description(self):
        return f" {self.name} "


obj = animal("tiger","red",25)
print(obj.description())


        
    


    