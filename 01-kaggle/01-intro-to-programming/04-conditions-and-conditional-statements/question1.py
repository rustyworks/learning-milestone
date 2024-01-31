def get_grade(score):
    mapper = {
        'lambda x: 90 <= x <= 100': 'A',
        'lambda x: 80 <= x <= 89': 'B',
        'lambda x: 70 <= x <= 100': 'C',
        'lambda x: 60 <= x <= 100': 'D',
        'lambda x: x < 60 ': 'F',
    }
    for function in mapper:
        if (eval(function))(score):
            return mapper[function]


if __name__ == '__main__':
    print(get_grade(90))
    print(get_grade(70))
    print(get_grade(58))
