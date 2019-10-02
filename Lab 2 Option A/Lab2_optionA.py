# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:30:50 2019

@author: Alexis Navarro
CS2302 - Lab 2 Option A
MW 1:30-2:50 PM
Professor: Diego Aguirre
Purpose: To create a linked lists with data from a text file and understand sorting with the
"""
class Node(object):
   def __init__(self, item, next=None):
       self.item = item
       self.next = next

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None

def is_empty(L):
    return L.head==None

def Append(L,x):
    if is_empty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

def Print(L):
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()


#-------------------------------------------------------------------------------------------------------------------------------------------------
'''
def compare(employees):
    duplicate_list = List()
    temp1=employees
    while temp1 != None:
        temp2 = temp1.next
        while temp2 != None:
                if temp1.item == temp2.item:
                    duplicate_list.append(temp1.item)
                temp2= temp2.next
        temp1= temp1.next
        return employees
'''  
'''
def compare(L):
    dupe_list = List()
    if L.head.item == L.next.item:
        dupe_list.append(L.head.item)
    else:
        compare(L.next)
    return dupe_list
'''

#working bubble sort
def bubble_sort(L):
    change_items=True  #set this to true 
    while change_items:
        t = L.head      #make a temp to store the head
        change_items=False
        while t.next is not None:
            if int(t.item[0]) > int(t.next.item[0]):
                temp = t.item
                t.item = t.next.item
                t.next.item = temp
                change_items = True
            t = t.next

#-------------------------------------------------------------------------------------------------------------------------------------------------
'''

#merge sort that did not work due the error maximum depth reached


def merge_sort(L):
    if L == None or L.next == None:
        return L 

    middle = split(L) #calls the split method to split the linked list by the middle 
    next_middle = middle.next

    middle.next = None
    left = merge_sort(L)
    right = merge_sort(next_middle)

    sorted_list = sorted_merge(left, right) 
    return sorted_list


def split(L):
    fast = L.next #fast and slow refer to the pointer ( slow will always be 1 item behind the fast pointer)
    slow = L      #stores the entire list/ start of the list
    while fast != None: # fast will move up the linked list by two
        fast = fast.next
        if fast != None:
            slow = slow.next # moves slow by 1 till it gets to the middle postion
            fast = fast.next
    return slow


def sorted_merge(left_side,right_side):

    Result=None#List()
    
    if left_side is None:
        return right_side
    
    if right_side is None:
        return left_side

    if left_side <= right_side:
        Result = int(left_side.item[0])
        Result.next = sorted_merge(left_side.next, right_side)
    else:
        Result = right_side
        Result.next = sorted_merge(left_side, right_side.next)

    
    return Result
'''

#Merge sort that does not sort correctly
def Merge(L):
    if is_empty:
        return None
    else:
        Split(L)
        print(L)
    
 #split method that splits the linked list in the middle
def Split(L):
    temp=L.head
    middle=len(L)//2
    
    left=L[middle:]
    right=L[:middle]
    
    i=0#tracking for L1
    j=0#tracking for L2
    k=0#tracking for entire L
    
    while temp is not None:
        while i<len(left) and j<len(right):#if both split lists are less than its length
            if left[i] < right[j]:#if its value is bigger, then will make compare/sort
                L[k]=right[j]
                i+=1
            else:
                L[k]=right[j]
                j+=1
            k+=1
            
            
        while i<len(left):#if L1 index less than length
            L[k]=left[i]
            i+=1
            k+=1
        while j<len(right):#if L2 index less than length
            L[k]=right[i]
            j+=1
            k+=1
    return L



#-------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    #Normal way to append and read the file

    '''
    file_info=[]
    file = open('activision.txt','r')
    line = file.readline()
    while line!='':
        line = line.strip()
        parts=line.split(' ')
        file_info.append(parts)
        line=file.readline()

    print(file_info)
    '''
    
    #Append with linked list
    file_info=List()
    with open("activision.txt","r") as i:
        for line in i:
            line = line.strip()
            parts=line.split(' ')
            Append(file_info,parts)

    #Print(file_info)

    with open("vivendi.txt","r") as j:
        for line in j:
            line = line.strip()
            parts=line.split(' ')
            Append(file_info,parts)
           
    #print("complete: ")
    #Print(file_info) #check to see if the items from txt file are in the linked list
    
    #compare(file_info)
    #bubble_sort(file_info)
    #Merge(file_info)
    Print(file_info)

main()
