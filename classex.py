class royal_enfield:
    def __init__(self,model_name,color,milage):
        self.m=model_name
        self.c=color
        self.mi=milage
model=input()
color=input()
mil=input()
obj1=royal_enfield(model,color,mil)
obj2=royal_enfield(model,color,mil)
obj3=royal_enfield(model,color,mil)
print(obj1.m,obj1.c,obj1.mi)
print(obj2.m,obj2.c,obj2.mi)
print(obj3.m,obj3.c,obj3.mi)
