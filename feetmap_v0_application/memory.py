
class Memory:
    """
    data consist of Record 
    """
    data = []
    def Add(self,right,left):
        if len(self.data) > 100:
            del self.data[0]
        self.data.append(Record(right,left))

class Record:
    def __init__(self,right,left):
        self.right = right
        self.left = left    