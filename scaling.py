'''
Code: Scaling for DSP
      The function time_function depends to the given by the professor by default piece-wise functions.
      The function time_function accepts only the input which n and the offset k. 
      if k+ -> the signal advance
      if k- -> the signal delays
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