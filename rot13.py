alphabets = ["A", "B", "C", "D", "E", "F",
             "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

rot_13_dict = ["N", "O", "P", "Q", "R", "S",
               "T", "U", "V", "W", "X", "Y", "Z",
               "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]


def rot13(message):
    results = []
    message_copy = list(message)
    print(message_copy)

    for l in message_copy:
        try:
            index = alphabets.index(l.upper())  # get index of the letter from the alphabets list.
            if l == alphabets[index]:  # if the letter is uppercase append it's R0T13 equivalent as uppercase.
                results.append(rot_13_dict[index])
            else:  # # if the letter is lowercase append it's R0T13 equivalent as lowercase.
                results.append((rot_13_dict[index]).lower())
        except ValueError:  # append the member as it is if not an alphabet
            results.append(l)

    return ''.join(results)


print(rot13("aA bB zZ 1234 *!?%"))

# test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
# test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
# test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')
