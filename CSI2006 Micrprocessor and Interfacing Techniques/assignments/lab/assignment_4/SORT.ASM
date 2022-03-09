.model small
.stack 64
.data
List DW  64h, 17h, 25h, 05h
Count EQU 04h
.code
start:Mov Ax,@data
      Mov DS,Ax
      Mov Dx,Count-1
Again0:Mov Cx,Dx
       Lea Si,List
Again1:Mov Ax,[Si]
       Cmp Ax,[Si+2]
       JL PR1
       XCHG [Si+2],Ax
       XCHG [Si],Ax
   PR1:ADD Si,02h
       Loop Again1
       Dec Dx
       JNZ Again0
       Mov Ah,4Ch
       int 21h
       hlt
       end
