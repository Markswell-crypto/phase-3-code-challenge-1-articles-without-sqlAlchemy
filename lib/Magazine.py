class Magazine:
    magazines = []

    def __init__(self, name, category):
        self.mag_name = name
        self.mag_category = category
        Magazine.magazines.append(self)

    def name(self):
        return self.mag_name

    def category(self):
        return self.mag_category

    def all(self):
        return self.magazines
    
    def set_name(self, new_name):
        self.mag_name = new_name
        
    def set_category(self, new_category):
        self.mag_category = new_category
    def __str__(self):
        return f"Magazine Name: {self.mag_name} Magazine Category: {self.mag_category}"


# Example usage:

# Create Magazine instances
magazine1 = Magazine("Tech Magazine", "Technology")
magazine2 = Magazine("Fashion Weekly", "Fashion")

# Accessing the name and category
print(magazine1.name())  # Output: Tech Magazine
print(magazine1.category())  # Output: Technology

# Changing the name and category
magazine1.set_name("New Tech Magazine")
magazine1.set_category("Innovation")

# Accessing the updated name and category
print(magazine1.name())  # Output: New Tech Magazine
print(magazine1.category())  # Output: Innovation

# class Magazine:
#     magazines = []

#     def __init__(self, name, category):
#         self.mag_name = name
#         self.mag_category = category
#         self.articles_written = []
#         Magazine.magazines.append(self)

#     def name(self):
#         return self.mag_name

#     def category(self):
#         return self.mag_category

#     def all(self):
#         return Magazine.magazines
    
#     def set_name(self, new_name):
#         self.mag_name = new_name
        
#     def set_category(self, new_category):
#         self.mag_category = new_category  

#     @classmethod
#     def find_by_name(cls, name):
#         for magazine in cls.magazines:
#             if magazine.name() == name:
#                 return magazine
#         return None

#     @classmethod
#     def article_titles(cls, name):
#         magazine = cls.find_by_name(name)
#         if magazine:
#             return [article.title() for article in magazine.articles_written]
#         return []

#     def contributing_authors(self):
#         authors_count = {}
#         for article in self.articles_written:
#             author = article._author
#             if author in authors_count:
#                 authors_count[author] += 1
#             else:
#                 authors_count[author] = 1

#         return [author for author, count in authors_count.items() if count > 2]