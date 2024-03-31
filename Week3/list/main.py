import sys
sys.path.append(r'C:\Users\me\Desktop\숭실대\2-1\자료주고\Week3\list\list')
#하.. 드디어 인식 성공했네

from list.linkedBasic import LinkedListBasic
from list.circularLinkedList import CircularLinkedList

if __name__ == "__main__":
    names = ["Amy", "Kevin", "Mary", "David"]
    #name_list = LinkedListBasic()
    name_list = CircularLinkedList()
    for name in names:
        name_list.append(name)
    
    for name in name_list:
        print(name)
    
    name_list.pop(-1)
    name_list.insert(0, "Rose")
    name_list.sort()
    name_list.printList()
        
