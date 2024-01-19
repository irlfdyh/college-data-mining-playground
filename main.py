# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test_shape():
    import numpy as np
    import numpy.ma as ma
    # creating an array
    a = np.array([1, 2, 3, 4, 5, 6])
    b = np.array([[1, 2, 3], [4, 5, 6]])

    # implementing the ma.shape() method
    c = ma.shape(a)
    d = ma.shape(b)

    print(a)
    print("This is the shape of array a: ", c)

    print(b)
    print("This is the shape of array b: ", d)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    test_shape()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
