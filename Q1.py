
def f_A(s):
    # reverse a string
    return s[::-1]

def f_B(s):
    # reverse a string while keeping the word order
    rev_words = [w[::-1] for w in s.split(" ")]

    return " ".join(rev_words)



def main():
    st = "qwer asdf 123"
    print(f_A(st))
    print(f_B(st))


if __name__ == "__main__":
    main()