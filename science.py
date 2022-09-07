def calc_weight(m,g=10):
    print(f"your weight is: {m*g}N")
    return m*g

mass = int(input("pleaase enter your mass:"))
print(f"Your weight is {calc_weight(mass)}N.")
