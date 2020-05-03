from ply import yacc
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
from AuxFuntions.Add import *
from AuxFuntions.Print import *
from Lexer.lexer import tokens
import ply.yacc as yacc

# from Structs import (ArraySet, ArrayStack, HashTableOA,
# HashTableSC, CircularDoublyLinkedList, DynamicBag, BinarySearchTree, SortedArrayList, DoublyLinkedQueue)
'''
Declare:
    <InputRequiredStruct> <ID> <Assign> \< (<Whitspace>*<Comparators>+<Whitspace>*)+ \>
    <InputOptionalStruct> <ID> <Assign> \< (<Whitspace>*<Comparators>+<Whitspace>*)+ \>
    <Structures> <ID> <Assign> \< <Whitspace>* \>

    Add Methods:
    Use <Structures> <
        <ID> :
        ([A-Za-z]+,?)*

     >


HashTableOA Names => (Comp) <
"Francisco, 1"
"Jorge, 2"
"Alberto, 3"
"Andrew, 4"
>

Structures:
   Stack, Queue, Map, ArrayList, CDLinkedList,Stack, Set, Bag,

InputRequiredStruct:
    Tree, SArrayList

InputOptionalStruct:
    HashTableOA HashTableSC 



'''
elements = []
generatedStructs = {}


def p_Program(p):
    ''' Program : Declaration
                | Program Separator Declaration
                | Program Separator Action

    '''
    # if len(p) == 3:
    #     p[0] = p[1] + p[2]
    # elif len(p) == 2:
    #     p[0] = p[1]


def p_Action(p):
    ''' Action : use Id add Prim
                | use Id add Tuples
                | print Id
    '''
    if generatedStructs.get(p[2]) is not None and len(p) == 5:
        if isinstance(generatedStructs.get(p[2])[1], Map):
            temp_map = map_no_elements(generatedStructs.get(p[2])[1], p[4])
            generatedStructs[str(p[2])] = ("Map", temp_map)
            print("Added " + str(p[4]) + " to Map " + str(p[2]))
        elif isinstance(generatedStructs.get(p[2])[1], BinarySearchTree):
            temp_tree = tree_no_elements(generatedStructs.get(p[2])[1], p[4])
            generatedStructs[str(p[2])] = ("Tree", temp_tree)
            print("Added " + str(p[4]) + " to Tree " + str(p[2]))
    elif len(p) == 3:
        if isinstance(generatedStructs.get(p[2])[1], BinarySearchTree):
            temp_tree: BinarySearchTree = generatedStructs.get(p[2])[1]
            tree_print(temp_tree, str(p[2]))


def p_Declaration(p):
    ''' Declaration : InputOptionalStruct LT Elements GT
                    | InputRequiredStruct LT Elements GT
                    | Structures Id Assign LT Elements GT
                    | InputOptionalStruct LT  GT
                    | InputRequiredStruct LT  GT
                    | Structures Id Assign LT  GT
    '''
    if len(p) == 7:
        temp_elements = p[5]
        print(temp_elements)
        if isinstance(p[1], Map):
            p[1] = map_elements(p[1], temp_elements)
            generatedStructs[str(p[2])] = ("Map", p[1])
        elif isinstance(p[1], CircularDoublyLinkedList):
            p[1] = cdll_elements(p[1], elements)
            generatedStructs[str(p[2])] = ("CDLL", p[1])
        elif isinstance(p[1], DynamicBag):
            p[1] = bag_elements(p[1], elements)
            generatedStructs[str(p[2])] = ("Bag", p[1])
        elif isinstance(p[1], ArraySet):
            p[1] = set_elements(p[1], elements)
            generatedStructs[str(p[2])] = ("Set", p[1])
        elif isinstance(p[1], Stack):
            p[1] = stack_elements(p[1], elements)
            generatedStructs[str(p[2])] = ("Stack", p[1])
        elif isinstance(p[1], DoublyLinkedQueue):
            p[1] = queue_elements(p[1], elements)
            generatedStructs[str(p[2])] = ("Queue", p[1])
    elif len(p) == 5:
        # p[3] are elements
        temp_elements = p[3]
        print(temp_elements)
        # HashTables
        if isinstance(p[1], HashTableOA) or isinstance(p[1], HashTableSC):
            hashtable_elements(p[1], temp_elements)
        if isinstance(p[1], BinarySearchTree):
            tree_elements(p[1], temp_elements)
    elif len(p) == 6:
        if isinstance(p[1], Map):
            generatedStructs[str(p[2])] = ("Map", p[1])
    elements.clear()
    print(generatedStructs)


def p_Tuples(p):
    ''' Tuples : LP Prim Separator Prim RP

    '''
    p[0] = (p[2], p[4])


def p_Elements(p):
    ''' Elements : Prim
                  | Elements Separator Elements
                  | Tuples
    '''
    if len(p) == 2:
        elements.append(p[1])
        p[0] = elements
    elif len(p) == 4:
        if len(p[1]) == 1:
            elements.append(p[1])
        if len(p[3]) == 1:
            elements.append(p[3])
        p[0] = elements
    elif len(p) == 1:
        p[0] = elements


def p_Prim(p):
    ''' Prim : Bool
                | Int
                | Id
                | String
    '''
    p[0] = p[1]


def p_Structures(p):
    ''' Structures : DLQ
                    | Map
                    | AL
                    | CDLL
                    | AS
                    | Set
                    | Bag
    '''
    if p[1] == 'Map':  # El value del Token
        p[0] = Map()
    elif p[1] == 'CircularDoublyLinkedList':
        p[0] = CircularDoublyLinkedList()
    elif p[1] == 'Set':
        p[0] = ArraySet()
    elif p[1] == 'Bag':
        p[0] = DynamicBag()
    elif p[1] == 'ArrayStack':
        p[0] = Stack()
    elif p[1] == 'DoublyLinkedQueue':
        p[0] = DoublyLinkedQueue()


def p_InputRequiredStruct(p):
    ''' InputRequiredStruct :  Tree Id Assign LP Comparator RP
                            |  SArrayList Id Assign LP Comparator Separator Comparator RP
    '''
    if p[1] == 'BinarySearchTree':
        p[0] = BinarySearchTree(p[5])
        generatedStructs[str(p[2])] = ('Tree', p[0])
    elif p[1] == 'SortedArrayList':
        p[0] = SortedArrayList(p[5])
        generatedStructs[str(p[2])] = ('SArrayList', p[0])


def p_InputOptionalStruct(p):
    ''' InputOptionalStruct : HSOA Id Assign LP Comparator Separator Comparator RP
                            | HSSC Id Assign LP Comparator Separator Comparator RP
                            | HSSC Id Assign LP RP
                            | HSOA Id Assign LP RP
    '''
    if p[1] == 'HashTableOA':
        if len(p) == 6:
            p[0] = HashTableOA()
            generatedStructs[str(p[2])] = ('HSOA', p[0])
        else:
            p[0] = HashTableOA(p[5], p[6])
            generatedStructs[str(p[2])] = ('HSOA', p[0])
    if p[1] == 'HashTableSC':
        if len(p) == 6:
            p[0] = HashTableSC()
            generatedStructs[str(p[2])] = ('HSSC', p[0])
        else:
            p[0] = HashTableSC(p[5], p[6])
            generatedStructs[str(p[2])] = ('HSSC', p[0])


def p_Comparator(p):
    ''' Comparator : NumberComp
                    | StringComp
    '''
    if p[1] == 'NumberComp':
        p[0]: Comparator = NumberComparator()
    else:
        p[0]: Comparator = StringComparator()


def p_Id(p):
    '''
    Id : character
        | Id digit
        | Id character
    '''
    if len(p) == 2:
        p[0] = str(p[1])
    else:
        word = str(p[1]) + str(p[2])
        p[0] = word


def p_Bool(p):
    '''
    Bool : True
        | False
    '''
    if p[1] == 'True':
        p[0] = True
    else:
        p[0] = False


def p_Int(p):
    '''
    Int : digit
        | Int digit
    '''
    if len(p) == 2:
        p[0] = int(p[1])
    else:
        num_1 = str(p[1]) + str(p[2])
        p[0] = int(num_1)


def p_String(p):
    '''
    String : Comillas Prim Comillas
            | Comillas Tuples Comillas
    '''
    p[0] = p[2]


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()
