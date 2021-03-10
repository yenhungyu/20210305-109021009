import sys
import Mymodule as my

if sys.argv[1] == "-f":
    val=int(sys.argv[2])
    print(my.getFibonacci(val))
elif sys.argv[1] == "-n":
    val = int(sys.argv[2])
    print(my.getNumberDigits(val))