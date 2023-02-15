from functools import lru_cache

@lru_cache(maxsize=None)
def euclid_alg_2(x,y):
    q, r = divmod(x,y)
    print(f"{x} = {q}*{y} + {r}")
    if r == 0:
        print(f"d = {y}")
        return 0, 1
#     if y%r == 0:
#         return 1, -q
    return euclid_alg_2(y, r)[1], (euclid_alg_2(y,r)[0] - euclid_alg_2(y,r)[1]*q)

x, y = 2476, 3539
a, b = euclid_alg_2(x,y)
d = a*x + b*y
print("\nYou can comment the print statement (that you see above) out of the function. It just prints x = q*y + r for each")
print("step of the algorithm.If you want to look at the second to last line, the 'r' there should be the gcd of x and y. ")
print(f"It should be d = {d}.\n")
print(f"x = {x}, y = {y}, and our function told us a = {a} and b = {b}.")
print(f"Here's the check: ax + by should be their GCD. Let's see: d = ax + by = ({a})*({x}) + ({b})*({y}) = {a*x + b*y}\n")
print(f"If d is a divisor of both x and y, then it must be the greatest common divisor (because no other divisor")
print(f"can be expressed as the sum of a multiple of x and a multiple of y. In the languate of ring theory, ")
print(f"<d> = <x,y> if and only if d divides both a and b (it's a common divisor) and d = ax + by for some a, b in Z.")
q1, r1 = divmod(x, d)
q2, r2 = divmod(y, d)
print(f"Check: x = {q1}d + {r1}, and y = {q2}d + {r2}.")
if (r1, r2) == (0, 0):
    print("Yes, it checks out!")
else: 
    print("Hang on! The remainders are not both 0, so d is NOT a common divisor. What happened?")