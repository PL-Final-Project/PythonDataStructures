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
from Structs.BinaryTreeNode import BinaryTreeNode
from Parser import parser


COUNT = [10]


def super_print(p):
    if isinstance(parser.generatedStructs.get(p[2])[1], BinarySearchTree):
        temp_tree: BinarySearchTree = parser.generatedStructs.get(p[2])[1]
        tree_print(temp_tree, str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], Map):
        temp_map: Map = parser.generatedStructs.get(p[2])[1]
        map_print(temp_map, str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DynamicBag):
        temp_bag: DynamicBag = parser.generatedStructs.get(p[2])[1]
        bag_print(temp_bag, str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], Stack):
        temp_stack: Stack = parser.generatedStructs.get(p[2])[1]
        stack_print(temp_stack, str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], DoublyLinkedQueue):
        temp_queue: DoublyLinkedQueue = parser.generatedStructs.get(p[2])[1]
        queue_print(temp_queue, str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], SinglyLinkedList):
        temp_list: SinglyLinkedList = parser.generatedStructs.get(p[2])[1]
        linkedlist_print(temp_list, str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], CircularDoublyLinkedList):
        temp_cdll: CircularDoublyLinkedList = parser.generatedStructs.get(p[2])[1]
        cdll_print(temp_cdll, str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], ArraySet):
        temp_set: ArraySet = parser.generatedStructs.get(p[2])[1]
        set_print(temp_set, str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableOA):
        temp_table: HashTableOA = parser.generatedStructs.get(p[2])[1]
        hashtable_print(temp_table, str(p[2]))
    elif isinstance(parser.generatedStructs.get(p[2])[1], HashTableSC):
        temp_table: HashTableSC = parser.generatedStructs.get(p[2])[1]
        hashtable_print(temp_table, str(p[2]))


def tree_print(temp_tree: BinarySearchTree, id):
    # final_display = []
    # temp_values: SinglyLinkedList = temp_tree.getKeys()
    # temp_values_2: SinglyLinkedList = temp_tree.getValues()
    # for index in range(0, temp_values.size()):
    #     element = temp_values.get(index)
    #     element_2 = temp_values_2.get(index)
    #     final_display.append((element, element_2))
    print("Displaying BST " + str(id))
    print2D(temp_tree.root)
    # print(final_display)


def tree_print_aux(n: BinaryTreeNode):
    if n is None:
        return
    else:
        tree_print_aux(n.getLeftChild())
        print((n.value.getKey(),n.value.getValue()))
        tree_print_aux(n.getRightChild())


# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root:BinaryTreeNode, space):
    # Base case
    if root is None:
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.getRightChild(), space)

    # Print current node after space
    # count
    # print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print((root.value.getKey(),root.value.getValue()))

    # Process left child
    print2DUtil(root.getLeftChild(), space)


# Wrapper over print2DUtil()
def print2D(root: BinaryTreeNode):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


def sortedarraylist_print(temp_arraylist: SortedArrayList, id):
    print("Displaying SortedList " + str(id))
    temp_arraylist.printValues()
    return

def map_print(temp_map:Map, id):
    keys = temp_map.getKeys()
    values = temp_map.getValues()
    print("Displaying Map " + str(id))
    for i in range(0, keys.size()):
        key = keys.get(i)
        value = values.get(i)
        print(str(key) + ', '+ str(value))
    return

def cdll_print(temp_cdll:CircularDoublyLinkedList, id):
    print("Displaying CDLL " + str(id))
    temp_cdll.display()
    return

def stack_print(temp_stack: Stack, id):
    print("Displaying Stack " + str(id))
    temp_stack.printStack()
    return

def queue_print(temp_queue: DoublyLinkedQueue, id):
    print("Displaying Queue " + str(id))
    temp_queue.printQueue()
    return

def set_print(temp_set:ArraySet, id):
    temp = temp_set.toArray()
    print("Displaying ArraySet " + str(id))
    for i in range(0, temp.length()):
        print(temp[i])
    return

def bag_print(temp_bag: DynamicBag, id):
    print("Displaying Bag " + str(id))
    for i in range(0, temp_bag.size()):
        print(temp_bag.elements[i])
    return

def hashtable_print(temp_hashtable, id):
    print("Displaying HashTable " + str(id))
    keys = temp_hashtable.getKeys()
    values = temp_hashtable.getValues()
    for i in range(0, keys.size()):
        key = keys.get(i)
        value = values.get(i)
        print(str(key) + ', '+ str(value))
    return

def linkedlist_print(temp_linkedlist:SinglyLinkedList, id):
    print("Displaying SinglyLinkedList " + str(id))
    temp_linkedlist.display()
    return