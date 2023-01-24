class Stack:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        
        return self.item == []
    def push(self, item):
        self.item.insert(0, item)
    def pop(self):
        return self.item.pop(0)
    def ptin_stack(self):
        print(self.item)
        
#calling function
st = Stack()
st.push('a')
st.push('b')
st.push('c')
st.ptin_stack()
st.pop()
st.ptin_stack()
        