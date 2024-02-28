import math
def main (x, y, a, z):
    Y = math.sqrt ((1+z) * ((x +(y/x)) / (a - (1/(1+x)))))
    print (Y)
    print (x, y, a, z)

main(27, 89, 68, 56) 