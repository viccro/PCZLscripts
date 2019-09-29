import string

class Library:
    def __init__(self, entries):
        self.entries = entries

    def __init__(self):
        self.entries = list()

    def add_entry(self, entry):
        self.entries.append(entry)

    def __str__(self):
        for entry in self.entries:
            print(entry)

    def find_entry_by_title(self,query_title):
        query_title_clean = query_title.translate(str.maketrans('', '', string.whitespace))\
            .translate(str.maketrans('', '', string.punctuation))\
            .lower()

        for entry in self.entries:
            entry_title_clean = entry.title.translate(str.maketrans('', '', string.whitespace)) \
                .translate(str.maketrans('', '', string.punctuation)) \
                .lower()
            if query_title_clean in entry_title_clean:
                return entry
        return "Not Found"