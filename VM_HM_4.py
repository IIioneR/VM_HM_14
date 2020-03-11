
def more_than_0(n):
    return n > 0


print(more_than_0(3))


def number_to_0(n):
    if n == 0:
        return 0
    print(n, end=' ')
    return number_to_0(n-1)


print(number_to_0(10))


def story(st):
    bad_words = ["an", "a", "the"]
    words = st.split()
    for i in words:
        if i in bad_words:
            i = ""
        print(i, end=' ')


print(story("the different an apple. a job, aaa"))


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(e)


print(division(5, 2))

