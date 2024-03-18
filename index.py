import csv
import math

PI = math.pi
TEST_VALUES = [0.0, 409.3, 149.8, -53.9, 75.0, 19.3, -52.2, 50.5, 0.0]
B_MULTIPLER = 2/PI

"""
(1) Getting values from csv
"""
def get_csv_values():
    res = []
    file = open('data.csv')
    for r in csv.reader(file):
        res.append(float(r[0]))
    file.close()
    return res

"""
(2) Converting i values to sin(ai/n), where a ranges from [0, n]
    and n is the length of all f values
"""
def get_sin_x_values(n, b):
    i_values = [i for i in range(n)]
    # 0, 1, 2, 3, 4 ... n
    
    pi_multiplier = (b * PI)/(n-1)
    # π/n
    
    pi_i_values = list(map(lambda i_value: i_value * pi_multiplier, i_values))
    # 0, π/n, 2π/n, 3π/n, ... nπ/n
    
    res_values = list(map(lambda pi_i_value: math.sin(pi_i_value), pi_i_values))
    # sin(0), sin(π/n), sin(2π/n) ... sin(nπ/n)
    
    assert n == len(res_values)
    
    return res_values

"""
(3) Cross multiply f * sin(x) to obtain the original approximation function
"""
def cross_fn(sin_i_values, f_values):
    return [sin_i_value * f_value for sin_i_value, f_value in zip(sin_i_values, f_values)]
    # f_0 * sin(0), f_1 * sin(π/n), f_2 * sin(2π/n) .... f_n * sin(nπ/n)

"""
(4) Trapezoid numerical approximation method
"""
def trap_fn(values):
    interval = PI/(len(values) - 1)
 
    total = sum(values[1:-1]) + (values[0]/2) + (values[-1]/2)
    
    return interval * total
    # standard formula for trapezoidal method

"""
(5) Multiplying the function by 2/π to get B_k(f)
"""
def get_b_fn(integral_value):
    return integral_value * B_MULTIPLER 
    # getting b_value

"""
(6) Putting (1) through (5) together to get a particular b value
"""
def get_b(f_values, b_index):
    sin_values = get_sin_x_values(len(f_values), b_index)
    trap_values = cross_fn(sin_values, f_values)
    return get_b_fn(trap_fn(trap_values))

"""
Iterative process for parsing test data in No. 3, and actual data in No. 4
"""    
def main():
    csv_values = get_csv_values()
    
    test_list = []
    test_b_value = 1
    
    while True:
        res = get_b(TEST_VALUES, test_b_value)
        if res <= 0:
            break
        test_b_value += 1
        test_list.append(round(res))
        
    print(test_list)
    print(bytes(test_list).decode('utf-8'))
    print("R: " + str(len(test_list)))
    
    res_list = []
    b_value = 1
    
    while True:
        res = get_b(csv_values, b_value)
        if res <= 0:
            break
        b_value += 1
        res_list.append(round(res))
    
    print(res_list)
    print(bytes(res_list).decode('utf-8'))
    print("R: " + str(len(res_list)-1)) # omit trailing 0
    
    
main()