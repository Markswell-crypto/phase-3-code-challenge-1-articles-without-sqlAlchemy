from Author import Author
from Magazine import Magazine

class Article:
    articles = []

    def __init__(self, author, magazine, title):
        self.author_name = author
        self.magazine_name = magazine
        self.title_mag = title
        Article.articles.append(self)

    def title(self):
        return self.title_mag

    def all_articles(self):
        return self.articles
    def __str__(self):
        return f"Author: {self.author_name} Magazine: {self.magazine_name} Title: {self.title_mag}"
    
# Create instances for testing
author1 = Author("John Doe")
magazine1 = Magazine("Tech Magazine", "Technology")

# Test Case 1: Creating an Article
article1 = Article(author1, magazine1, "The Future of AI")

# Test Case 2: Accessing the title of the article
print(article1.title()) 

# Test Case 3: Accessing all articles
for article_info in Article.articles:
    print(article_info) 
