'''
Code: Scaling for DSP
'''

def time_function(n):
    x_n = 0
    if(0 >= n and -7 <= n):
        x_n = n+4
    elif (n >= 1 and n<= 6):
        x_n = 4 
    else:
        x_n = 0
    return x_n 

def scaling(n,k):
    return time_function((k*n))

if __name__ == "__main__":
    for i in range(-7,7):
        print(f'y({i}) = x(3*({i})) = x({3*i}) = {scaling(i,3)}')