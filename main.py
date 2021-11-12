import sys
import time

from container import *

#----------------------------------------------


# Algorithm was taken from https://stackoverflow.com/questions/18262306/quicksort-with-python/20258416
def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0].max_dist()
        for x in array:
            if x.max_dist() < pivot:
                less.append(x)
            elif x.max_dist() == pivot:
                equal.append(x)
            elif x.max_dist() > pivot:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return array

#----------------------------------------------


# main.py
# main.py -r 10 out1.txt out2.txt
# main.py -f in1.txt out1.txt out2.txt
if __name__ == '__main__':
    start_time = time.time()
    sys.argv = ["", "-f", "in6.txt", "out1.txt", "out2.txt"]
    if len(sys.argv) != 5:
        print( "Waited:\n command -f infile outfile01 outfile02\n Or:\n command -n number outfile01 outfile02\n")
        exit(-1)
    print('==> Start')
    container = Container()
    if sys.argv[1] == "-f":
        ifile = open(sys.argv[2])
        data = ifile.read()
        ifile.close()
        strArray = data.replace("\n", " ").split(" ")
        container.read(strArray)
    elif sys.argv[1] == "-r":
        size = int(sys.argv[2])
        if (size < 1) or (size > 10000):
            print("Wrong size for array")
            exit()
        container.rnd(int(sys.argv[2]))
    else:
        print("Incorrect file format")
        exit()

    first_output = open(sys.argv[3], "w+")
    second_output = open(sys.argv[4], "w+")

    container.print(first_output)
    first_output.close()
    container.store = quick_sort(container.store)
    container.print(second_output)
    second_output.close()
    print('==> Finish')
    print(f"-> {(time.time() - start_time) * 1000: .4f}ms")
