from ply import yacc

from Get import super_get, super_get_index
from RemoveAll import super_removeAll
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
from Add import *
from Print import *
from Remove import *
from Contains import *
from Clear import *
from lexer import tokens
import ply.yacc as yacc


elements = []
generatedStructs = {}

messages = []


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
    ''' Action : use Id Assign add Prim
                | use Id Assign add Tuples
                | use Id Assign remove Prim
                | use Id Assign remove Tuples
                | use Id Assign contains Prim
                | use Id Assign contains Tuples
                | use Id Assign clear
                | use Id Assign get Prim
                | use Id Assign get Tuples
                | use Id Assign get index Assign Int
                | use Id Assign removeAll Prim
                | use Id Assign removeAll Tuples
                | print Id
    '''
    # ---------- ADD --------------------
    if generatedStructs.get(p[2]) is not None and len(p) == 6 and str(p[4]) == 'add':
        super_add(p)
    # ------ REMOVE -----------
    elif generatedStructs.get(p[2]) is not None and len(p) == 6 and str(p[4]) == 'remove':
        super_remove(p)
    # ---------- CONTAINS ------------------------
    elif generatedStructs.get(p[2]) is not None and len(p) == 6 and str(p[4]) == 'contains':
        super_contains(p)
    # --------- PRINT -------------
    elif len(p) == 3:
        super_print(p)
    # ---------- REMOVE_ALL (element)-------------
    elif generatedStructs.get(p[2]) is not None and len(p) == 6 and str(p[4]) == 'removeAll':
        super_removeAll(p)
    # ---------- CLEAR ---------------------------
    elif len(p) == 5 and p[4] == 'clear':
        super_clear(p)
    # ---------- GET -----------------------------
    elif p[4] == 'get':
        if len(p) == 6:
            super_get(p)
        else:
            super_get_index(p)


def p_Declaration(p):
    ''' Declaration : InputOptionalStruct LT Elements GT
                    | InputRequiredStruct LT Elements GT
                    | Structures Id Assign LT Elements GT
                    | InputOptionalStruct LT  GT
                    | InputRequiredStruct LT  GT
                    | Structures Id Assign LT  GT
    '''
    # ----- STRUCTURES --------------
    if len(p) == 7:
        temp_elements = p[5]
        print(temp_elements)
        if isinstance(p[1], Map):
            p[1] = map_elements(p[1], temp_elements)
            generatedStructs[str(p[2])] = ("Map", p[1])
        elif isinstance(p[1], CircularDoublyLinkedList):
            p[1] = cdll_elements(p[1], elements)
            generatedStructs[str(p[2])] = ("CDLL", p[1])
        elif isinstance(p[1], SinglyLinkedList):
            p[1] = linkedlist_elements(p[1], elements)
            generatedStructs[str(p[2])] = ("SLL", p[1])
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
        elif isinstance(p[1], BinarySearchTree):
            tree_elements(p[1], temp_elements)
    elif len(p) == 6:
        if isinstance(p[1], Map):
            generatedStructs[str(p[2])] = ("Map", p[1])
        elif isinstance(p[1], CircularDoublyLinkedList):
            generatedStructs[str(p[2])] = ("CDLL", p[1])
        elif isinstance(p[1], SinglyLinkedList):
            generatedStructs[str(p[2])] = ("SLL", p[1])
        elif isinstance(p[1], DynamicBag):
            generatedStructs[str(p[2])] = ("Bag", p[1])
        elif isinstance(p[1], ArraySet):
            generatedStructs[str(p[2])] = ("Set", p[1])
        elif isinstance(p[1], Stack):
            generatedStructs[str(p[2])] = ("Stack", p[1])
        elif isinstance(p[1], DoublyLinkedQueue):
            generatedStructs[str(p[2])] = ("Queue", p[1])
    
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
                    | SLL
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
    elif p[1] == 'SinglyLinkedList':
        p[0] = SinglyLinkedList()


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
            p[0] = HashTableOA(p[5], p[7])
            generatedStructs[str(p[2])] = ('HSOA', p[0])
    if p[1] == 'HashTableSC':
        if len(p) == 6:
            p[0] = HashTableSC()
            generatedStructs[str(p[2])] = ('HSSC', p[0])
        else:
            p[0] = HashTableSC(p[5], p[7])
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
    messages.append("Syntax error")


release_parser = yacc.yacc()
