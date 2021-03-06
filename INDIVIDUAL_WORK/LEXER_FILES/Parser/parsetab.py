
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AL AS Assign Bag CDLL Comillas DLQ False GT HSOA HSSC LP LT Map None NumberComp RP SArrayList SLL Separator Set StringComp Tree True add character digit print use Program : Declaration\n                | Program Separator Declaration\n                | Program Separator Action\n\n     Action : use Id add Prim\n                | use Id add Tuples\n                | print Id\n     Declaration : InputOptionalStruct LT Elements GT\n                    | InputRequiredStruct LT Elements GT\n                    | Structures Id Assign LT Elements GT\n                    | InputOptionalStruct LT  GT\n                    | InputRequiredStruct LT  GT\n                    | Structures Id Assign LT  GT\n     Tuples : LP Prim Separator Prim RP\n\n     Elements : Prim\n                  | Elements Separator Elements\n                  | Tuples\n     Prim : Bool\n                | Int\n                | Id\n                | String\n     Structures : DLQ\n                    | Map\n                    | AL\n                    | CDLL\n                    | AS\n                    | Set\n                    | Bag\n     InputRequiredStruct :  Tree Id Assign LP Comparator RP\n                            |  SArrayList Id Assign LP Comparator Separator Comparator RP\n     InputOptionalStruct : HSOA Id Assign LP Comparator Separator Comparator RP\n                            | HSSC Id Assign LP Comparator Separator Comparator RP\n                            | HSSC Id Assign LP RP\n                            | HSOA Id Assign LP RP\n     Comparator : NumberComp\n                    | StringComp\n    \n    Id : character\n        | Id digit\n        | Id character\n    \n    Bool : True\n        | False\n    \n    Int : digit\n        | Int digit\n    \n    String : Comillas Prim Comillas\n            | Comillas Tuples Comillas\n    '
    
_lr_action_items = {'HSOA':([0,17,],[6,6,]),'HSSC':([0,17,],[7,7,]),'Tree':([0,17,],[8,8,]),'SArrayList':([0,17,],[9,9,]),'DLQ':([0,17,],[10,10,]),'Map':([0,17,],[11,11,]),'AL':([0,17,],[12,12,]),'CDLL':([0,17,],[13,13,]),'AS':([0,17,],[14,14,]),'Set':([0,17,],[15,15,]),'Bag':([0,17,],[16,16,]),'$end':([1,2,21,26,27,31,34,35,36,37,39,40,41,44,46,47,53,54,56,60,69,70,72,81,82,84,89,],[0,-1,-36,-2,-3,-10,-17,-18,-19,-20,-39,-40,-41,-11,-37,-38,-6,-7,-42,-8,-43,-44,-12,-4,-5,-9,-13,]),'Separator':([1,2,21,26,27,30,31,32,33,34,35,36,37,39,40,41,43,44,46,47,53,54,56,57,60,67,69,70,71,72,73,75,76,77,80,81,82,84,89,],[17,-1,-36,-2,-3,55,-10,-14,-16,-17,-18,-19,-20,-39,-40,-41,55,-11,-37,-38,-6,-7,-42,68,-8,55,-43,-44,55,-12,85,-34,-35,86,88,-4,-5,-9,-13,]),'LT':([3,4,45,74,78,87,93,94,95,],[18,19,61,-33,-32,-28,-30,-31,-29,]),'character':([5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,28,29,36,38,42,46,47,52,53,55,61,66,68,],[21,21,21,21,21,-21,-22,-23,-24,-25,-26,-27,21,21,47,-36,47,47,47,47,21,21,47,21,21,-37,-38,47,47,21,21,21,21,]),'use':([17,],[28,]),'print':([17,],[29,]),'GT':([18,19,21,30,32,33,34,35,36,37,39,40,41,43,46,47,56,61,67,69,70,71,89,],[31,44,-36,54,-14,-16,-17,-18,-19,-20,-39,-40,-41,60,-37,-38,-42,72,-15,-43,-44,84,-13,]),'LP':([18,19,42,48,49,50,51,55,61,66,],[38,38,38,62,63,64,65,38,38,38,]),'True':([18,19,38,42,55,61,66,68,],[39,39,39,39,39,39,39,39,]),'False':([18,19,38,42,55,61,66,68,],[40,40,40,40,40,40,40,40,]),'digit':([18,19,20,21,22,23,24,25,35,36,38,41,42,46,47,52,53,55,56,61,66,68,],[41,41,46,-36,46,46,46,46,56,46,41,-41,41,-37,-38,46,46,41,-42,41,41,41,]),'Comillas':([18,19,21,34,35,36,37,38,39,40,41,42,46,47,55,56,58,59,61,66,68,69,70,89,],[42,42,-36,-17,-18,-19,-20,42,-39,-40,-41,42,-37,-38,42,-42,69,70,42,42,42,-43,-44,-13,]),'Assign':([20,21,22,23,24,25,46,47,],[45,-36,48,49,50,51,-37,-38,]),'add':([21,46,47,52,],[-36,-37,-38,66,]),'RP':([21,34,35,36,37,39,40,41,46,47,56,62,63,69,70,75,76,79,83,90,91,92,],[-36,-17,-18,-19,-20,-39,-40,-41,-37,-38,-42,74,78,-43,-44,-34,-35,87,89,93,94,95,]),'NumberComp':([62,63,64,65,85,86,88,],[75,75,75,75,75,75,75,]),'StringComp':([62,63,64,65,85,86,88,],[76,76,76,76,76,76,76,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'Declaration':([0,17,],[2,26,]),'InputOptionalStruct':([0,17,],[3,3,]),'InputRequiredStruct':([0,17,],[4,4,]),'Structures':([0,17,],[5,5,]),'Id':([5,6,7,8,9,18,19,28,29,38,42,55,61,66,68,],[20,22,23,24,25,36,36,52,53,36,36,36,36,36,36,]),'Action':([17,],[27,]),'Elements':([18,19,55,61,],[30,43,67,71,]),'Prim':([18,19,38,42,55,61,66,68,],[32,32,57,58,32,32,81,83,]),'Tuples':([18,19,42,55,61,66,],[33,33,59,33,33,82,]),'Bool':([18,19,38,42,55,61,66,68,],[34,34,34,34,34,34,34,34,]),'Int':([18,19,38,42,55,61,66,68,],[35,35,35,35,35,35,35,35,]),'String':([18,19,38,42,55,61,66,68,],[37,37,37,37,37,37,37,37,]),'Comparator':([62,63,64,65,85,86,88,],[73,77,79,80,90,91,92,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> Declaration','Program',1,'p_Program','parser.py',62),
  ('Program -> Program Separator Declaration','Program',3,'p_Program','parser.py',63),
  ('Program -> Program Separator Action','Program',3,'p_Program','parser.py',64),
  ('Action -> use Id add Prim','Action',4,'p_Action','parser.py',74),
  ('Action -> use Id add Tuples','Action',4,'p_Action','parser.py',75),
  ('Action -> print Id','Action',2,'p_Action','parser.py',76),
  ('Declaration -> InputOptionalStruct LT Elements GT','Declaration',4,'p_Declaration','parser.py',94),
  ('Declaration -> InputRequiredStruct LT Elements GT','Declaration',4,'p_Declaration','parser.py',95),
  ('Declaration -> Structures Id Assign LT Elements GT','Declaration',6,'p_Declaration','parser.py',96),
  ('Declaration -> InputOptionalStruct LT GT','Declaration',3,'p_Declaration','parser.py',97),
  ('Declaration -> InputRequiredStruct LT GT','Declaration',3,'p_Declaration','parser.py',98),
  ('Declaration -> Structures Id Assign LT GT','Declaration',5,'p_Declaration','parser.py',99),
  ('Tuples -> LP Prim Separator Prim RP','Tuples',5,'p_Tuples','parser.py',139),
  ('Elements -> Prim','Elements',1,'p_Elements','parser.py',146),
  ('Elements -> Elements Separator Elements','Elements',3,'p_Elements','parser.py',147),
  ('Elements -> Tuples','Elements',1,'p_Elements','parser.py',148),
  ('Prim -> Bool','Prim',1,'p_Prim','parser.py',164),
  ('Prim -> Int','Prim',1,'p_Prim','parser.py',165),
  ('Prim -> Id','Prim',1,'p_Prim','parser.py',166),
  ('Prim -> String','Prim',1,'p_Prim','parser.py',167),
  ('Structures -> DLQ','Structures',1,'p_Structures','parser.py',173),
  ('Structures -> Map','Structures',1,'p_Structures','parser.py',174),
  ('Structures -> AL','Structures',1,'p_Structures','parser.py',175),
  ('Structures -> CDLL','Structures',1,'p_Structures','parser.py',176),
  ('Structures -> AS','Structures',1,'p_Structures','parser.py',177),
  ('Structures -> Set','Structures',1,'p_Structures','parser.py',178),
  ('Structures -> Bag','Structures',1,'p_Structures','parser.py',179),
  ('InputRequiredStruct -> Tree Id Assign LP Comparator RP','InputRequiredStruct',6,'p_InputRequiredStruct','parser.py',196),
  ('InputRequiredStruct -> SArrayList Id Assign LP Comparator Separator Comparator RP','InputRequiredStruct',8,'p_InputRequiredStruct','parser.py',197),
  ('InputOptionalStruct -> HSOA Id Assign LP Comparator Separator Comparator RP','InputOptionalStruct',8,'p_InputOptionalStruct','parser.py',208),
  ('InputOptionalStruct -> HSSC Id Assign LP Comparator Separator Comparator RP','InputOptionalStruct',8,'p_InputOptionalStruct','parser.py',209),
  ('InputOptionalStruct -> HSSC Id Assign LP RP','InputOptionalStruct',5,'p_InputOptionalStruct','parser.py',210),
  ('InputOptionalStruct -> HSOA Id Assign LP RP','InputOptionalStruct',5,'p_InputOptionalStruct','parser.py',211),
  ('Comparator -> NumberComp','Comparator',1,'p_Comparator','parser.py',230),
  ('Comparator -> StringComp','Comparator',1,'p_Comparator','parser.py',231),
  ('Id -> character','Id',1,'p_Id','parser.py',241),
  ('Id -> Id digit','Id',2,'p_Id','parser.py',242),
  ('Id -> Id character','Id',2,'p_Id','parser.py',243),
  ('Bool -> True','Bool',1,'p_Bool','parser.py',254),
  ('Bool -> False','Bool',1,'p_Bool','parser.py',255),
  ('Int -> digit','Int',1,'p_Int','parser.py',265),
  ('Int -> Int digit','Int',2,'p_Int','parser.py',266),
  ('String -> Comillas Prim Comillas','String',3,'p_String','parser.py',277),
  ('String -> Comillas Tuples Comillas','String',3,'p_String','parser.py',278),
]
