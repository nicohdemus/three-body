import threeBody

print ("""
Hello World
""")
print ("*" * 11)

x = threeBody.ThreeBody()
print("Base Parry = " + str(x.baseParry()))

for i in x.attributes:
    print (i)