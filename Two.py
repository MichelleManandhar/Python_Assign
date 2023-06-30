# 2) Fibonacci Sequence
# Take length as input and give fib seq till that 
# length
# Example 1:
# Input: 5
# Output:
# 0,1,1,2,3
# Example 2:
# Input: 10
# Output:
# 0,1,1,2,3,5,8,13,21,34
def fibonacci(num):
    #sets intial sequence
    fib_seq = [0,1]

    while len(fib_seq) < num:
        next_num = fib_seq[-1] + fib_seq[-2] #-1 last element and -2 second last element
        fib_seq.append(next_num)  #appending it to the previous list
    return fib_seq
    
user_input = int(input("Enter an interger:"))
value = fibonacci(user_input)
print(value)
