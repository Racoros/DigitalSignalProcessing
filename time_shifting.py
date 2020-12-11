'''
Code: Time Shifting for DSP
'''


def time_function(n):
    x_n = 0
    if(0 >= n and -5 <= n):
        x_n = n + 4
    elif (n >= 1 and n<= 4):
        x_n = 4
    else:
        x_n = 0
    return x_n 

def time_shifting(n, k):
    return time_function(n + k)

if __name__ == "__main__":
    print(time_shifting(-8, -3))
