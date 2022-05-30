class Criteria(object):
    def __init__(self, name):
        self.name = name
        self.desc = None
        self.sub_criteria = []
        self.priority = None

    def add_sub_criteria(self, sub_criteria):
        self.sub_criteria.append(sub_criteria)

    def validate_have_sub_criteria(self, have_sub_criteria):
        if have_sub_criteria == "y" or have_sub_criteria == "n":
            return True
        else:
            return False
        
    def validate_desc(self, desc):
        if desc == "profit" or desc == "loss":
            return True
        else:
            return False
    
    def validate_priority(self, priority):
        if priority >= 1 and priority <= 100:
            return True
        else:
            return False
        
        