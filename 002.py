#Even Fibonacci numbers
 
sum_even_value = 0

def fib_num(previous, next_num, init, end):
    prv = previous
    nxt = next_num
    for num in range(init, end):
        fib = prv + nxt
        if fib > 4000000:
            break
        if fib % 2 == 0:
            global sum_even_value
            sum_even_value = sum_even_value + fib
        
        #print(num, fib)
        prv = nxt
        nxt = fib

fib_num(0, 1, 0, 32)
print('Sum Even-Value: ', sum_even_value)