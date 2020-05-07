from Structs.Map import Map
from Structs.CircularDoublyLinkedList import CircularDoublyLinkedList
from Structs.CircularDoublyLinkedList import Node
from Structs.HashTableOA import HashTableOA
from Structs.HashTableSC import HashTableSC
from Structs.BinarySearchTree import BinarySearchTree
from Structs.SortedArrayList import SortedArrayList
from Structs.ArraySet import ArraySet
from Structs.DynamicBag import DynamicBag
from Structs.ArrayStack import Stack
from Structs.DoublyLinkedQueue import DoublyLinkedQueue
from Structs.SinglyLinkedList import SinglyLinkedList
from Parser import parser


def super_add(p):
    if isinstance(parser.generatedStructs.get(p[2])[1], Map):
        temp_map = map_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("Map", temp_map)
        print("Added " + str(p[5]) + " to Map " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        temp_tree = tree_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("Tree", temp_tree)
        print("Added " + str(p[5]) + " to Tree " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
        temp_cdll = cdll_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("CDLL", temp_cdll)
        print("Added " + str(p[5]) + " to CDLL " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], ArraySet):
        temp_set = set_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("Set", temp_set)
        print("Added " + str(p[5]) + " to ArraySet " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DynamicBag):
        temp_bag = bag_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("Bag", temp_bag)
        print("Added " + str(p[5]) + " to Bag " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
        temp_list = linkedlist_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("SinglyLinkedList", temp_list)
        print("Added " + str(p[5]) + " to SLL " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableOA):
        temp_table = hashtable_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("HSOA", temp_table)
        print("Added " + str(p[5]) + " to HSOA " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table = hashtable_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("HSSC", temp_table)
        print("Added " + str(p[5]) + " to HSSC " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], SortedArrayList):
        temp_sl = sortedarraylist_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("SortedList", temp_sl)
        print("Added " + str(p[5]) + " to SortedList " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], Stack):
        temp_stack = stack_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("Stack", temp_stack)
        print("Added " + str(p[5]) + " to Stack " + str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DoublyLinkedQueue):
        temp_queue = queue_no_elements(parser.generatedStructs.get(p[2])[1], p[5])
        parser.generatedStructs[str(p[2])] = ("Queue", temp_queue)
        print("Added " + str(p[5]) + " to Queue " + str(p[2]))


def map_elements(temp_map: Map, values):
    for element in values:
        temp_map = map_no_elements(temp_map, element)
    return temp_map


def map_no_elements(temp_map: Map, element):
    if isinstance(element, tuple):
        temp_map.put(element[0], element[1])
    else:
        temp_map.put(element, element)
    return temp_map


def tree_elements(temp_tree: BinarySearchTree, values):
    for element in values:
        temp_tree = tree_no_elements(temp_tree, element)
    return temp_tree


def tree_no_elements(temp_tree: BinarySearchTree, element):
    if isinstance(element, tuple):
        temp_tree.put(element[0], element[1])
    else:
        temp_tree.put(element, element)
    return temp_tree


def cdll_elements(temp_cdll: CircularDoublyLinkedList, values):
    for element in values:
        temp_cdll = cdll_no_elements(temp_cdll, element)
    return temp_cdll


def cdll_no_elements(temp_cdll: CircularDoublyLinkedList, element):
    tempVal = Node(element)
    temp_cdll.insert_at_end(tempVal)
    return temp_cdll


def set_elements(temp_set: ArraySet, values):
    for element in values:
        temp_set = set_no_elements(temp_set, element)
    return temp_set


def set_no_elements(temp_set: ArraySet, element):
    temp_set.add(element)
    return temp_set


def bag_elements(temp_bag: DynamicBag, values):
    for element in values:
        temp_bag = bag_no_elements(temp_bag, element)
    return temp_bag


def bag_no_elements(temp_bag: DynamicBag, element):
    temp_bag.add(element)
    return temp_bag


def stack_elements(temp_stack: Stack, values):
    for element in values:
        temp_stack = stack_no_elements(temp_stack, element)
    return temp_stack


def stack_no_elements(temp_stack: Stack, element):
    temp_stack.push(element)
    return temp_stack


def queue_elements(temp_queue: DoublyLinkedQueue, values):
    for element in values:
        temp_queue = queue_no_elements(temp_queue, element)
    return temp_queue


def queue_no_elements(temp_queue: DoublyLinkedQueue, element):
    temp_queue.enqueue(element)
    return temp_queue


def hashtable_elements(temp_hashtable, values):
    for element in values:
        temp_hashtable = tree_no_elements(temp_hashtable, element)
    return temp_hashtable


def hashtable_no_elements(temp_hashtable, element):
    if isinstance(element, tuple):
        temp_hashtable.put(element[0], element[1])
    else:
        temp_hashtable.put(element, element)
    return temp_hashtable

def linkedlist_elements(temp_linkedlist, values):
    for element in values:
        temp_linkedlist = linkedlist_no_elements(temp_linkedlist,element)
    return temp_linkedlist

def linkedlist_no_elements(temp_linkedlist, element):
    temp_linkedlist.add(element)
    return temp_linkedlist

def sortedarraylist_elements(temp_sortedarraylist,values):
    for element in values:
        temp_sortedarraylist = sortedarraylist_no_elements(temp_sortedarraylist,element)
    return temp_sortedarraylist

def sortedarraylist_no_elements(temp_sortedarraylist, element):
    temp_sortedarraylist.add(element)
    return temp_sortedarraylist