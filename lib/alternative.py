class Alternative(object):
    def __init__(self, name):
        self.name = name
        self.attribute = []
        
    def add_attribute(self, attribute):
        self.attribute.append(attribute)