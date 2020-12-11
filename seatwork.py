'''
Code: Time Shifting for DSP
      The function time_function depends to the given by the professor by default piece-wise functions.
      The time shifting_function accepts only the input which n and the offset k. 
      if k+ -> the signal advance
      if k- -> the signal delays
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

def delay_time_shifting(n, k):
    return n[k:]

def advance_time_shifting(n, k):
    return n[:k]

def time_folding(n, k):
    return n[-(k+1)::-1]

if __name__ == "__main__":
    out = list()
    for i in range(-3,4):
        out.append(time_function(i))
    print(out)
    print(time_folding(out,-4))
