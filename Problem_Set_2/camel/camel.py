input = input("camelCase:")
space = ""

for camel in input:
    if camel.isupper():
        space += "_" + camel.lower()
    else:
        space += camel

if space.startswith("_"):
    space = space[1:]
print("snake_case:", space)
