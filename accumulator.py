'''
Code: discrete time for DSP
'''

def time_function(n):
    x_n = 0
    if(n >= -3 and n <= 3):
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
    a_n = list()
    b_n = list()
    c_n = list()
    d_n = list()
    for i in range(-7,4):
        a_n.append(a(i))
        b_n.append(b(i))
        c_n.append(c(i))
        d_n.append(d(i))
    print(a_n)
    print(b_n)
    print(c_n)
    print(d_n)