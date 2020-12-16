'''
Code: discrete time for DSP
'''

def time_function(n):
    x_n = 0
    if(n >= -4 and n <= 4):
        x_n = abs(n)
    else:
        x_n = 0
    return x_n 

def a(n):
    return time_function((n))

def b(n):
    return time_function((n-1))

def c(n):
    return time_function((n+1))

def d(n):
    return (1/3)*(a(n)+b(n)+c(n))

if __name__ == "__main__":
    item_one = list()
    item_two = list()
    for i in range(-4,5):
        item_one.append(c(i))
        item_two.append(d(i))
    print(f'y(n) = x(n+1) sequence:{item_one}')
    print(f'y(n) = (1/3)*[x(n+1) + x(n) + x(n-1)] sequence:{item_two}')