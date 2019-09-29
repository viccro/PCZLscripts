import string

class Zine:
    def __init__(self, title, catalog_number, author, keywords):
        self.title = title
        self.catalog_number = catalog_number
        self.author = author
        self.keywords = keywords

    def __str__(self):
        return self.catalog_number + ": " + self.title + " by " + self.author