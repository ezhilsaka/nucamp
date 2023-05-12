def with_no_param():
    print("inside the function with no parameters")

def addition_fun(a, b):
    c = a + b
    print(c)
    return c

with_no_param()
d = addition_fun(10, 3)
e = addition_fun(1, 2)
print("values which are returned from functions ", d, e)