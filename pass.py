
lcase = [chr(ord('a')+p) for p in range(0,36)]
ucase = [chr(ord('A')+p) for p in range(0,36)]

def checkmin(password):
    lower = [x for x in password if x.islower()]
    upper = [x for x in password if x.isupper()]
    number = [x for x in password if x.isdigit()]
    if lower and upper and number:
        return True
    else:
        return False

print checkmin('aB1fDw6')
print checkmin('ab1df6')

    
