def consistent_str_to_int_conversion(f_value:str)->int:
    """
        Check if str value is a consistent value (integer > 0) for this application. If value is consistent function returns
        integer else -1.
    :param f_value: string to convert into a valid integer.
    :return: int value converted or -1 if value is not consistent for application.
    """
    try:
        ret_value = int(f_value)
    except ValueError:
        print("Not a number")
        ret_value = -1
    else:
        if f_value < 0:
            ret_value = -1
            raise ValueError("Number should be higher than 0")
    finally:
        return ret_value

