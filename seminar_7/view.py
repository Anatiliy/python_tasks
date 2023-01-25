


def show(data):
    if data:
        for row in data:
            for item in row:
                print(item.ljust(12), end='')
            print()