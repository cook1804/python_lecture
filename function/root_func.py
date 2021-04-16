def get_root(a,b,c):
    x_1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x_2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return x_1, x_2

sol = get_root(2,-1,-6)
print(sol)