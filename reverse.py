# Question 5: Reverse Integer
def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_n = int(str(abs(n))[::-1])
    return sign * reversed_n

input_integer = int(input("Enter an integer: "))
reversed_result = reverse_integer(input_integer)

print(f"For input {input_integer}, the program returns {reversed_result}.")
