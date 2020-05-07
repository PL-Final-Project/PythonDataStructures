import ArrayStack
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


def super_clear(p):
    if isinstance(release_parser.generatedStructs.get(p[2])[1], Map):
        temp_map = map_clear(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("Map", temp_map)
        print("Removed all elements from Map " + str(p[2]))
        release_parser.messages.append("Removed all elements from Map " + str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        temp_tree = tree_clear(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("Tree", temp_tree)
        print("Removed all elements from Tree " + str(p[2]))
        release_parser.messages.append("Removed all elements from Tree " + str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
        temp_list = cdll_clear(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("CircularDoublyLinkedList", temp_list)
        print("Removed all elements from CircularDoublyLinkedList " + str(p[2]))
        release_parser.messages.append("Removed all elements from CircularDoublyLinkedList " + str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
        temp_list = sll_clear(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("SinglyLinkedList", temp_list)
        print("Removed all elements from SinglyLinkedList " + str(p[2]))
        release_parser.messages.append("Removed all elements from SinglyLinkedList " + str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], ArraySet):
        temp_set = set_clear(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("ArraySet", temp_set)
        print("Removed all elements from ArraySet " + str(p[2]))
        release_parser.messages.append("Removed all elements from ArraySet " + str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], DynamicBag):
        temp_bag = bag_clear(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("DynamicBag", temp_bag)
        print("Removed all elements from DynamicBag " + str(p[2]))
        release_parser.messages.append("Removed all elements from DynamicBag " + str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], HashTableOA):
        temp_table = htoa_clear(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("HashTableOA", temp_table)
        print("Removed all elements from HashTableOA " + str(p[2]))
        release_parser.messages.append("Removed all elements from HashTableOA " + str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table = htsc_clear(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("HashTableSC", temp_table)
        print("Removed all elements from HashTableSC " + str(p[2]))
        release_parser.messages.append("Removed all elements from HashTableSC " + str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], Stack):
        temp_stack = stack_clear(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("Stack", temp_stack)
        print("Removed all elements from Stack " + str(p[2]))
        release_parser.messages.append("Removed all elements from Stack " + str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], DoublyLinkedQueue):
        temp_queue = queue_clear(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("Queue", temp_queue)
        print("Removed all elements from Queue " + str(p[2]))
        release_parser.messages.append("Removed all elements from Queue " + str(p[2]))
    


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