def convert_pass(password, c_status):
    c = ord('}')  
    text = ""

    for char in password:
        if c_status == "E":  # Encryption
            num = ord(char)  
            value2 = num + c  
            text2 = chr(value2)  
        elif c_status == "D":  
            num = ord(char)
            value2 = num - c  
            # Check if value2 is within the valid range
            if 0 <= value2 <= 255:
                text2 = chr(value2)  
            else:
                text2 = char  # If out of range, keep the original character

        text += text2  # Append the processed character to the result

    return text