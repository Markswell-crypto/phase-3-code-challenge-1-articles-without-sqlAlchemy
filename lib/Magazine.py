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

