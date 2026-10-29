s = "Ronaldo" #string are immutable cant change a string character it creates a new string
s1 = "B" + s[1:]
s2 = s.replace("R","r")
s = s.replace("R", "G") #creates a new string s 
# print(s1)
# print(len(s2))
# print(s)
# print(s.lower())
# print(s1.upper()) #creates a new s string with all character uppercase
# print(s1.replace("e", "")) #replace al occurances of e with a empty string ""
print(s*3)
print(f"{s2} is a smart guy, while {s} is a oversmart guy")
print("I am {} and {} is my son".format("God", s2))
print("ronaldo" in s2) #return a True or False value if the given string is present or absent in a perticular string\
