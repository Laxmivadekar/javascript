catA=int(input('enter the catA position: '))
catB=int(input('enter the catB position: '))
mouse=int(input('enter the mouse position: '))
catA_diff=mouse-catA
catB_diff=catB-mouse
if catA_diff!=catB_diff:
    print('catB')
elif catA_diff==catB_diff:
    print('mouse')
elif catA<mouse and catA>catB:
    print('catA')
elif catB<mouse and catB>catA:
    print('catB')
elif mouse<catB and catB>catA:
    print('catB')
elif mouse<catA and catA>catB:
    print('catA')
else:
    print('nothing')
