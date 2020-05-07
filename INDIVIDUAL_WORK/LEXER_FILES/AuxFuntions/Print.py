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

COUNT = [10]


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
