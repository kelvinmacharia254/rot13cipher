def rot13_fn(message: str) -> str:
    alphabets = ["A", "B", "C", "D", "E", "F",
                 "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    rot_13_dict = ["N", "O", "P", "Q", "R", "S",
                   "T", "U", "V", "W", "X", "Y", "Z",
                   "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    results = []
    message_copy_as_lst = list(message)

    for l in message_copy_as_lst:
        try:
            index = alphabets.index(l.upper())  # get index of the letter from the alphabets list.
            if l == alphabets[index]:  # if the letter is uppercase append it's R0T13 equivalent as uppercase.
                results.append(rot_13_dict[index])
            else:  # if the letter is lowercase append it's R0T13 equivalent as lowercase.
                results.append((rot_13_dict[index]).lower())
        except ValueError:  # append the element as it is if not a latin/english alphabet
            results.append(l)

    return ''.join(results)

input = "ahaha$!"
if __name__ == "__main__":
    result = rot13_fn(input)
    print(f"'{input}' is encrypted to '{result}' by ROT-13 Cipher.")
