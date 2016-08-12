# Due to, in OOP recurtion takes a lot of memory space, Idecided to do it iterating
def fibonacci(number):
    if number == 0:
            return [0]
    Fn_1 = 1
    Fn_2 = 0
    fib = [Fn_2,Fn_1]
    if float(number).is_integer():
        for i in range(number-1):
            Fn = Fn_1 + Fn_2
            Fn_2 = Fn_1
            Fn_1 = Fn
            fib.append(Fn)
    else:
        return ("Oe, only integers!")

    return (fib)


            # python -i EjercicioJaimeMolina.py 3
            # 6
if __name__ == '__main__':
    for i in range(11):
        print("Number: {0}; Fibonacci: {1}".format(i, fibonacci(i)))
