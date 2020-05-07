from Map import Map
from CircularDoublyLinkedList import CircularDoublyLinkedList
from CircularDoublyLinkedList import Node
from HashTableOA import HashTableOA
from HashTableSC import HashTableSC
from Comparator import Comparator
from NumberComparator import NumberComparator
from StringComparator import StringComparator
from BinarySearchTree import BinarySearchTree
from SortedArrayList import SortedArrayList
from ArraySet import ArraySet
from DynamicBag import DynamicBag
from ArrayStack import Stack
from DoublyLinkedQueue import DoublyLinkedQueue
from SinglyLinkedList import SinglyLinkedList
import release_parser

def super_get(p):
    if isinstance(release_parser.generatedStructs.get(p[2])[1], Map):
        temp_map = release_parser.generatedStructs.get(p[2])[1]
        element = map_get(temp_map, p[5])
        print("Got " + str(p[5]) + " from Map " + str(p[2]) + "found: " + str(p[5]))
        release_parser.messages.append("Got " + str(p[5]) + " from Map " + str(p[2]) + "found: " + str(p[5]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        temp_tree = release_parser.generatedStructs.get(p[2])[1]
        element = tree_get(temp_tree, p[5])
        print("Got " + str(p[5]) + " from Tree " + str(p[2]) + "found: " + str(p[5]))
        release_parser.messages.append("Got " + str(p[5]) + " from Tree " + str(p[2]) + "found: " + str(p[5]))

    elif isinstance(release_parser.generatedStructs.get(p[2])[1], HashTableOA) or isinstance(release_parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table = release_parser.generatedStructs.get(p[2])[1]
        element = hashtable_get(temp_table, p[5])
        print("Got " + str(p[5]) + " from HashTable " + str(p[2]) + "found: " + str(p[5]))
        release_parser.messages.append("Got " + str(p[5]) + " from HashTable " + str(p[2]) + "found: " + str(p[5]))

    else:
        print("Structure not valid")
        release_parser.messages.append("Structure not valid")



def super_get_index(p):
    try:
        if isinstance(release_parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
            if isinstance(p[7], int):
                value = linkedlist_get(release_parser.generatedStructs.get(p[2])[1], p[7])
                print("Got " + str(value) + " from SinglyLinkedList " + str(p[2]))
                release_parser.messages.append("Got " + str(value) + " from SinglyLinkedList " + str(p[2]))

            else:
                print(str(p[7]) + " is not a valid index")
                release_parser.messages.append(str(p[7]) + " is not a valid index")

        elif isinstance(release_parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
            if isinstance(p[7], int):
                value = cdll_get(release_parser.generatedStructs.get(p[2])[1], p[7])
                print("Got " + str(value) + " from CDLL " + str(p[2]))
                release_parser.messages.append("Got " + str(value) + " from CDLL " + str(p[2]))

            else:
                print(str(p[7]) + " is not a valid index")
                release_parser.messages.append()

        else:
            print("Structure not valid")
            release_parser.messages.append("Structure not valid")

    except Exception:
        print(str(p[7]) + " is not a valid index")
        release_parser.messages.append(str(p[7]) + " is not a valid index")




def tree_get(temp_tree: BinarySearchTree, key):
    if isinstance(key, tuple):
        return temp_tree.containsKey(key[0])
    else:
        return temp_tree.containsKey(key)

def hashtable_get(temp_table, key):
    if isinstance(temp_table, HashTableOA) or isinstance(temp_table, HashTableSC):
        if isinstance(key, tuple):
            return temp_table.get(key[0])
        else:
            return temp_table.get(key)

def map_get(temp_map: Map,key):
    if isinstance(key, tuple):
        return temp_map.containsKey(key[0])
    else:
        return temp_map.containsKey(key)

def linkedlist_get(temp_list: SinglyLinkedList, index):
	return temp_list.get(index)

def cdll_get(temp_list: CircularDoublyLinkedList, index):
    return temp_list.get(index)

