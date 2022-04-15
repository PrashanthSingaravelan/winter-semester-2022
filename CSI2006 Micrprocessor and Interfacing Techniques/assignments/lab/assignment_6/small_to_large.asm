.model small
.stack 100h
.data
text db 'TEAM ASSIGNMENT'
count dw 05
.code
Start:Mov Ax, @data
Mov Ds, Ax
Mov ES, Ax
Mov SI,offset text
Mov Cx, count
again:Mov Al, [SI]
Add Al, 20h
Mov [SI],Al
Inc SI
Loop again
Mov Ah, 4Ch
INT 21h
end start