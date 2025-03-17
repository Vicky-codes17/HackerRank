def swap_case(s):
    s=list(s)
    for index in range(len(s)):
        if s[index].islower():
            s[index] = s[index].upper()
        else:
            s[index]=s[index].lower() 
    return "".join(s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)