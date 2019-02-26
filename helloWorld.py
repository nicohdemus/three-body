from threeBody import *

print("""
Hello World""")
print("*" * 11)

testVar = 'Hello Dave'

print('Test variable = {}'.format(testVar))

x = ThreeBody()
y = ThreeBody()

x.setAttribute(STR=6, VIG=8, CHA=0)
x.setSkill(Range=6)

print("\nBase Parry = " + str(x.baseParry()))

print("\nToughness")
for i in x.armor:
    print('{} = {}'.format(i, x.toughness(i)))
#    print(f'{i} = {x.toughness(i)}')

print("\nAttributes")
for i in x.attributes:
    print('{} = {}'.format(i, x.attributes[i]))
 #   print(f'{i} = {x.attributes[i]}')

print("\nPlayer name: {}".format(x.name))
print("\nPlayer name: {}\n\n".format(y.name))

def fizzBuzz(input):
    output = ""
    if input % 3 == 0:
        print("Divisible by 3")
        output = "Fizz"
    if input % 5 == 0:
        print("Divisible by 5")
        output += "Buzz"
    if output == "":
        output = input
    return output


print(fizzBuzz(15))
