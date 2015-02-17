def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

def ask_me():
    user_input = raw_input("What card number would you like to validate?");
    card_validation = is_luhn_valid(user_input)
    validation_text = "valid" if card_validation == True else "invalid";
    print "The card you input was " + validation_text;
    user_input2 = raw_input("Would you like to check on another? (Y/n)") or "y";
    if user_input2 == "y":
        ask_me();

ask_me();
