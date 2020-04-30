import ply.yacc as yacc

from ANDREW.ArrayStack import ArrayStack
from FRANCISCO.DoublyLinkedQueue import DoublyLinkedQueue
from JORGE.ArraySet import ArraySet
from Scanner import tokens

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
def p_Program(p):
    ''' Program : Declaration Declaration 
                | Declaration 
                | 
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    elif len(p) == 2:
        p[0] = p[1]


def p_Declaration(p):
    ''' Declaration : InputOptionalStruct LT Elements GT
                    | InputRequiredStruct  LT Elements GT
                    | Structures Id Assign LT GT
    '''
    if len(p) == 9:
        if(p[1] == 'InputOptionalStruct'):
            p[0] = p[1] + p[2] + p[3] + p[4] + p [5] + p[6] + p[7] + p[8]
        else:
            p[0] = p[1] + p[2] + p[3] + p[4] + p [5] + p[6] + p[7] + p[8]    
    elif len(p) == 8:
        p[0] = p[1] + p[2] + p[3] + p[4] + p [5] + p[6] + p[7]
    elif len(p) == 7:
        p[0] = p[1] + p[2] + p[3] + p[4] + p [5] + p[6]
    elif len(p) == 5:
        p[0] = p[1] + p[2] + p[3] + p[4]


def p_Elements(p): 
    ''' Elements : Bool
                  | Int
                  | String
                  | Elements Separator Elements
                  |
    '''

def p_Structures(p):
    ''' Structures : Stack
                    | DLQ
                    | Map
                    | AL
                    | CDLL
                    | AS
                    | Set
                    | Bag
    '''
    if p[1] == 'AS':
        p[0] = ArrayStack()
    elif p[1] == 'DLQ':
        p[0] = DoublyLinkedQueue()
    elif p[1] == 'AL':
        p[0] = ArrayList()
    elif p[1] == 'CDLL':
        p[0] = CDLinkedList()
    elif p[1] == 'Bag':
        p[0] = DynamicBag()
    elif p[1] == 'Set':
        p[0] = ArraySet()
        
def p_InputRequiredStruct(p):
    ''' InputRequiredStruct :  Tree  Id Assign LP Comparator RP 
                            |  SArrayList  Id Assign LP Comparator RP 

    '''
    if p[1] == 'Tree':
        p[0] = BinarySearchTree(p[5])
    elif p[1] == 'SArrayList':
        p[0] = SArrayList(p[5])

