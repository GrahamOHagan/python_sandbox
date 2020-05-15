stuff = ["abc", "def", "ghi", "jkl", "mno", "pqr"]


def example(i, x={}):
    x[i] = stuff[i]
    print(x)
    return x


def another(i):
    x = {}
    x[i] = stuff[i]
    print(x)
    return x


if __name__ == "__main__":
    for i in range(6):
        mydict = example(i)
    print()
    for i in range(6):
        mydict2 = another(i)

"""
Output:
{0: 'abc'}
{0: 'abc', 1: 'def'}
{0: 'abc', 1: 'def', 2: 'ghi'}
{0: 'abc', 1: 'def', 2: 'ghi', 3: 'jkl'}
{0: 'abc', 1: 'def', 2: 'ghi', 3: 'jkl', 4: 'mno'}
{0: 'abc', 1: 'def', 2: 'ghi', 3: 'jkl', 4: 'mno', 5: 'pqr'}

{0: 'abc'}
{1: 'def'}
{2: 'ghi'}
{3: 'jkl'}
{4: 'mno'}
{5: 'pqr'}
"""
