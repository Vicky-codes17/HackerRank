def split_and_join(line):
    line = line.split()
    return "-".join(line)               # where split(" ") uses divide user input in the list
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)   
    print(result)