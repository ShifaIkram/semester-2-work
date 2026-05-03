# Task#3
# Decimal to Hexadecimal Conversion using UDF and error handling

def dec_to_hex(number):
    try:
        # Convert the decimal number to hexadecimal
        hex_value = hex(number)[2:].upper()       #hex() returns a string starting with '0x', i.e. 0xff
        print(f"Hexadecimal equivalent: {hex_value}")    #so using [2:] to clean it up
        print("UDF call successfully")

        return hex_value

    except TypeError:
        # This handles cases where the input is not an integer(string/float)
        print("Error: You must provide an integer. Strings or floats are not supported.")

# Self Testing the Program
# Successful Call
print("Test 1 (Valid Input):")
dec_to_hex(270)
print("-" * 20)

# Call with String (Triggers TypeError)
print("Test 2 (String Input):")
dec_to_hex("100")