# Regula Falsi Method

def f(x):
# Define the function here
    return x**3 - x - 2

# Input interval
a = float(input("Enter first approximation (a): "))
b = float(input("Enter second approximation (b): "))

# Accuracy and maximum iterations
tolerance = 0.0001
max_iter = 50

# Check if root lies in the interval
if f(a) * f(b) > 0:
    print("Invalid interval! Root does not lie between a and b.")
else:
    print(f"\n{'Iter':<10}{'a':<8}{'b':<8}{'x':<8}{'f(a)':<8}{'f(b)':<8}{'f(x)':<8}")
    print("-" * 55)

    for i in range(1, max_iter + 1):

        # Regula Falsi Formula
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"{i:<8}{a:<8.4f}{b:<8.4f}{x:<8.4f}{f(a):<8.4f}{f(b):<8.4f}{f(x):<8.4f}")
        
        # Check stopping condition
        if abs(f(x)) < tolerance:
            print("\nAns:an approximate Root of the given equation is", round(x, 4))
            break

        # Update interval
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    else:
        print("\nMaximum iterations reached.")
