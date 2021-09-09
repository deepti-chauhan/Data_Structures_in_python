#Program to implement Stack
#creating a class Stack
class Stack:
    #size(int) : for size of the stack   
    def __init__(self,size):
        self.size = size
        self.top = -1   #initial value of top also means that the stack is empty
        self.st = [' ']*size   #creating a list of SIZE : size with value ' '

    #returns boolean value: True if stack is Empty else False
    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    #returns boolean value: True if stack is Full else False
    def isFull(self):
        if self.top == self.size-1:
            return True
        return False

    '''
    function to push an element to the stack
            returns -1 if stack is full
            else returns None and appends the el to the list 
    '''
    def push(self,el):
        if self.isFull():
            return -1

        self.top += 1
        self.st[self.top] = el

    '''
    function to pop an element from the stack
            returns -1 if stack is empty
            else returns stack[top] then  decrements top  
    '''
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            temp = self.st[self.top]
            self.top -= 1
            return temp
    '''
    function to fetch the element at top of stack
            returns -1 if stack is empty
            else returns stack[top]
    '''
    def peek(self):
        if self.isEmpty():
            return -1
        return self.st[self.top]

    #overriding the __str__() method
    def __str__(self):
        string = str()
        ptr = -1
        for i in range(self.size+1):
            ptr += 1
            if ptr <= self.top:
                string += f'\t  {self.st[ptr]}\n'
            else:
                string +='\n'
        return string


#--------------------------------------main function----------------------------------------#
def main():
    stack = Stack(int(input('Enter the size of stack : ')))

    while(True):
        print(
            '------------OPERATIONS-----------\n'
            '\t1. push\n'
            '\t2. pop\n'
            '\t3. top of stack\n'
            '\t4. check for empty\n'
            '\t5. check for full\n'
            '\t6. display stack\n'
            '---------------------------------\n'
        )
        #for performing certain operations make a choice
        ch = int(input('Enter your choice(0 to exit) : '))

        print('\n','-'*35)
        #breaking condition
        if ch == 0:
            break

        #push operation
        elif ch == 1:
            e = (input('Enter the element : '))
            msg = stack.push(e)
            if msg == -1:
                print('Stack is full item cannot be push!!')
            else:    
                print('item pushed successfully!!')
        
        #pop operation
        elif ch == 2:
            msg = stack.pop()
            if msg == -1:
                print('Stack is empty item cannot be popped!!')
            else:    
                print(' item popped successfully!! \n\n\t item pop : ',msg)

        #peek operation
        elif ch == 3:
            print('PEEK SUCCESSFUL! \n\n\tSTACK[TOP] : ',stack.peek())

        #isEmpty operation
        elif ch == 4:
            print('STACK EMPTY ? : ',stack.isEmpty())

        #isFull operation
        elif ch == 5:
            print('STACK FULL ? : ',stack.isFull())

        #display operation
        elif ch == 6:
            print('STACK SIZE : ',stack.size)
            print(stack)

        #default operation
        else:
            print('INVALID CHOICE!!!')
        
        print('-'*30,'\n')

#---------------------calling main function----------------------#
if __name__ == '__main__':
    main() 