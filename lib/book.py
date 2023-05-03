#!/usr/bin/env python3
import ipdb

class Book:
    
    def __init__(self, title, page_count = 0):
        self.title = title
        self.page_count = page_count

    def get_page_count(self):
        print('Inside the getter')
        return self._page_count
    
    def set_page_count(self, page_count):
        if type(page_count) == int:
            print('Inside the setter')
            self._page_count = page_count
        else: 
            print("page_count must be an integer")
        
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_page_count, set_page_count)

# ipdb.set_trace()