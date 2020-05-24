from equations import gpe

# help(gpe)
# gpe.hello()

# eqn_gpe = gpe.GPE()
# print(eqn_gpe.name)
# print(eqn_gpe.call())

print("Now using a list")

equations = []
equations.append(gpe.GPE())
# print(equations[0].name)

for num, equation in enumerate(equations, start=1):
    # print(num)
    # print(equation.name)
    print("{}: {}".format(num, equation.name))
index = int(input("Choose equation: ")) - 1
# print(equations[index].call())
eqn_gpe = equations[index]
result = eqn_gpe.call()
print(result)
