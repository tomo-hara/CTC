# Given 2 integers, write a program that outputs the value of subtracting the larger number from the a smaller number given in the input.
# Outputs the value of the larger integer minus a smaller integer.

n, m= map(int, input().split())

if n > m:
    print(n - m)
else:
    print(m - n)