class linked_list:
    def __init__(self):
        self.lim=[]
    def push(self,value):
        self.lim.append(value)

    def pop(self):
        if len(self.lim)==0:
           return None
        return self.lim.pop()

    def length(self):
        return len(self.lim)
    
    def show(self):
        try:
            print(self.lim[len(self.lim)-1])
            return None
        except:
            print(""""
    +---|
    |   GAME OVER
    |  
    |  
    ===
    """)
        
       
        




