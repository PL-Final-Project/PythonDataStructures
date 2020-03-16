This Folder contains the implementation of Hash Table in the Python programming language
It exists in two modalities:
-Open Address
--Implementation that only uses map entries and the basic array to insert elements with hash code variables
--In case hashing fails to not collide, it will use a squared hashing function in an attempt to find space
--Worst case is a linear probing system that keeps looking for element in a linear sequence
-Separate Chaining
--Implementation that uses the main array with linked lists in order to keep allocating elements that collide in the
--same index. It's design to only hold a maximum of 2 elements to diminish the complexity time in case of multiple
--collisions. In case that the capacity has reached a 70%, it will reallocate

It also contains the Map "Interface". Technically it's not an interface but an abstract class that forces the
implementation of the designated methods.