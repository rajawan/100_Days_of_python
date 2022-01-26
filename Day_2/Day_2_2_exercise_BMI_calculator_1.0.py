#Get the weight from  user
weight=input("Enter your weight: ")
height=input("Enter your height: ")

#Check the type of those input if they str then convert them into number
print(type(weight))
print(type(height))
weight_in_int=int(weight)
height_in_float=float(height)
#Bmi calculation rule weight/height*height
result=weight_in_int/height_in_float**2
print(int(result))