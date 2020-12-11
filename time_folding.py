'''
Code: Time Shifting for DSP
      The function time_function depends to the given by the professor by default piece-wise functions.
      The function time_function accepts only the input which n and the offset k. 
      if k+ -> the signal advance
      if k- -> the signal delays
'''

def time_function(n):
    x_n = 0
    if(-1 >= n and -3 <= n):
        x_n = 2
    elif (n >= 1 and n<= 4):
        x_n = n 
    else:
        x_n = 0
    return x_n 

def time_folding(n, k):
    return time_function((-1*n) + k)

if __name__ == "__main__":
    print(time_folding(-4, 0))
