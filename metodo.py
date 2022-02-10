def descuento1(sueldo,categ):
    if categ==1:
        desc1=sueldo*0.12
    elif categ==2:
        desc1=sueldo*0.10
    elif categ==2:
        desc1=sueldo*0.08
    elif categ==2:
        desc1=sueldo*0.06
    else:
        desc1=sueldo*0.04
    return str(round(desc1,2))+" S/."

def descuento2(sueldo,categ):
    if categ==1:
        desc2=sueldo*0.10
    elif categ==2:
        desc2=sueldo*0.08
    elif categ==2:
        desc2=sueldo*0.06
    elif categ==2:
        desc2=sueldo*0.04
    else:
        desc2=sueldo*0.02
    return str(round(desc2,2))+" S/."

def bonificacion1(sueldo,categ):
    if categ==1:
        bono1=sueldo*0.14
    elif categ==2:
        bono1=sueldo*0.12
    elif categ==2:
        bono1=sueldo*0.10
    elif categ==2:
        bono1=sueldo*0.08
    else:
        bono1=sueldo*0.06
    return str(round(bono1,2))+" S/."

def bonificacion2(sueldo,categ):
    if categ==1:
        bono2=sueldo*0.16
    elif categ==2:
        bono2=sueldo*0.14
    elif categ==2:
        bono2=sueldo*0.12
    elif categ==2:
        bono2=sueldo*0.10
    else:
        bono2=sueldo*0.08
    return str(round(bono2,2))+" S/."


