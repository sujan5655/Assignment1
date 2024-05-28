#. Given a list of strings representing decimal numbers (e.g., ['1.1', '2.2', '3.3']), write a for loop that converts each string to a float, doubles the value, and prints the result.
list=['1.1','2.2','3.3','4.4','5.5']
double=0
for strToFloat in list:
    floatvalue=float(strToFloat)
    double=floatvalue*floatvalue
    print(double)   