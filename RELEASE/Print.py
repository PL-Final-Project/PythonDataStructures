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
from BinaryTreeNode import BinaryTreeNode
import release_parser


COUNT = [10]


def super_print(p):
    if isinstance(release_parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        temp_tree: BinarySearchTree = release_parser.generatedStructs.get(p[2])[1]
        tree_print(temp_tree, str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], Map):
        temp_map: Map = release_parser.generatedStructs.get(p[2])[1]
        map_print(temp_map, str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], DynamicBag):
        temp_bag: DynamicBag = release_parser.generatedStructs.get(p[2])[1]
        bag_print(temp_bag, str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], Stack):
        temp_stack: Stack = release_parser.generatedStructs.get(p[2])[1]
        stack_print(temp_stack, str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], DoublyLinkedQueue):
        temp_queue: DoublyLinkedQueue = release_parser.generatedStructs.get(p[2])[1]
        queue_print(temp_queue, str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
        temp_list: SinglyLinkedList = release_parser.generatedStructs.get(p[2])[1]
        linkedlist_print(temp_list, str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
        temp_cdll: CircularDoublyLinkedList = release_parser.generatedStructs.get(p[2])[1]
        cdll_print(temp_cdll, str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], ArraySet):
        temp_set: ArraySet = release_parser.generatedStructs.get(p[2])[1]
        set_print(temp_set, str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], HashTableOA):
        temp_table: HashTableOA = release_parser.generatedStructs.get(p[2])[1]
        hashtable_print(temp_table, str(p[2]))
    elif isinstance(release_parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table: HashTableSC = release_parser.generatedStructs.get(p[2])[1]
        hashtable_print(temp_table, str(p[2]))


def tree_print(temp_tree: BinarySearchTree, id):
    # final_display = []
    # temp_values: SinglyLinkedList = temp_tree.getKeys()
    # temp_values_2: SinglyLinkedList = temp_tree.getValues()
    # for index in range(0, temp_values.size()):
    #     element = temp_values.get(index)
    #     element_2 = temp_values_2.get(index)
    #     final_display.append((element, element_2))
    release_parser.messages.append(("Displaying BST " + str(id)))
    release_parser.messages.append("Displaying BST " + str(id))
    print2D(temp_tree.root)
    # release_parser.messages.append((final_display)


def tree_print_aux(n: BinaryTreeNode):
    if n is None:
        return
    else:
        tree_print_aux(n.getLeftChild())
        release_parser.messages.append((n.value.getKey(), n.value.getValue()))
        tree_print_aux(n.getRightChild())


# Function to release_parser.messages.append( binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root:BinaryTreeNode, space):
    # Base case
    if root is None:
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.getRightChild(), space)

    # release_parser.messages.append( current node after space
    # count
    # release_parser.messages.append(()
    for i in range(COUNT[0], space):
        print(end=" ")
        release_parser.messages.append(" ")
        
    release_parser.messages.append((root.value.getKey(), root.value.getValue()))
    

    # Process left child
    print2DUtil(root.getLeftChild(), space)


# Wrapper over print2DUtil()
def print2D(root: BinaryTreeNode):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


def sortedarraylist_print(temp_arraylist: SortedArrayList, id):
    release_parser.messages.append(("Displaying SortedList " + str(id)))
    
    temp_arraylist.printValues()
    return

def map_print(temp_map:Map, id):
    keys = temp_map.getKeys()
    values = temp_map.getValues()
    release_parser.messages.append(("Displaying Map " + str(id)))
    
    for i in range(0, keys.size()):
        key = keys.get(i)
        value = values.get(i)
        release_parser.messages.append((str(key) + ', '+ str(value)))
        
    return

def cdll_print(temp_cdll:CircularDoublyLinkedList, id):
    release_parser.messages.append(("Displaying CDLL " + str(id)))
    
    temp_cdll.display()
    return

def stack_print(temp_stack: Stack, id):
    release_parser.messages.append(("Displaying Stack " + str(id)))
    
    temp_stack.printStack()
    return

def queue_print(temp_queue: DoublyLinkedQueue, id):
    release_parser.messages.append(("Displaying Queue " + str(id)))
    
    temp_queue.printQueue()
    return

def set_print(temp_set:ArraySet, id):
    temp = temp_set.toArray()
    release_parser.messages.append(("Displaying ArraySet " + str(id)))
    
    for i in range(0, temp.length()):
        release_parser.messages.append((temp[i]))
        
    return

def bag_print(temp_bag: DynamicBag, id):
    release_parser.messages.append(("Displaying Bag " + str(id)))
    for i in range(0, temp_bag.size()):
        release_parser.messages.append((temp_bag.elements[i]))
        
    return

def hashtable_print(temp_hashtable, id):
    release_parser.messages.append(("Displaying HashTable " + str(id)))
    keys = temp_hashtable.getKeys()
    values = temp_hashtable.getValues()
    for i in range(0, keys.size()):
        key = keys.get(i)
        value = values.get(i)
        release_parser.messages.append((str(key) + ', '+ str(value)))
    return

def linkedlist_print(temp_linkedlist:SinglyLinkedList, id):
    release_parser.messages.append(("Displaying SinglyLinkedList " + str(id)))
    temp_linkedlist.display()
    return