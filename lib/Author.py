class Author:
    authors = [] 

    def __init__(self, name):
        self.author_name = name
        Author.authors.append(self) 
    
    def name(self):
        return self.author_name

