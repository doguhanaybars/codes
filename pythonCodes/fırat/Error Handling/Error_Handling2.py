
def sum(num1, num2):
    try:
        return num1 + num2
    # aynı zamanda errorları birleştirebiliriz. şöyle ki except (TypeError, ZeroDivisionError): yazdığım zaman iki errorda da alttaki işlemi yapacaktır.
    except TypeError as err:
        return f"Please enter numbers. \n{err}"


print(sum("1", 2))
