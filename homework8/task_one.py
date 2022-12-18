input_list = ['Hello', 'world']


def text_up(func):
    def wrapper(*args, **kwargs):
        result_upper = func(*args, **kwargs).upper()
        print(result_upper)
        return result_upper
    return wrapper


@text_up
def get_text(list_str):
    result_text = (' ').join(list_str)
    print(result_text)
    return result_text


get_text(input_list)
