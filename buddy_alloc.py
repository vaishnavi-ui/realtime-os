class node:
    def __init__(self,reqd,space,flag):
        self.reqd=reqd
        self.space=space
        self.flag=flag
        self.next=None
import math
class LinkedList:
    def __init__(self):
        self.head=None
        self.marker=None
        
    def allocate(self,s):
        temp=self.head
        prev=self.head
        t=0
        n=0
        k=0
        while(temp is not None):
            if(s<=temp.space and temp.flag =='false'):
                n=math.ceil(math.log(temp.space)/math.log(2))
                if(s>math.pow(2,n-1)):
                    temp.reqd=s
                    temp.flag='true'
                    break
                else:
                    t=temp.space/2
                    add=node(0,t,'false')
                    add.next=temp
                    temp.space=t
                    if(k==0):
                        self.head=add
                        temp=self.head
                    elif (k>0):
                        prev.next=add
                        temp=add
            else:
                prev=temp
                temp=temp.next
                k+=1
        if(temp is None):
            print("\n")
            print(s," can't be allocated!")
            print("\n")
            
    def deallocate(self,s):
        self.combine()
        temp=self.head
        while(temp is not None):
            if(temp.reqd==s and temp.flag=='true'):
                temp.reqd=0
                temp.flag='false'
                break
            temp=temp.next
        if(temp is None):
            print("\n")
            print(s,"can't be de allocated")
            print("\n")
        self.combine()
    def combine(self):
        temp=self.head
        temp2=self.head
        while(temp.next is not None):
            temp2=temp.next
            if(temp.reqd==0 and temp2.reqd==0 and temp.flag=='false' and temp2.flag=='false'):
                if(temp.space==temp2.space and temp is not self.marker):
                    temp.space=temp.space+temp2.space
                    temp.next=temp2.next
                    break
            temp=temp.next
    def display(self):
        self.combine()
        temp=self.head
        left=0
        k=0
        print("M E M O R Y  A L L O C A T I O N !")
        while(temp is not None):
            print("Memory space of: ",temp.space,end=" ")
            if(temp.flag =='true'):
                k=temp.space-temp.reqd
                left+=k
                print("is occupied with:",temp.reqd)
            else:
                left+=temp.space
                print("is empty")
            temp=temp.next
            print("--------------------------------------------")
        print("Total unused spaces are->",left)
        print("\n")
        
    def control(self):
        total=0
        total=int(input("Enter the TOTAL MEMORY space in the system:"))
        print("--------------------------------------------")
        if(self.head is None):
            add=node(0,total,'false')
            add.next=None
            self.head=add
            self.marker=self.head
        n=math.ceil(math.log(total)/math.log(2))
        ch=0
        while(ch!=4):
            print("Make a choice from the following menu->")
            print("1.Allocation to memory")
            print("2.De-allocation from memory")
            print("3.Display")
            print("4.Exit")
            print("--------------------------------------------")
            ch=int(input("Enter  choice-->"))
            print("--------------------------------------------")
            if(ch==1):
                c=int(input("Enter size of the memory to be allocated:"))
                self.allocate(c)
            elif(ch==2):
                c=int(input("Enter the size of the memory to be de-allocated:"))
                self.deallocate(c)
                self.combine()
            elif(ch==3):
                self.combine()
                self.display()
            elif(ch==4):
                print("The program is exited")
                break
            else:
                print("Your choice is invalid")
l=LinkedList()
l.control()
            
    
