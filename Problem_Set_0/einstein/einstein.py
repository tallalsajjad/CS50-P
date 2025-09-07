def main():
    mass = int(input("Enter a mass:"))
    E = joul(mass)
    print("The energy is", E)

def joul(n):
    m = int(n * 9 * 10**16)
    return m


main()
