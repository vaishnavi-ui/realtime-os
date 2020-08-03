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
        total=1024
        #total=int(input("Enter the TOTAL MEMORY space in the system:"))
        print("The total memory space in KB:",total)
        print("--------------------------------------------")
        if(self.head is None):
            add=node(0,total,'false')
            add.next=None
            self.head=add
            self.marker=self.head
        n=math.ceil(math.log(total)/math.log(2))
        self.allocate(100)
        print("100 K has been allocated")
        print("--------------------------------------------")
        self.display()
        self.allocate(240)
        print("240 K has been allocated")
        print("--------------------------------------------")
        self.display()
        self.allocate(64)
        print("64 K has been allocated")
        print("--------------------------------------------")
        self.display()
        self.allocate(256)
        print("256 K has been allocated")
        print("--------------------------------------------")
        self.display()
        self.deallocate(240)
        print("240 K has been de-allocated")
        print("--------------------------------------------")
        self.combine()
        self.combine()
        self.display()
        self.deallocate(64)
        print("64 K has been de-allocated")
        print("--------------------------------------------")
        self.combine()
        self.combine()
        self.display()
        self.deallocate(100)
        print("100 K has been de-allocated")
        print("--------------------------------------------")
        self.combine()
        self.combine()
        self.display()
        self.deallocate(256)
        print("256 K has been de-allocated")
        print("--------------------------------------------")
        self.combine()
        self.combine()
        self.display()
        '''
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
        '''


def edf():
    tasks=[]
    print("Please Enter the number of tasks:")
    n=int(input())

    for i in range (n):
        tasks.append([])
        tasks[i].append( i+1) 
        print("Please Enter the Execution time of task:",i+1)
        tasks[i].append(int(input()))
        print("Please Enter the Periodicity time of task:",i+1)
        tasks[i].append(int(input()))
        print("Please Enter the Deadline time of task:",i+1)
        tasks[i].append(int(input()))
        print("Please Enter the Arrival time of task:",i+1)
        tasks[i].append(int(input()))

    print (tasks)

    u=0

    for i in range(n):
        u+=float(tasks[i][1]/tasks[i][2])

    print("Utilization: ",u)



    if u>1:
        print("The tasks are not feasible")

    else:

        lcm=1
        temp_p=[]
        for i in range(n):
            temp_p.append(tasks[i][2])


        print(temp_p)
        i=2
        while i <= max(temp_p):
            counter=0
            for j in range(n):
                if temp_p[j]%i==0:
                    counter=1
                    temp_p[j]/=i

            if counter==1:
                lcm=lcm*i
            else:
                i+=1


        print("LCM: ",lcm)

        i=0
        instances=[]
        for i in range(n):
            j=1
            while 1:
                if j*tasks[i][2]<=lcm:
                    instances.append([tasks[i],j*tasks[i][2], (j*tasks[i][2])-(tasks[i][2]-tasks[i][3])])
                    j+=1
                else:
                    break
        
        print()
        print("Processes are divided into time periods")
        print()
        for i in range(len(instances)):
            print(instances[i])


        for i in range(len(instances)):
            tmp = instances[i].copy()
            k = i
            while k > 0 and tmp[2] < instances[k-1][2]:
                instances[k] = instances[k - 1].copy()
                k -= 1
            instances[k] = tmp.copy()


        print()
        print()

        print("Process are sorted according to their deadlines : ")
        print()
        
        for i in range(len(instances)):
            print(instances[i])

        timeLeft=[]

        for i in range(n):
            if tasks[i][4]==0:
                timeLeft.append(tasks[i][1])
            else:
                timeLeft.append(int(0))

        
        timeLine=[]
        time=0


        while time<lcm:
            for i in range(n):
                if time>1 and ((time%tasks[i][2]==0 and time>tasks[i][4]) or time==tasks[i][4]):

                    timeLeft[i]=tasks[i][1]
            anyrun=0
            for j in range(len(instances)):
                if j==0 and timeLeft[instances[j][0][0]-1]>0:
                    timeLine.append(instances[j][0][0])
                    timeLeft[instances[j][0][0]-1]-=1
                    anyrun=1
                    if timeLeft[instances[j][0][0]-1]==0:
                        instances.pop(j)

                    break

                elif j>0 and instances[j][1]==instances[0][1]:
                    if timeLeft[instances[j][0][0]-1]>0:
                        tmp=instances[j].copy()
                        instances[j]=instances[0].copy()
                        instances[0]=tmp.copy()
                        time-=1
                        anyrun=1
                        break
                elif j>0 and timeLeft[instances[j][0][0]-1]>0:
                    timeLine.append(instances[j][0][0])
                    timeLeft[instances[j][0][0]-1]-=1
                    anyrun=1
                    if timeLeft[instances[j][0][0]-1]==0:
                        instances.pop(j)

                    break


            if anyrun==0:
                timeLine.append(0)

            time+=1




        print()
        print()
        print(" GANTT  CHART  :")
        mn=0
        mx=0

        for i in range(lcm):
            if i>0 and timeLine[i]!=timeLine[i-1]:
                mx=i
                if timeLine[i-1] == 0:
                    print(mn," - ",mx," : ", "[ IDLE ]")

                else :

                    print(mn," - ",mx," : ", "[ Process "+str(timeLine[i-1])+"]")
                mn=i
            if i==lcm-1:
                mx=lcm

                if timeLine[i] == 0:
                    print(mn," - ",mx," : ", "[ IDLE ]")

                else:
                    print(mn," - ",mx," : ", "[ Process"+str(timeLine[i])+"]")
                    
                    

def c_look():
    l=[176,79,34,60,92,11,41,114]
    print("Entered Sequence is :-")
    print(l)
    head = int(input("Enter head position "))
    sum=0
    sum1=0
    sum2=0
    l.sort()
    l1=list()
    for x in l:
        if(x<head):
            l1.append(x)
    l3=list()
    l3 = [x for x in l if x not in l1]
    sum=l3[-1]-head
    sum1=l3[-1]-l1[0]
    sum2=l1[-1]-l1[0]
    total=sum+sum1+sum2
    print("Total seek time = ",total)
    print("Seek sequence : ")
    for x in l1:
        l3.append(x)
    for x in l3:
        print(x)



def linked_file_allocation():
    f = [0 for i in range(50)]
    p = int(input("Enter how many blocks that are already allocated\n"))

    print("Enter the blocks no.s that are already allocated")

    for i in range(p):
        a = int(input())
        f[a] = 1

    def X(f):
        print("Enter the starting index block & length")
        inp = input().split()
        inp = list(map(int,inp))
        st = inp[0]
        length = inp[1]
        k = length
        
        j = st
        
        while j<(k+st):
            if f[j] == 0:
                f[j] = 1
                print(j,"->",f[j])
            else:
                print("{0}->file is already allocated".format(j))
                k+=1
            j+=1
    c = 1    
    while c != 0:
        X(f)
        c = int(input("If u want to enter one more file? (yes-1/no-0)\n"))



while 1:
    
    choice = int(input("Enter 1 for process management \nEnter 2 for memory management \nEnter 3 for file management \nEnter 4 for I/O management\nEnter 5 to quit\n"))
    
    if choice == 1:
        edf()
        
    elif choice == 2:
        l=LinkedList()
        l.control()
        
    elif choice == 3:
        linked_file_allocation()
        
    elif choice == 4:
        c_look()
    
    elif choice == 5:
        break
        
    else :
        print("Invalid choice . Enter again")
    

        


    




    
    






    
    



            








