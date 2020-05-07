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


def map_elements(temp_map: Map, values):
    for element in values:
        temp_map = map_no_elements(temp_map, element)
    return temp_map


def map_no_elements(temp_map: Map, element):
    if isinstance(element, tuple):
        temp_map.put(element[0], element[1])
    else:
        temp_map.put(element, None)
    return temp_map


def tree_elements(temp_tree: BinarySearchTree, values):
    for element in values:
        temp_tree = tree_no_elements(temp_tree, element)
    return temp_tree


def tree_no_elements(temp_tree: BinarySearchTree, element):
    if isinstance(element, tuple):
        temp_tree.put(element[0], element[1])
    else:
        temp_tree.put(element, None)
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
        temp_stack = bag_no_elements(temp_stack, element)
    return temp_stack


def stack_no_elements(temp_stack: Stack, element):
    temp_stack.push(element)
    return temp_stack


def queue_elements(temp_queue: DoublyLinkedQueue, values):
    for element in values:
        temp_queue = bag_no_elements(temp_queue, element)
    return temp_queue


def queue_no_elements(temp_queue: DoublyLinkedQueue, element):
    temp_queue.push(element)
    return temp_queue


def hashtable_elements(temp_hashtable, values):
    for element in values:
        temp_hashtable = tree_no_elements(temp_hashtable, element)
    return temp_hashtable


def hashtable_no_elements(temp_hashtable, element):
    if isinstance(element, tuple):
        temp_hashtable.put(element[0], element[1])
    else:
        temp_hashtable.put(element, None)
    return temp_hashtable


