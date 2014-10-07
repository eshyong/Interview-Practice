def palind_in_str(string):
    i = 0
    largest = ''
    while i < len(string):
        # Check for substrings with i as the middle.
        left, right = i - 1, i + 1
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        substr1 = string[left+1:right]

        # Check for substrings with i, i+1 as the middle.
        substr2 = ''
        if i < len(string) - 1 and string[i] == string[i+1]:
            left, right = i - 1, i + 2
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1
            substr2 = string[left+1:right]

        # print('1: ' + substr1 + ', 2: ' + substr2)

        if len(substr1) > len(substr2) and len(largest) < len(substr1):
            largest = substr1
        elif len(substr2) > len(substr1) and len(largest) < len(substr2):
            largest = substr2

        i += 1
    return largest


while True:
    input_str = raw_input()
    print(palind_in_str(input_str))
