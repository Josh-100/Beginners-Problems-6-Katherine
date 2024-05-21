def triangleTest(a, b, c):
    if (a + b > c ) and (b + c > a) and (a + c) > b:
        return True 
    else:
        return False  

print(triangleTest(3, 4, 5)) 
print(triangleTest(1, 2, 3))