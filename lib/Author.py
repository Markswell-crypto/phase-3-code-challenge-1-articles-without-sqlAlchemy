class Author:
    authors = [] 

    def __init__(self, name):
        self.author_name = name
        Author.authors.append(self) 
    
    def __str__(self):
        return f"Author: {self.author_name}"

# Create an instance for testing
author1 = Author("Ogutu")
author2 = Author("Max")

for author in Author.authors:
    print(author)  

