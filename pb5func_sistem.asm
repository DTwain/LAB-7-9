bits 32 ;asamblare și compilare pentru arhitectura de 32 biți
; definim punctul de intrare in programul principal
global start

; declaram functiile externe necesare programului nostru 
extern exit,printf ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import exit msvcrt.dll  ; exit este o functie care incheie procesul, este definita in msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante
 
segment data use32 class=data

a dw 23
b dw 5

copie_a dd 23
copie_b dd 5
format_afiare db "%d mod %d = %d", 0
    
; segmentul de cod
segment code use32 class=code
    start:
    
    mov ax, [a]
    cwd
    idiv word [b]

    mov ax, dx
    cwde
    
    ;print sum
    push eax
    push dword [copie_b]
    push dword [copie_a]
    push dword format_afiare
    call [printf]
    add esp, 16
    

    push dword 0
    call [exit]