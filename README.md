# Welcome to the PyDa documentation webpage
## Authors of this project:

 - Alberto I. Cruz Salamán
 - Andrew González Pérez
 - Jorge Ortiz 
 - Francisco J. Vera Orengo
 
## Purpose of this language:
The main purpose of this language is to be able to implement Data Structures easily in a format which most programmers are used to. The language used to base this program is Python. Python is the third most popular language in the world right now according to [Tiobe](https://www.tiobe.com/tiobe-index/). For this reason, we decided to implement the structures in Python for newcomers to be able to see how they work "behind the hood" if they wish, but the main goal is to be able to quickly implement data structures with its methods without coding them. The motivation behind this language is to help others to see the power of using Data Structures to store data in different formats. Some of the language features are the use of interfaces like other programming languages, use of comparators (i.e. NumberComp and StringComp) and the process of using map to store key value pairs.

## Data Structures implemented:

|        Structures        |                                   Methods                                   |
|:------------------------:|:---------------------------------------------------------------------------:|
| Map                      | size, isEmpty, get, put, remove, makeEmpty, containsKey, getKeys, getValues |
| SinglyLinkedList         | add, print, isEmpty, clear, get, removeLast, size                           |
| CircularDoublyLinkedList | add, print, isEmpty, clear, get, removeLast, size                           |
| BinarySearchTree         | isEmpty, get, put, containsKey, getKeys, getValues                          |
| DoublyLinkedQueue        | size, isEmpty, front, dequeue, enqueue, makeEmpty                           |
| ArrayStack               | isEmpty, push, pop, print                                                   |
| DynamicBag               | size, isEmpty, add, isMember, remove, removeAll, clear                      |
| ArraySet                 | size, isEmpty, add, isMember, remove, clear                                 |

## Method of implementation
In order to implement these data structures, every team member decided to code at least one of them in Python. The reason to choose this language was that it would be easier to import them in order for the parser to use it to generate intermediate code. After doing this, the scanner was implemented using lex from a library called [PLY](https://www.dabeaz.com/ply/). After defining the tokens and the structure of the program in the scanner, the parser and intermediate code was also designed using PLY, since its such a useful tool which facilitates the process. 

## How to run PyDa
In order to run PyDa, you need to have Python 3.6 downloaded and the IDE of your preference. After importing the files, click the run button. A text file should pop up, in which you can write the code following the video examples. After saving and closing the text file, check your IDE terminal to see the results. 
