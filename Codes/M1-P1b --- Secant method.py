# Secant Method

def f(x):
    # Define the function here
    return x**3 - x - 2

# Input interval
a = float(input("Enter first approximation (a): "))
b = float(input("Enter second approximation (b): "))

# Accuracy and maximum iterations
tolerance = 0.0001
max_iter = 50

print(f"\n{'Iter':<10}{'a':<9}{'b':<9}{'x':<9}{'f(a)':<9}{'f(b)':<9}{'f(x)':<9}")
print("-" * 60)

for i in range(1, max_iter + 1):

       # Regula Falsi Formula
       x = (a * f(b) - b * f(a)) / (f(b) - f(a))
       print(f"{i:<9}{a:<9.4f}{b:<9.4f}{x:<9.4f}{f(a):<9.4f}{f(b):<9.4f}{f(x):<9.4f}")
        
       # Check stopping condition
       if abs(f(x)) < tolerance:
           print("\nAns:an approximate Root of the given equation is", round(x, 4))
           break

       # Update interval
       a = b
       b = x

else:
    print("\nMaximum iterations reached.")
