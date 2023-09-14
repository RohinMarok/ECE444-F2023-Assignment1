class NumberUtils:
    
    def reverse_integer(number):
        if number < 0:
            sign = -1
            number = abs(number)
        else:
            sign = 1

        reversed_string = str(number)[::-1]
        reversed_number = int(reversed_string)
        reversed_number *= sign

        return reversed_number

    def format_to_binary_and_octal(number):
        binary_representation = bin(number)
        octal_representation = oct(number)

        return binary_representation, octal_representation