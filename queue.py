
''' Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner.
    With a queue the least recently added item is removed first.
    A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.'''
    
class Queue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size

    def __str__(self):
        myString = ' '.join(str(i) for i in self.queue)
        return myString

    def enqueue(self, item):
        '''This function adds an item to the rear end of the queue '''
        if(self.isFull() != True):
            self.queue.insert(0, item)
        else:
            print('Queue is Full!')

    def dequeue(self):
        ''' This function removes an item from the front end of the queue '''
        if(self.isEmpty() != True):
            return self.queue.pop()
        else:
            print('Queue is Empty!')

    def isEmpty(self):
        ''' This function checks if the queue is empty '''
        return self.queue == []

    def isFull(self):
        ''' This function checks if the queue is full '''
        return len(self.queue) == self.size

    def peek(self):
        ''' This function helps to see the first element at the front end of the queue '''
        if(self.isEmpty() != True):
            return self.queue[-1]
        else:
            print('Queue is Empty!')
            

def main():
    myQueue = Queue(int(input("Enter size of queue : ")))

    while(True):
        print(
            '------------OPERATIONS-----------\n'
            '\t1. enqueue\n'
            '\t2. dequeue\n'
            '\t3. Front of queue\n'
            '\t4. check for empty\n'
            '\t5. check for full\n'
            '\t6. display Queue\n'
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
            msg = myQueue.enqueue(e)
            if msg == -1:
                print('Queue is full item cannot be enqueued!!')
            else:    
                print('item enqueued successfully!!')
        
        #pop operation
        elif ch == 2:
            msg = myQueue.dequeue()
            if msg == -1:
                print('Queue is empty item cannot be dequeued!!')
            else:    
                print(' item dequeued successfully!! \n\n\t item dequeued : ',msg)

        #peek operation
        elif ch == 3:
            print('PEEK SUCCESSFUL! \n\n\t : ',myQueue.peek())

        #isEmpty operation
        elif ch == 4:
            print('QUEUE EMPTY ? : ',myQueue.isEmpty())

        #isFull operation
        elif ch == 5:
            print('QUEUE FULL ? : ',myQueue.isFull())

        #display operation
        elif ch == 6:
            print(myQueue)

        #default operation
        else:
            print('INVALID CHOICE!!!')
        
        print('-'*30,'\n')

#---------------------calling main function----------------------#
if __name__ == '__main__':
    main() 
