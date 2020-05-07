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


def super_remove(p):
    if isinstance(release_parser.generatedStructs.get(p[2])[1], Map):
        temp_map = map_remove_obj(release_parser.generatedStructs.get(p[2])[1], p[5])
        release_parser.generatedStructs[str(p[2])] = ("Map", temp_map)
        release_parser.messages.append(("Removed " + str(p[5]) + " from Map " + str(p[2])))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        temp_tree = tree_remove_obj(release_parser.generatedStructs.get(p[2])[1], p[5])
        release_parser.generatedStructs[str(p[2])] = ("Tree", temp_tree)
        release_parser.messages.append(("Removed " + str(p[5]) + " from Tree " + str(p[2])))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
        temp_list = cdll_remove_obj(release_parser.generatedStructs.get(p[2])[1], p[5])
        release_parser.generatedStructs[str(p[2])] = ("CircularDoublyLinkedList", temp_list)
        release_parser.messages.append(("Removed " + str(p[5]) + " from CDLL " + str(p[2])))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
        temp_list = sll_remove_obj(release_parser.generatedStructs.get(p[2])[1], p[5])
        release_parser.generatedStructs[str(p[2])] = ("SinglyLinkedList", temp_list)
        release_parser.messages.append(("Removed " + str(p[5]) + " from SLL " + str(p[2])))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], ArraySet):
        temp_set = set_remove_obj(release_parser.generatedStructs.get(p[2])[1], p[5])
        release_parser.generatedStructs[str(p[2])] = ("ArraySet", temp_set)
        release_parser.messages.append(("Removed " + str(p[5]) + " from ArraySet " + str(p[2])))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], DynamicBag):
        temp_bag = bag_remove_obj(release_parser.generatedStructs.get(p[2])[1], p[5])
        release_parser.generatedStructs[str(p[2])] = ("DynamicBag", temp_bag)
        release_parser.messages.append(("Removed " + str(p[5]) + " from DynamicBag " + str(p[2])))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], HashTableOA):
        temp_table = hashtable_remove_obj(release_parser.generatedStructs.get(p[2])[1], p[5])
        release_parser.generatedStructs[str(p[2])] = ("HashTableOA", temp_table)
        release_parser.messages.append(("Removed " + str(p[5]) + " from HashTableOA " + str(p[2])))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table = hashtable_remove_obj(release_parser.generatedStructs.get(p[2])[1], p[5])
        release_parser.generatedStructs[str(p[2])] = ("HashTableSC", temp_table)
        release_parser.messages.append(("Removed " + str(p[5]) + " from HashTableSC " + str(p[2])))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], Stack):
        temp_stack = stack_remove_obj(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("Stack", temp_stack)
        release_parser.messages.append(("Removed " + str(p[5]) + " from Stack " + str(p[2])))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], DoublyLinkedQueue):
        temp_queue = queue_remove_obj(release_parser.generatedStructs.get(p[2])[1])
        release_parser.generatedStructs[str(p[2])] = ("Queue", temp_queue)
        release_parser.messages.append(("Removed " + str(p[5]) + " from Queue " + str(p[2])))

        
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
    