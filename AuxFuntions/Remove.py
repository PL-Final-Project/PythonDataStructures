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


def super_remove(p):
    if isinstance(parser.generatedStructs.get(p[2])[1], Map):
        temp_map = map_remove_obj(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("Map", temp_map)
        print("Removed " + str(p[5]) + " from Map " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        temp_tree = tree_remove_obj(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("Tree", temp_tree)
        print("Removed " + str(p[5]) + " from Tree " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
        temp_list = cdll_remove_obj(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("CircularDoublyLinkedList", temp_list)
        print("Removed " + str(p[5]) + " from CDLL " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
        temp_list = sll_remove_obj(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("SinglyLinkedList", temp_list)
        print("Removed " + str(p[5]) + " from SLL " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], ArraySet):
        temp_set = set_remove_obj(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("ArraySet", temp_set)
        print("Removed " + str(p[5]) + " from ArraySet " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DynamicBag):
        temp_bag = bag_remove_obj(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("DynamicBag", temp_bag)
        print("Removed " + str(p[5]) + " from DynamicBag " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableOA):
        temp_table = hashtable_remove_obj(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("HashTableOA", temp_table)
        print("Removed " + str(p[5]) + " from HashTableOA " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table = hashtable_remove_obj(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("HashTableSC", temp_table)
        print("Removed " + str(p[5]) + " from HashTableSC " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], Stack):
        temp_stack = stack_remove_obj(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("Stack", temp_stack)
        print("Removed " + str(p[5]) + " from Stack " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DoublyLinkedQueue):
        temp_queue = queue_remove_obj(parser.generatedStructs.get(p[2])[1])
        parser.generatedStructs[str(p[2])] = ("Queue", temp_queue)
        print("Removed " + str(p[5]) + " from Queue " + str(p[2]))

        
def map_remove_obj(temp_map: Map, element):
    temp_map.remove(element)
    return temp_map


def hashtable_remove_obj(temp_table , element):
    if isinstance(element, tuple):
        temp_table.remove(element[0])
    else:
        temp_table.remove(element)
    return temp_table


def cdll_remove_obj(temp_list: CircularDoublyLinkedList, element):
    temp_list.remove(element)
    return temp_list

def stack_remove_obj(temp_stack: Stack):
    temp_stack.pop()
    return temp_stack

def queue_remove_obj(temp_queue: DoublyLinkedQueue):
    temp_queue.dequeue()
    return temp_queue


def set_remove_obj(temp_set, element):
    if temp_set.isMember(element):
        temp_set.remove(element)
    return temp_set
   

def bag_remove_obj(temp_bag: DynamicBag, element):
    if temp_bag.isMember(element):
        temp_bag.remove(element)
    return temp_bag


def sll_remove_obj(temp_list: SinglyLinkedList, element):
    if temp_list.contains(element):
        temp_list.remove(element)
    return temp_list
    

def tree_remove_obj(temp_tree:BinarySearchTree, element):
    if isinstance(element, tuple):
        temp_tree.remove(element[0])
    else:
        temp_tree.remove(element)
    return temp_tree
    