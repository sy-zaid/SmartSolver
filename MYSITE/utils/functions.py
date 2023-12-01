

def counttheletters(string):
    count = 0
    for i in string:
        if i != ' ':
            count += 1

    return str(count)
