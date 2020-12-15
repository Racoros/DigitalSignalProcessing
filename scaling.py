'''
Code: Scaling for DSP
'''

def time_function(n):
    x_n = 0
    if(0 >= n and -7 <= n):
        x_n = n+4
    elif (n >= 1 and n<= 4):
        x_n = 4 
    else:
        x_n = 0
    return x_n 

def scaling(n):
    return time_function((2*n))

if __name__ == "__main__":
    for i in range(-7,4):
        print(scaling(i))