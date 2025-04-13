def count_letter(lst, letter):
    count = 0
    for word in lst:
        if letter in word:
            count += 1
    return count

print(count_letter(['python', 'c++', 'c', 'scala', 'java'], 'c'))