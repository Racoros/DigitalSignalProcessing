'''
Code: Time Shifting for DSP
'''


def time_function(n):
    x_n = 0
    if(-1 >= n and -3 <= n):
        x_n = 1 + n/3
    elif (n >= 0 and n<= 3):
        x_n = 1
    else:
        x_n = 0
    return x_n 

def time_shifting(n, k):
    return time_function(n + k)

def time_folding(n, k):
    return time_function((-1*n) + k)

if __name__ == "__main__":
    time_function_list = list()
    time_folding_list = list()
    for i in range(-3,4):
        print(i)
        time_function_list.append(time_function(i))
        time_folding_list.append(time_folding(i,0))
    print(f'original function {time_function_list}')
    print(f'folding function {time_folding_list}')