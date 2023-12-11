bits 32 ;asamblare și compilare pentru arhitectura de 32 biți
; definim punctul de intrare in programul principal
global start

; declaram functiile externe necesare programului nostru 
extern exit,printf,scanf ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import exit msvcrt.dll  ; exit este o functie care incheie procesul, este definita in msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante
 


; segmentul de date in care se vor defini variabilele 
segment data use32 class=data

 
a resb 1000
format_citire db "%s", 0
 



    
; segmentul de cod
segment code use32 class=code
    start:
    
    push dword a
    push dword format_citire
    call [scanf]
    add esp,4*2
     

    push dword 0
    call [exit]