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

def super_clear(p):
    if isinstance(parser.generatedStructs.get(p[2])[1], Map):
        temp_map = map_clear(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("Map", temp_map)
        print("Removed all elements from Map " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        temp_tree = tree_clear(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("Tree", temp_tree)
        print("Removed all elements from Tree " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
        temp_list = cdll_clear(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("CircularDoublyLinkedList", temp_list)
        print("Removed all elements from CircularDoublyLinkedList " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
        temp_list = sll_clear(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("SinglyLinkedList", temp_list)
        print("Removed all elements from SinglyLinkedList " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], ArraySet):
        temp_set = set_clear(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("ArraySet", temp_set)
        print("Removed all elements from ArraySet " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DynamicBag):
        temp_bag = bag_clear(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("DynamicBag", temp_bag)
        print("Removed all elements from DynamicBag " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableOA):
        temp_table = htoa_clear(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("HashTableOA", temp_table)
        print("Removed all elements from HashTableOA " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table = htsc_clear(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("HashTableSC", temp_table)
        print("Removed all elements from HashTableSC " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], Stack):
        temp_stack = stack_clear(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("Stack", temp_stack)
        print("Removed all elements from Stack " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DoublyLinkedQueue):
        temp_queue = queue_clear(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("Queue", temp_queue)
        print("Removed all elements from Queue " + str(p[2]))
    


def set_clear(temp_set: ArraySet):
    temp_set.clear()
    return temp_set

def bag_clear(temp_bag: DynamicBag):
    temp_bag.clear()
    return temp_bag

def stack_clear(temp_stack: Stack):
    while not temp_stack.isEmpty():
        temp_stack.pop()
    return temp_stack

def cdll_clear(temp_cdll: CircularDoublyLinkedList):
    temp_cdll.clear()
    return temp_cdll

def sll_clear(temp_sll: SinglyLinkedList):
    temp_sll.clear()
    return temp_sll

def tree_clear(temp_tree: BinarySearchTree):
    temp_tree.makeEmpty()
    return temp_tree

def queue_clear(temp_queue: DoublyLinkedQueue):
    temp_queue.makeEmpty()
    return temp_queue

def map_clear(temp_map: Map):
    temp_map.makeEmpty()
    return temp_map

def htoa_clear(temp_htoa: HashTableOA):
    temp_htoa.makeEmpty()
    return temp_htoa

def htsc_clear(temp_htsc: HashTableSC):
    temp_htsc.makeEmpty()
    return temp_htsc