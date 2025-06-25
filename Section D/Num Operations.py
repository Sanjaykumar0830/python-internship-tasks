def square_and_cube(num):
    square = num ** 2
    cube = num ** 3
    return square, cube
n = int(input("Enter a number: "))
sq, cu = square_and_cube(n)
print("Square:", sq)
print("Cube:", cu)
