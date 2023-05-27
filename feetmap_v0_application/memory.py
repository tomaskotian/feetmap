
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

def Convert(buffer):
    if buffer == None:
        return [0,0,0,0,0]
    tmp = [0,0,0,0,0]
    for val in buffer:
        print(buffer)
        if int(val.split()[0][3:]) == 0:
            continue
        tmp[int(val[1])-1] = round(((int(val.split()[0][3:]))-992875)/250,0)
    return tmp