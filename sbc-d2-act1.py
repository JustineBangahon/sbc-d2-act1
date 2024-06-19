#indexing
#a = input("Word: ")
#print(a[len(a) - 1])
#x = "Hello World"
#print(x[-1])

#======================================
#slicing

#a = "Hello World"
#print(a[-8:-6])
#print(a[0:2], a[6:8])
#print(f"{a[0:2]} {a[6:8]}")
#print("{0} {1}".format(a[0:2], a[6:8]) )

#======================================
#string MEthods

#a = "helloworld123"
#print(a.upper()) #upper all
#print(a.lower()) #lower all
#print(a.capitalize()) #capitalize first letter
#print(a.title()) # every first letter of word
#print(a.replace("h", "x")) #replace the letter you want
#print(a.find("h")) #find the index of the letter
#print(a.isalpha()) #check if all are alphabit
#print(a.isnumeric()) #check if all are numerical
#print(a.isalnum()) #check if all are numerical

#======================================
#excercise
a = "summber bootcamp"

print(a.title())

print(f"{a.capitalize().replace("p", "P")}")
replace1 = a.replace("b", "L")
print(f"{replace1[8:12]}")

print(f"{a[12:16].replace("p", "E")}")
#print(a.find("a"))
#print(a.find("r"))
print(f"{a[13].upper()}{a[6].upper()}")

print(a.replace(" ", "").isalpha)
