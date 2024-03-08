def main(wn, fn, sn, tn):
    phone_numbers = [fn, sn, tn]

    for i in range(len(phone_numbers)):
        if '+' in phone_numbers[i]:
            phone_numbers[i] = phone_numbers[i].replace('+', '')
        if '(' in phone_numbers[i]:
            phone_numbers[i] = phone_numbers[i].replace('(', '')
        if ')' in phone_numbers[i]:
            phone_numbers[i] = phone_numbers[i].replace(')', '')
        if '-' in phone_numbers[i]:
            phone_numbers[i] = phone_numbers[i].replace('-', '')

        # Extract the first digit of the cleaned phone number
        first_digit = phone_numbers[i][0]

        # Check if the first digit is 7 or 8
        if first_digit in ['7', '8']:
            # If it is, remove it from the phone number
            phone_numbers[i] = phone_numbers[i][1:]

    print("Cleaned Phone Numbers:", phone_numbers)

    for number in phone_numbers:
        if wn == number:
            print('YES')
            return 'YES'
    print('NO')
    return 'NO'


main(
    input(),  # Phone number Vasya wants to add
    input(),  # First existing phone number
    input(),  # Second existing phone number
    input()   # Third existing phone number
)

