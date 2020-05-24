from equations import gpe

# help(gpe)
gpe.hello()

eqn_gpe = gpe.GPE()
print(eqn_gpe.description)
# eqn_gpe.call()

print("Now using a list")

equations = []
equations.append(gpe.GPE())
print(equations[0].description)

for num, equation in enumerate(equations, start=1):
    # print(num)
    # print(equation.description)
    print("{}: {}".format(num, equation.description))
