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

def super_contains(p):
    if isinstance(parser.generatedStructs.get(p[2])[1], Map):
        temp_map = parser.generatedStructs.get(p[2])[1]
        contains = map_contains(temp_map, p[5])
        print("Map " + str(p[2] + " contains " + str(p[5]) + "? -> " + str(contains)))
    elif isinstance(parser.generatedStructs.get(p[2])[1], ArraySet):
        temp_set = parser.generatedStructs.get(p[2])[1]
        contains = set_contains(temp_set, p[5])
        print("Set " + str(p[2] + " contains " + str(p[5]) + "? -> " + str(contains)))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DynamicBag):
        temp_bag = parser.generatedStructs.get(p[2])[1]
        contains = bag_contains(temp_bag, p[5])
        print("Set " + str(p[2] + " contains " + str(p[5]) + "? -> " + str(contains)))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableOA) or isinstance(parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table = parser.generatedStructs.get(p[2])[1]
        contains = hashtable_contains(temp_table, p[5])
        print("Hashtable " + str(p[2] + " contains " + str(p[5]) + "? -> " + str(contains)))
    elif isinstance(parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
        temp_list = parser.generatedStructs.get(p[2])[1]
        contains = linkedlist_contains(temp_list, p[5])
        print("LinkedList " + str(p[2] + " contains " + str(p[5]) + "? -> " + str(contains)))
    elif isinstance(parser.generatedStructs.get(p[2])[1], SortedArrayList):
        temp_sortedlist = parser.generatedStructs.get(p[2])[1]
        contains = sortedlist_contains(temp_sortedlist, p[5])
        print("ArrayList " + str(p[2] + " contains " + str(p[5]) + "? -> " + str(contains)))
    elif isinstance(parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
        temp_list = parser.generatedStructs.get(p[2])[1]
        contains = cdll_contains(temp_list, p[5])
        print("CDLList " + str(p[2] + " contains " + str(p[5]) + "? -> " + str(contains)))
    elif isinstance(parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        temp_tree = parser.generatedStructs.get(p[2])[1]
        contains = tree_contains(temp_tree, p[5])
        print("Tree " + str(p[2] + " contains " + str(p[5]) + "? -> " + str(contains)))

def map_contains(temp_map: Map, key):
    if isinstance(key, tuple):
        return temp_map.containsKey(key[0])
    else:
        return temp_map.containsKey(key)
    

def set_contains(temp_set: ArraySet, element):
    return temp_set.isMember(element)

def bag_contains(temp_bag: DynamicBag, element):
    return temp_bag.isMember(element)

def sortedlist_contains(temp_sortedlist: SortedArrayList, element):
    return temp_sortedlist.isMember(element)

def cdll_contains(temp_cdll: CircularDoublyLinkedList, element):
    return False

def hashtable_contains(temp_table, element):
    if isinstance(temp_table, HashTableOA) or isinstance(temp_table, HashTableSC):
        if isinstance(element, tuple):
            return temp_table.containsKey(element[0])
        else:
            return temp_table.containsKey(element)


def linkedlist_contains(temp_list: SinglyLinkedList, element):
    return temp_list.contains(element)

def tree_contains(temp_tree:BinarySearchTree, key):
    if isinstance(key, tuple):
        return temp_tree.containsKey(key[0])
    else:
        return temp_tree.containsKey(key)