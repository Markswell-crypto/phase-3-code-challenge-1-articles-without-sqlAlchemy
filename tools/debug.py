from Author import Author
from Article import Article
from Magazine import Magazine

# Test Cases
author1 = Author("John Doe")
author2 = Author("Jane Smith")

magazine1 = Magazine("Tech Magazine", "Technology")
magazine2 = Magazine("Science Journal", "Science")

# Adding articles
article1 = author1.add_article(magazine1, "Python Programming")
article2 = author2.add_article(magazine1, "Machine Learning Basics")
article3 = author1.add_article(magazine2, "Theories of Relativity")

# Changing magazine name and category
magazine1.set_name("New Tech Magazine")
magazine1.set_category("New Technology")

# Find magazine by name
found_magazine = Magazine.find_by_name("New Tech Magazine")
print(found_magazine.name())  # Output: New Tech Magazine

# Get article titles for a magazine
titles = Magazine.article_titles("New Tech Magazine")
print(titles)  # Output: ['Python Programming', 'Machine Learning Basics']

# Get contributing authors for a magazine
contributing_authors = magazine1.contributing_authors()
print([author.author_name for author in contributing_authors])  # Output: ['John Doe']
