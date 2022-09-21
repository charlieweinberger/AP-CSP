def c_to_f(c):
    return float(c) * 9/5 + 32

def f_to_c(f):
    return (float(f) - 32) * 5/9

def c_to_k(c):
    return float(c) + 273.15

def k_to_c(k):
    return float(k) - 273.15

input_type = input("What is the temp measured in? (c/f/k) ")
temp = input("What is the temperature? (just the number) ")
output_type = input("What would you like to convert to? (c/f/k) ")

if input_type not in ['c', 'f', 'k'] or output_type not in ['c', 'f', 'k']:
    print('please enter correct values.')
elif input_type == 'c' and output_type == 'f':
    print(f'Your new temperature is {c_to_f(temp)} degrees fahrenheit.')
elif input_type == 'f' and output_type == 'c':
    print(f'Your new temperature is {f_to_c(temp)} degrees celcius.')
elif input_type == 'c' and output_type == 'k':
    print(f'Your new temperature is {c_to_k(temp)} degrees kelvin.')
elif input_type == 'k' and output_type == 'c':
    print(f'Your new temperature is {k_to_c(temp)} degrees celcius.')
else:
    print('That converter is not available.')