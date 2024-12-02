def convert_pass(password, c_status):
    c = ord('}')  # ASCII value of '}'
    text = ""

    for char in password:
        if c_status == "E":  # Encryption
            num = ord(char)  # Get ASCII value of the character
            value2 = num + c  # Increase by ASCII value of '}'
            text2 = chr(value2)  # Convert back to character
        elif c_status == "D":  # Decryption
            num = ord(char)
            value2 = num - c  # Decrease by ASCII value of '}'
            # Check if value2 is within the valid range
            if 0 <= value2 <= 255:
                text2 = chr(value2)  # Convert back to character
            else:
                text2 = char  # If out of range, keep the original character

        text += text2  # Append the processed character to the result

    return text