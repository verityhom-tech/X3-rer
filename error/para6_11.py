class ForbiddenError(Exception):
    def __str__(self):
        return f"With so 13"


def check_material(number):
    if 13 in str(number):
        raise ForbiddenError(number)
    else:
        raise number

material = 1
check_material(material)
