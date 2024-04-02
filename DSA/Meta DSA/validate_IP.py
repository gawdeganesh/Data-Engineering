def validate_IP(queryIP):
    def is_valid_IPv4(s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except ValueError:
            return False

    def is_valid_IPv6(s):
        if len(s) > 4:
            return False
        try:
            int(s, 16)
            return True
        except ValueError:
            return False

    if queryIP.count(".") == 3 and all(is_valid_IPv4(part) for part in queryIP.split(".")):
        return "IPv4"
    elif queryIP.count(":") == 7 and all(is_valid_IPv6(part) for part in queryIP.split(":")):
        return "IPv6"
    else:
        return "Neither"

# Example usage
# print(validate_IP("192.168.1.1"))  # IPv4
# print(validate_IP("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # IPv6
# print(validate_IP("192.168@1.1"))  # Neither
print(validate_IP("02001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Neither
# print(validate_IP("192.168.01.01"))  # Expected to print "Neither"
