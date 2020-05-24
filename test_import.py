from equations import gpe
from equations import velocity

# help(gpe)
# gpe.hello()

# eqn_gpe = gpe.GPE()
# print(eqn_gpe.name)
# print(eqn_gpe.calculate())

print("Now using a list")

equations = []
equations.append(gpe.GPE())
equations.append(velocity.Velocity())
# print(equations[0].name)

for num, equation in enumerate(equations, start=1):
    # print(num)
    # print(equation.name)
    print("{}: {}".format(num, equation.name))
index = int(input("Choose equation: ")) - 1
equation = equations[index]
print("{} = {}".format(equation.name, equation.calculate()))
# print(equations[index].calculate())
# eqn_gpe = equations[index]
# result = eqn_gpe.calculate()
# print(result)
