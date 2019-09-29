#!/usr/local/bin/python3.7

import csv
import os
import sys
import time
from Zine import Zine
from Library import Library

def main(new_file, old_file):
    old_library = build_old_library(old_file)
    new_library = build_new_library(new_file)

    for entry in new_library.entries:
        match = old_library.find_entry_by_title(entry.title)
        if match != "Not Found":
            #print(match.title, entry.title, match.catalog_number)
            print(True)
        else:
            print("")


def build_new_library(new_file):
    library = Library()
    with open(new_file, newline='') as csvfile:
        filereader = csv.DictReader(csvfile)
        for row in filereader:
            title = row['Title']
            catalog_number = ""
            author = row['Creator(s)']
            keywords = row['Keywords']
            entry = Zine(title, catalog_number, author, keywords)
            library.add_entry(entry)
    return library

def build_old_library(old_file):
    library = Library()
    with open(old_file, newline='') as csvfile:
        filereader = csv.DictReader(csvfile)
        for row in filereader:
            title = row['Title']
            catalog_number = row['Catalog #']
            author = row['Author']
            entry = Zine(title, catalog_number, author, "")
            library.add_entry(entry)
    return library

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Be sure you include the relative path to the new sheet and old sheet inputs respectively")