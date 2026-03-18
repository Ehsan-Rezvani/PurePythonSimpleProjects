def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    try:
        main_digits = isbn[:-1] 
        given_check_digit = isbn[-1]

        main_digits_list = [int(digit) for digit in main_digits]
        
        if length == 10:
            expected_check_digit = calculate_check_digit_10(main_digits_list)
        else:
            expected_check_digit = calculate_check_digit_13(main_digits_list)

        if str(given_check_digit) == str(expected_check_digit):
            print('Valid ISBN Code.')
        else:
            print('Invalid ISBN Code.')
            
    except ValueError:
        print('Invalid character was found.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    
    result = (11 - (digits_sum % 11)) % 11
    if result == 10:
        return 'X'
    return str(result)

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    
    result = (10 - (digits_sum % 10)) % 10
    return str(result)

def main():
    user_input = input('Enter ISBN and length: ')
    
    if ',' not in user_input:
        print('Enter comma-separated values.')
        return

    values = user_input.split(',')
    isbn = values[0].strip()
    
    try:
        length = int(values[1].strip())
    except ValueError:
        print('Length must be a number.')
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

if __name__ == '__main__':
    main()
