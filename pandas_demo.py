import numpy
import pandas


def demo_panda_series():
    print(f'{pandas.Series(numpy.array([13, 25, 19, 143, 14344]))}\n')
    print(f'{pandas.Series(numpy.array([1000,2000,3000,5000]),["Manila","Pune","Elgin","Belgrade"])}\n')


def demo_data_frame_movies():
    data_frame_list = pandas.DataFrame([
        ["The Exorcist", 1973, 500000000],
        ["Barbie", 2023, 1300000000],
        ["The Lion King", 2019, 1200000000]
    ], columns=["movie", "release year", "gross"])
    print(f'Movie Box Office Table\n'
          f'{data_frame_list}\n')
    print(f'Movie Box Office Table without index\n'
          f'{data_frame_list.set_index("movie")}\n')
    print(f'Barbie Box Office\n'
          f'{data_frame_list[1:2]}')
    print(f'Sort Box Office by year\n'
          f'{data_frame_list.sort_values(by="release year").set_index("movie")}')


def demo_data_frame_tv():
    data_frame_dict = pandas.DataFrame(
        {
            'Morning': [4.0, 3.2, 1.1, 5.3],
            'Afternoon': [3.6, 4.2, 2.8, 2.6],
            'Evening': [2.3, 1.1, 2.1, 3.0]
        }, index=['TV2', 'TV5', 'TV7', 'TV13'])
    print(f'TV ratings data\n'
          f'{data_frame_dict}\n')
    print(f'TV ratings statistics\n'
          f'{data_frame_dict.describe()}\n')
    print(f'TV ratings times 10\n'
          f'{data_frame_dict.transform(lambda x: x*10)}')
    print(f'Convert panda data to numpy data\n'
          f'{data_frame_dict.to_numpy()}')
    print(f'Convert panda data to csv\n'
          f'{data_frame_dict.to_csv()}')


def demo_histogram():
    data = numpy.random.randint(0, 7, size=50)
    print(f'Input data series is\n{data}\n')
    table = pandas.Series(data)
    print(f'Histogram:\n{table.value_counts()}\n')


if __name__ == '__main__':
    choice = input('Enter your demo choice:\n'
                   '1: Demo Panda Series\n'
                   '2: Demo Data Frame using Movie box-office example\n'
                   '3: Demo Data Frame using TV ratings example\n'
                   '4: Demo Histogram\n'
                   'Enter your choice number:\t')
    print('\n')
    if 1 == int(choice):
        demo_panda_series()
    elif 2 == int(choice):
        demo_data_frame_movies()
    elif 3 == int(choice):
        demo_data_frame_tv()
    elif 4 == int(choice):
        demo_histogram()
    else:
        print('INVALID CHOICE. Please input only numbers 1-9.')
