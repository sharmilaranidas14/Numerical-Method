

def newton(x, y, xp):

    n = len(x)
    d = []

    for i in range(n):
        d.append(y[i])

    yp = d[0]

    product = 1
    for i in range(1, n):
        for j in range(n-i):
            d[j] = (d[j+1] - d[j]) / (x[j+i] - x[j])

        product = product * (xp - x[i-1])

        term = d[0] * product

        print("Order", i)
        print("Term =", term)

        yp = yp + term

        print("Estimate =", yp)

    return yp

n = int(input("Number of data points: "))

x = []
y = []

print("Enter x values:")
for i in range(n):
    x.append(float(input()))

print("Enter y values:")
for i in range(n):
    y.append(float(input()))

xp = float(input("Enter interpolation point: "))


result = newton(x, y, xp)

print("\nFinal estimate:")
print("f(", xp, ") =", result)
