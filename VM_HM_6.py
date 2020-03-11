def decorator(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print(result)
        return result

    return wrapper


@decorator
def sum(a, b):
    return a + b


sum(5, 7)


@decorator
def dif(n, m):
    return n > m

dif(8, 6)


def read_line(file):
    result = []
    result2 = []
    with open(file, 'r') as file:
        for line in file.readlines():
            person_words = line.split(',')
            person_words[2] = person_words[2].replace('\n', '')
            if person_words[0].isalpha() and person_words[1].isalpha() and person_words[2].isnumeric():
                person = {
                    "name":person_words[0],
                    "surname":person_words[1],
                    "age":person_words[2]
                }
                result.append(person)
            else:
                person2 = {
                    "name": person_words[0],
                    "surname": person_words[1],
                    "age": person_words[2]
                }
                result2.append(person2)
                print("!wrongDATA!",end=" ")
                print(person2,end=" ")
        print()
        print("_______"*25)
    return result

print(read_line('test'))