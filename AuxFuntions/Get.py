from Structs.Map import Map
from Structs.CircularDoublyLinkedList import CircularDoublyLinkedList
from Structs.CircularDoublyLinkedList import Node
from Structs.HashTableOA import HashTableOA
from Structs.HashTableSC import HashTableSC
from Structs.Comparator import Comparator
from Structs.NumberComparator import NumberComparator
from Structs.StringComparator import StringComparator
from Structs.BinarySearchTree import BinarySearchTree
from Structs.SortedArrayList import SortedArrayList
from Structs.ArraySet import ArraySet
from Structs.DynamicBag import DynamicBag
from Structs.ArrayStack import Stack
from Structs.DoublyLinkedQueue import DoublyLinkedQueue
from Structs.SinglyLinkedList import SinglyLinkedList
from Parser import parser

def super_get(p):
    if isinstance(parser.generatedStructs.get(p[2])[1], Map):
        temp_map = parser.generatedStructs.get(p[2])[1]
        element = map_get(temp_map, p[5])
        print("Got " + str(p[5]) + " from Map " + str(p[2]) + "found: " + str(p[5]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        temp_tree = parser.generatedStructs.get(p[2])[1]
        element = tree_get(temp_tree, p[5])
        print("Got " + str(p[5]) + " from Tree " + str(p[2]) + "found: " + str(p[5]))        
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableOA) or isinstance(parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table = parser.generatedStructs.get(p[2])[1]
        element = hashtable_get(temp_table, p[5])
        print("Got " + str(p[5]) + " from HashTable " + str(p[2]) + "found: " + str(p[5]))
    else:
        print("Structure not valid")


def super_get_index(p):
    try:
        if isinstance(parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
            if isinstance(p[7], int):
                value = linkedlist_get(parser.generatedStructs.get(p[2])[1], p[7])
                print("Got " + str(value) + " from SinglyLinkedList " + str(p[2]))
            else:
                print(str(p[7]) + " is not a valid index")
        elif isinstance(parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
            if isinstance(p[7], int):
                value = cdll_get(parser.generatedStructs.get(p[2])[1], p[7])
                print("Got " + str(value) + " from CDLL " + str(p[2]))
            else:
                print(str(p[7]) + " is not a valid index")
        else:
            print("Structure not valid")
    except Exception:
        print(str(p[7]) + " is not a valid index")



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

