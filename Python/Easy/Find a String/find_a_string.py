def count_substring(string, sub_string):
    count = 0
    length = len(string)
    sub_string_length = len(sub_string)
    for i in range(length + 1 - sub_string_length):
        if string[i:i + sub_string_length] == sub_string:
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)