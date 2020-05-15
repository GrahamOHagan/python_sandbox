stuff = ["abc", "def", "ghi", "jkl", "mno", "pqr"]


def example(i, x={}):
    x[i] = stuff[i]
    return x


if __name__ == "__main__":
    for i in range(6):
        mydict = example(i)
        print(mydict)

"""
Output:
{0: 'abc'}
{0: 'abc', 1: 'def'}
{0: 'abc', 1: 'def', 2: 'ghi'}
{0: 'abc', 1: 'def', 2: 'ghi', 3: 'jkl'}
{0: 'abc', 1: 'def', 2: 'ghi', 3: 'jkl', 4: 'mno'}
{0: 'abc', 1: 'def', 2: 'ghi', 3: 'jkl', 4: 'mno', 5: 'pqr'}
"""
