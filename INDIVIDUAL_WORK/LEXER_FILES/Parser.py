import ply.yacc as yacc
import logging
from click._compat import raw_input
from Scanner import tokens


from Scanner import tokens

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
def p_Program(p):
    ''' Program : Declaration Declaration 
                | Declaration 
                | 
    '''
    # if len(p) == 3:
    #     p[0] = p[1] + p[2]
    # elif len(p) == 2:
    #     p[0] = p[1]


def p_Declaration(p):
    ''' Declaration : InputOptionalStruct LT Elements GT
                    | InputRequiredStruct LT Elements GT
                    | Structures Id Assign LT Elements GT
    '''
    # if len(p) == 5:
    #     if(p[1] == 'InputOptionalStruct'):
    #         p[0] = p[1] + p[2] + p[3] + p[4] 
    #     else:
    #         p[0] = p[1] + p[2] + p[3] + p[4]  
    # elif len(p) == 6:
    #         p[0] = p[1] + p[2] + p[3] + p[4] + p[5]  
        


def p_Elements(p): 
    ''' Elements : Bool
                  | Int
                  | Id
                  | String
                  | Elements Separator Elements
                  |
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = None

def p_Structures(p):
    ''' Structures : DLQ 
                    | Map
                    | AL
                    | CDLL
                    | AS
                    | Set
                    | Bag
    '''
    # if p[1] == 'AS':
    #     p[0] = ArrayStack.Stack()
    # elif p[1] == 'DLQ':
    #     p[0] = DoublyLinkedQueue()
    # elif p[1] == 'AL':
    #     p[0] = None
    # elif p[1] == 'CDLL':
    #     p[0] = CircularDoublyLinkedList.CircularDoublyLinkedList()
    # elif p[1] == 'Bag':
    #     p[0] = DynamicBag.DynamicBag()
    # elif p[1] == 'Set':
    #     p[0] = ArraySet.ArraySet()
        
def p_InputRequiredStruct(p):
    ''' InputRequiredStruct :  Tree  Id Assign LP StringComp RP 
                            |   Tree  Id Assign LP NumberComp RP 
                            |  SArrayList  Id Assign LP StringComp RP 
                            |  SArrayList  Id Assign LP NumberComp RP 

    '''
    # if p[1] == 'Tree':
    #     p[0] = BinarySearchTree.BinarySearchTree(p[5])
    # elif p[1] == 'SArrayList':
    #     p[0] = SortedArrayList.SortedArrayList(p[5])

def p_InputOptionalStruct(p):
    ''' InputOptionalStruct : HSOA Id Assign LP StringComp RP
                            | HSOA Id Assign LP NumberComp RP
                            | HSSC Id Assign LP StringComp RP
                            | HSSC Id Assign LP NumberComp RP
                            | HSSC Id Assign LP RP
                            | HSOA Id Assign LP RP
    '''   
    # if len(p) == 6:            
    #     if p[1] == 'HashTableOA':
    #         p[0] = HashTableOA.HashTableOA(p[5])
    #     elif p[1] == 'HashTableSC':
    #         p[0] = HashTableSC.HashTableSC(p[5])
    # elif len(p) == 5:
    #     if p[1] == 'HashTableOA':
    #         p[0] = HashTableOA.HashTableOA()
    #     elif p[1] == 'HashTableSC':
    #         p[0] = HashTableSC.HashTableSC()

def p_Id(p):
    '''
    Id : character
        | Id digit
        | Id character
    '''
    
def p_Bool(p):
    '''
    Bool : True
        | False

    '''  
def p_Int(p):
    '''
    Int : digit
        | digit Int
    '''

def p_String(p):
    '''
    String : Comillas Elements Comillas           
    '''

def p_error(p):
    print("Syntax error")



parser = yacc.yacc()

logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue

    result = parser.parse(s, debug=log)
    print(result)