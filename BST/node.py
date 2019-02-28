class node(object):
    def __init__(self, key, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.key = key


def main():
    a = node(10)
    print(a.__dict__)
    return 0


if __name__ == '__main__':
    main()