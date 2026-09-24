# Jacobi Iteration Method

# Input coefficients
a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))
d1 = float(input("Enter d1: "))

a2 = float(input("\nEnter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))
d2 = float(input("Enter d2: "))

a3 = float(input("\nEnter a3: "))
b3 = float(input("Enter b3: "))
c3 = float(input("Enter c3: "))
d3 = float(input("Enter d3: "))

# Initial guesses
x = float(input("\nInitial guess for x: "))
y = float(input("Initial guess for y: "))
z = float(input("Initial guess for z: "))

# Number of iterations
n = int(input("Enter number of iterations: "))

print("\nIteration\t x\t\t y\t\t z")
print("-" * 50)

for i in range(1, n + 1):

    # Calculate NEW values using OLD values
    x_new = (d1 - b1 * y - c1 * z) / a1
    y_new = (d2 - a2 * x - c2 * z) / b2
    z_new = (d3 - a3 * x - b3 * y) / c3

    # Display new values
    print(f"{i}\t\t {x_new:.6f}\t {y_new:.6f}\t {z_new:.6f}")

    # Update values AFTER all three calculations
    x = x_new
    y = y_new
    z = z_new

print("\nApproximate Solution:")
print("x =", round(x, 6))
print("y =", round(y, 6))
print("z =", round(z, 6))
