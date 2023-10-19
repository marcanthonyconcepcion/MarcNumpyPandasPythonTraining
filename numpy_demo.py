import numpy


def demo_numpy_array():
    print('Demo: Numpy Array')
    input_list = [1.0, 2.1, 3.3, 4.2, 5.2]
    print(f'Input list is {input_list}')
    output_numpy_array = numpy.array(input_list, dtype=int)
    print(f'Output numpy array is {output_numpy_array}')


def demo_array_shape():
    print('Demo: Array Shape')
    one_dimensional_list = [1, 2, 3, 4, 5]
    print(f'One-dimensional input list is\n {one_dimensional_list}\n')
    one_dimensional_array = numpy.array(one_dimensional_list)
    print(f'One-dimensional array is\n {one_dimensional_array}\n')
    print(f'Shape spec of the one-dimensional array is\n {one_dimensional_array.shape}\n')

    two_dimensional_list = [[1, 2], [3, 4], [6, 5]]
    print(f'Two dimensional list is\n {two_dimensional_list}\n')
    two_dimensional_array = numpy.array(two_dimensional_list)
    print(f'Two-dimensional array is\n {two_dimensional_array}\n')
    print(f'Shape spec of the two-dimensional array is\n {two_dimensional_array.shape}\n')

    three_dimensional_list = [[1, 2, 3, 4], [3, 4, 5, 6], [6, 5, 4, 8]]
    print(f'Three dimensional list is\n {three_dimensional_list}\n')
    three_dimensional_array = numpy.array(three_dimensional_list)
    print(f'Three-dimensional array is\n {three_dimensional_array}\n')
    print(f'Shape spec of the three-dimensional array is\n {three_dimensional_array.shape}\n')


def demo_array_transpose():
    print('Demo Transpose and Flatten')
    original_array = numpy.array([[1, 2, 3], [4, 5, 6]])
    print(f'Original array is\n {original_array}\n')
    print(f'Shape spec of Original array is\n {original_array.shape}\n')

    transposed_array = numpy.transpose(original_array)
    print(f'Resulting Transposed array is\n {transposed_array}\n')
    print(f'Shape Spec of Resulting Transposed array is\n {transposed_array.shape}\n')

    flattened_array = original_array.flatten()
    print(f'Resulting Flattened array is\n {flattened_array}\n')
    print(f'Shape Spec of Resulting Flattened array is\n {flattened_array.shape}\n')


def demo_concatenate():
    print('Demo Concatenate')

    array_1 = numpy.array([[1, 2, 3],[11,12,13]])
    print(f'First array is\n {array_1}\n')
    array_2 = numpy.array([[4, 5, 6],[14,15,16]])
    print(f'Second array is\n {array_2}\n')
    array_3 = numpy.array([[7, 8, 9],[17,18,19]])
    print(f'Third array is\n {array_3}\n')

    merged_concatenated_array = numpy.concatenate((array_1, array_2, array_3))
    print(f'Resulting merged concatenated array is\n {merged_concatenated_array}\n')


def demo_numpy_arithmetic():
    print('Demo Numpy Arithmetic')
    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7, 8]
    matrix_a = numpy.array(list_a, float)
    matrix_b = numpy.array(list_b, int)
    print(f'a + b = {matrix_a + matrix_b}')
    print(f'a + 1 = {matrix_a + 1}\n')

    print(f'a - b = {matrix_a - matrix_b}')
    print(f'a - 1 = {matrix_a - 1}\n')

    print(f'a * b = {matrix_a * matrix_b}')
    print(f'a * 10 = {matrix_a * 10}\n')

    print(f'a / b = {matrix_a / matrix_b}')
    print(f'a / b = {matrix_a / 10}\n')

    print(f'a raised to the b power is {matrix_a ** matrix_b}')
    print(f'a raised to the 2 power is {matrix_a ** 2}\n')


def demo_round_off():
    print('Demo Round Off (floor, ceil, rint)')
    original_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    print(f'Input original array is {original_array}')
    print(f'Floor set is {numpy.floor(original_array)}')
    print(f'Ceiling set is {numpy.ceil(original_array)}')
    print(f'Real round off set is {numpy.rint(original_array)}')


def demo_statistical_operations():
    print('Demo statistical MIN')
    original_array = numpy.array([[2, 5], [3, 7], [1, 3], [4, 0]])
    print(f'{original_array}')
    print(numpy.min(original_array, axis=0))
    print(numpy.min(original_array, axis=1))
    print(numpy.min(original_array, axis=None))
    print(f'{numpy.min(original_array)}\n')

    print('Demo Statistical MAX')
    print(f'With Axis 0 {numpy.max(original_array, axis=0)}')
    print(f'With Axis 1 {numpy.max(original_array, axis=1)}')
    print(f'With no defined Axis {numpy.max(original_array)}\n')

    print('Demo Statistical Mean')
    print(f'With Axis 0 {numpy.mean(original_array, axis=0)}')
    print(f'With Axis 1 {numpy.mean(original_array, axis=1)}')
    print(f'With no defined Axis {numpy.mean(original_array)}\n')

    print('Demo Statistical Variance')
    print(f'With Axis 0 {numpy.var(original_array, axis=0)}')
    print(f'With Axis 1 {numpy.var(original_array, axis=1)}')
    print(f'With no defined Axis {numpy.var(original_array)}\n')

    print('Demo Statistical Standard Deviation')
    print(f'With Axis 0 {numpy.std(original_array, axis=0)}')
    print(f'With Axis 1 {numpy.std(original_array, axis=1)}')
    print(f'With no definite Axis {numpy.std(original_array)}')


def demo_polynomial():
    print('Demo Polynomial Algebra')

    print('Example 1: Given x1=-1, x2=1, x3=1, x4=10\n '
          'The polynomial is: x^4 - 11x^3 + 9x^2 + 11x - 10 = 0')
    print(f'{numpy.poly([-1, 1, 1, 10])}\n')

    print('Example 2: Polynomial x^2-1 = 0\n '
          'The roots are x1=-1 & x2=1')
    print(f'{numpy.roots([1, 0, -1])}\n')

    print('Example 3: Integral of x^2+x+1 is:\n'
          'x^3/3 + x^2/2 + x + C')
    print(f'{numpy.polyint([1, 1, 1])}\n')

    print('Example 4: Derivative of x^3+x^2+x+1 is:\n'
          '3x^2+2x+1')
    print(f'{numpy.polyder([1, 1, 1, 1])}\n')

    print('Example 5: What is the value of:\n'
          'x^3-2x^2+2 given x=4?')
    print(f'{numpy.polyval([1, -2, 0, 2], 4)}\n')

    print('Example 6: What could be an accurate polynomial for these (x,y) points with'
          'the least square error degree of 2?\n'
          'x^2-3.173*10^-16')
    print(f'{numpy.polyfit([0, 1, -1, 2, -2], [0, 1, 1, 4, 4], 2)}\n')


def demo_linear_algebra():
    print('Demo Linear Algebra')
    print('Given the matrix:')
    print('|1, 2|')
    print('|2, 1|')
    print(f'Determinant is\n {numpy.linalg.det(numpy.array([[1, 2], [2, 1]]))}\n')

    eigenvalues, eigenvectors = numpy.linalg.eig(numpy.array([[1, 2], [2, 1]]))
    print(f'Eigenvalues are\n {eigenvalues}\n')
    print(f'Eigenvectors are\n {eigenvectors}\n')

    print('Multiplicative inverse matrix is\n'
          f'{numpy.linalg.inv(numpy.array([[1, 2], [2, 1]]))}\n')


if __name__ == '__main__':
    choice = input('Enter your demo choice:\n'
                   '1: Demo Numpy Array\n'
                   '2: Demo Numpy Shape\n'
                   '3: Demo Array Transpose\n'
                   '4: Demo Concatenate\n'
                   '5: Demo Numpy Arithmetic\n'
                   '6: Demo Round Off\n'
                   '7: Demo Statistical Operations\n'
                   '8: Demo Polynomial\n'
                   '9: Demo Linear Algebra\n'
                   'Enter your choice number:\t')
    print('\n')
    if 1 == int(choice):
        demo_numpy_array()
    elif 2 == int(choice):
        demo_array_shape()
    elif 3 == int(choice):
        demo_array_transpose()
    elif 4 == int(choice):
        demo_concatenate()
    elif 5 == int(choice):
        demo_numpy_arithmetic()
    elif 6 == int(choice):
        demo_round_off()
    elif 7 == int(choice):
        demo_statistical_operations()
    elif 8 == int(choice):
        demo_polynomial()
    elif 9 == int(choice):
        demo_linear_algebra()
    else:
        print('INVALID CHOICE. Please input only numbers 1-9.')
