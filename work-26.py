
#23-misol
 #   n = int(input("n = "))
 #   x = float(input("x = "))
 #   S = 0
 #   sign = 1
 #        daraja = 2*i + 1
 #       factorial = math.factorial(daraja)
 #       S += sign * x**daraja / factorial
 #       sign *= -1
 #   print("Yig'indi =", S)
 #   print("math.sin(x) =", math.sin(x))


#24-misol
  #  n = int(input("n = "))
  #  x = float(input("x = "))
  #  S = 0
  #  sign = 1
  #  for i in range(n + 1):
  #      daraja = 2*i
  #      factorial = math.factorial(daraja)
  #      S += sign * x**daraja / factorial
  #      sign *= -1
 #   print("Yig'indi =", S)
 #   print("math.cos(x) =", math.cos(x))


#25-misol
#    n = int(input("n = "))
#    x = float(input("x = "))
#    S = 0
#    for i in range(1, n + 1):
#        S += ((-1)**(i-1)) * x**i / i
#    print("Yig'indi =", S)


#26-misol
 #   n = int(input("n = "))
  #  x = float(input("x = "))
#    S = 0
#    sign = 1
#    for i in range(n):
#        daraja = 2*i + 1
#        S += sign * x**daraja / (2*i + 1)
#        sign *= -1
#    print("Yig'indi =", S)


# 29-misol:
   # n = int(input("n = "))
   # A = float(input("A = "))
   # B = float(input("B = "))
   # h = (B - A) / n
   # for i in range(n + 1):
   #     print(A + i*h)


#30-misol
#    n = int(input("n = "))
#    A = float(input("A = "))
#    B = float(input("B = "))
#    h = (B - A) / n
#    for i in range(n + 1):
#        x = A + i*h
#        print("x =", x, " F(x) =", 1 - math.sin(x))


#31-misol
#    n = int(input("n = "))
#    print(A)
   #  for k in range(1, n):
  #       A = 2 + 1/A
   #       print(A)


#32-misol
#      n = int(input("n = "))
#      A = 1
#      print(A)
#      for k in range(1, n):
#          A = (A + 1) / k
#          print(A)