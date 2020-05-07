from Structs import ArrayStack
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

def super_removeAll(p):
    if isinstance(parser.generatedStructs.get(p[2])[1], Map):
        temp_map = map_remove_all(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("Map", temp_map)
        print("Removed all instances of " + str(p[5]) + " from Map " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        print("Can't instances of "  + str(p[5]) + " from Tree " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
        temp_list = cdll_remove_all(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("CircularDoublyLinkedList", temp_list)
        print("Removed all instances of "  + str(p[5]) + " from CDLL " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
        temp_list = sll_remove_all(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("SinglyLinkedList", temp_list)
        print("Removed all instances of "  + str(p[5]) + " from SLL " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], ArraySet):
        print("Can't remove instances of "  + str(p[5]) + " from ArraySet " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DynamicBag):
        temp_bag = bag_remove_all(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("DynamicBag", temp_bag)
        print("Removed all instances of "  + str(p[5]) + " from DynamicBag " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableOA):
        temp_table = htoa_remove_all(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("HashTableOA", temp_table)
        print("Removed all instances of "  + str(p[5]) + " from HashTableOA " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table = htsc_remove_all(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("HashTableSC", temp_table)
        print("Removed all instances of "  + str(p[5]) + " from HashTableSC " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], Stack):
        print("Can't remove instances of "  + str(p[5]) + " from Stack " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DoublyLinkedQueue):
        print("Can't remove instances of "  + str(p[5]) + " from Queue " + str(p[2]))

def bag_remove_all(temp_bag: DynamicBag, element):
    temp_bag.removeAll(element)
    return temp_bag

def cdll_remove_all(temp_cdll: CircularDoublyLinkedList, element):
    temp_cdll.remove
    return temp_cdll

def sll_remove_all(temp_sll: SinglyLinkedList, element):
    while temp_sll.contains(element):
        temp_sll.remove(element)
    return temp_sll

# def tree_remove_all(temp_tree: BinarySearchTree, element):
#     temp_tree.makeEmpty()
#     return temp_tree

def map_remove_all(temp_map: Map, element):
    if isinstance(element, tuple):
        while temp_map.get(element[0]):
            temp_map.remove(element[0])
    else:
        while temp_map.get(element):
            temp_map.remove(element)
    return temp_map

def htoa_remove_all(temp_htoa: HashTableOA, element):
    if isinstance(element, tuple):
        while temp_htoa.get(element[0]):
            temp_htoa.remove(element[0])
    else:
        while temp_htoa.get(element):
            temp_htoa.remove(element)
    return temp_htoa

def htsc_remove_all(temp_htsc: HashTableSC, element):
    if isinstance(element, tuple):
        while temp_htsc.get(element[0]):
            temp_htsc.remove(element[0])
    else:
        while temp_htsc.get(element):
            temp_htsc.remove(element)
    return temp_htsc