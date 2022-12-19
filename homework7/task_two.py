right_angled = {
    'result': True,
    'description': 'the triangle is right-angled'
}
not_right_angled = {
    'result': False,
    'description': 'the triangle is not right-angled'
}
triangle_exists = {
    'result': False,
    'description': 'no such triangle exists'
}


def is_right_angle_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a ^ 2 + b ^ 2 == c ^ 2:
            return right_angled
        else:
            return not_right_angled
    else:
        return triangle_exists


result = is_right_angle_triangle(11, 11, 21)
print(result)
