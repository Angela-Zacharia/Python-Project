import sympy as sy


def newtonsmethod(func, funcderiv, x, n):
  for i in range(1, n + 1):
    f = eval(func)
    df = eval(funcderiv)
    x = x - f / df
  print(f"The root was found to be at {x} after {n} iterations")


def getuserfunction():
  expression = input("Enter the function in terms of 'x': use * for coefficients and ** for exponents: ")
  x = sy.Symbol('x')
  return sy.sympify(expression)


def trapezoidal_rule(f, a, b, n):
  h = (b - a) / n
  k = 1
  sum_value1 = 0
  while (k < n):
    t = a + k * h
    sum_value1 = sum_value1 + f.subs(x, t)
    k = k + 1
  int_a = (h / 2) * (f.subs(x, a) + f.subs(x, b) + 2 * sum_value1)
  return int_a


def simpsons_rule(f, a, b, n):
  h = (b - a) / n
  k = 1
  sum_value = 0
  while (k < n):
    x_k = a + k * h
    if (k % 2 == 0):
      sum_value = sum_value + 2 * f.subs(x, x_k)
    else:
      sum_value = sum_value + 4 * f.subs(x, x_k)
    k = k + 1
  Ia = (h / 3) * (f.subs(x, a) + f.subs(x, b) + sum_value)
  return Ia


while True: 
    print(' ')
    print('Enter: ')
    print('1 - for root finder')
    print('2  - for integral calculation')
    print('3  - to exit the program')
    option = int(input())

    if option == 1:

        print('Enter the function: use * for coefficients and ** for exponents')
        func = input()

        print('Enter the derivative of the function: use * for coefficients and ** for exponents')
        dfunc = input()

        print('Enter the intial guess')
        x = float(input())

        print('Enter the maximum number of iterations')
        num_iter = int(input())

        newtonsmethod(func, dfunc, x, num_iter)

    elif option == 2:
        choice = int(input('Choose 1 for Simpsons method and 2 for Trapezoidal method: '))

        user_function = getuserfunction()

        x = sy.Symbol("x")
        a = float(input("Lower Limit: "))
        b = float(input("Upper Limit: "))
        n = int(input("Number of strips= "))

        if choice == 1:

            Ie = sy.integrate(user_function, (x, a, b))

            Ia = simpsons_rule(user_function, a, b, n)
            print("Approximate Value of Integration=", Ia)
            print("Exact Value of Integration=", Ie.evalf())
        else:

            Ie = sy.integrate(user_function, (x, a, b))

            int_a = trapezoidal_rule(user_function, a, b, n)
            print("Approximate Value of Integration=", int_a)
            print("Exact Value of Integration=", Ie.evalf())
    else: 
        print("You have chosen to exit the program")
        break