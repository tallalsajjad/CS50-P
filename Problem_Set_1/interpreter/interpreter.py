
interpreter= input("Expression: ")

x, y, z = interpreter.split()

x = int(x)
z = int(z)

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
else:
    print("Not supported")
    exit()

print(f"{result:.1f}")
