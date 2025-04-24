def Encription(string, shift):
    string_list = [(alphabet[(alphabet.index(sym) + shift) % 26] if sym != " " else " ") for sym in string]
    new_str = ""
    for i in string_list:
        new_str += i
    return new_str

string = input("Input string to encrypt:")
shift = int(input("Input shift value:"))
alphabet = "abcdefghijklmnopqrstuvwxyz"

output = Encription(string, shift)
print("Encrypted string:", output)
