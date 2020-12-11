'''
Code: Time Shifting for DSP
      The function time_function depends to the given by the professor by default piece-wise functions.
      The time shifting_function accepts only the input which n and the offset k. 
      if k+ -> the signal advance
      if k- -> the signal delays
'''
import argparse

def time_function(n):
    x_n = 0
    if(-1 >= n and -3 <= n):
        x_n = 1 + n/3
    elif (n >= 0 and n<= 3):
        x_n = 1
    else:
        x_n = 0
    return x_n 

def delay_shifting(n, k=0):
    return n[k:]

def advance_shifting(n, k=0):
    return n[:k]

def time_folding(n, k=0):
    return n[-(k+1)::-1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve seatwork 1.")
    parser.add_argument('--s',"--starting_point",type=int, required=True) 
    parser.add_argument('--e',"--ending_point",type=int, required=True) 
    parser.add_argument('--sp',"--sampling_point",type=int, required=True) 
    row_range = parser.parse_args()

    original_signal = list()
    start = row_range.s
    end = row_range.e
    sample = row_range.sp
    for i in range(start,end):
        original_signal.append(time_function(i))
    
    print(f"original signal{original_signal}")

    #1. First fold(n) and ten delay the resulting signal by four samples.
    
    folded_signal = time_folding(original_signal)
    delay_four = delay_shifting(folded_signal,sample)
    print(f'answer 1: {delay_four}')

    #First delay x(n) by four samples and then fold the resulting signal
    delay_four = delay_shifting(original_signal,sample)
    folded_signal = time_folding(delay_four)
    print(f'answer 2: {folded_signal}')