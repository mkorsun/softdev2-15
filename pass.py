
lcase = [chr(ord('a')+p) for p in range(0,36)]
ucase = [chr(ord('A')+p) for p in range(0,36)]
nan = '.?!&#,;:-_*'

def checkmin(password):
    lower = [x for x in password if x.islower()]
    upper = [x for x in password if x.isupper()]
    number = [x for x in password if x.isdigit()]
    if lower and upper and number:
        return True
    else:
        return False

def strength(password):
    lower = [x for x in password if x.islower()]
    upper = [x for x in password if x.isupper()]
    number = [x for x in password if x.isdigit()]
    nothing = [x for x in password if x in nan]
    score = 0
    if not checkmin(password):
        return False;
    if len(lower) + len(upper) > 3:
        score +=1;
    if len(lower) + len(upper) > 5:
        score +=1;
    if len(lower) + len(upper)> 7:
        score +=1;
    if len(lower) + len(upper) > 10:
        score +=1;
    if len(number)  > 1:
        score +=1;
    if len(number)  > 2:
        score +=1;
    if len(number)  > 3:
        score +=1;
    if len(nothing)  > 1:
        score +=1;
    if len(nothing)  > 2:
        score +=1;
    if len(nothing)  > 3:
        score +=1;
    return score;
 
    
        
        
    

print strength('aB1fDw6')
print strength('ab1df6')

    
