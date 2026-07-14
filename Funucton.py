class book:

    def __init__(self, name, writer, pages):
        self.name = name
        self.writer = writer
        self.pages = pages

    def __len__(self):
        return int(self.pages)

b = book ("harrypotter", "J.K. Rowling", 378)

print(len(b))  # accessing private class variable