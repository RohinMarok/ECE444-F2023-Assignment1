class Utils:
    def reversed(number):
        """Reverses an integer."""
        if not isinstance(number, int):
            raise ValueError("Input must be an integer.")

        if number < 0:
            sign = -1
            number = abs(number)
        else:
            sign = 1

        reversed_string = str(number)[::-1]
        reversed_number = int(reversed_string)
        reversed_number *= sign

        return reversed_number

    def formatter(number):
        """Returns a number in base 2 (binary) and base 8 (octal) format."""
        if not isinstance(number, int):
            raise ValueError("Input must be an integer.")
        
        binary_representation = bin(number)
        octal_representation = oct(number)

        return binary_representation, octal_representation
