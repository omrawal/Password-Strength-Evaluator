import re


def shallowCheck(password):
    count = 1
    if len(password) == 0:
        return 0
    if len(password) < 4:
        return 1
    if len(password) > 8:
        count += 1
    if re.search("[0-9]", password):
        count += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        count += 1
    if re.search(".", password):
        count += 1
    if re.search(r"[!#$%&()*+,-./:;<=>?@[\]^_{|}~]", password):
        count += 1
    return count


def deepCheck(password):
    listCheckpass = password+'\n'
    common200 = open('Assets\\200_common_password.txt')
    common200_lst = common200.readlines()
    res = listCheckpass in common200_lst
    index = None
    if(res):
        index = common200_lst.index(listCheckpass)
    return(res, index)


def fullcheck(password):
    listCheckpass = password+'\n'
    common10k = open('Assets\\10k-most-common.txt')
    common10k_lst = common10k.readlines()
    res = listCheckpass in common10k_lst
    index = None
    if(res):
        index = common10k_lst.index(listCheckpass)
    return(res, index)


def checkPass(password, flag=0):
    # password = ""
    # flag==0 implies shallow check
    # flag==1 implies deep check
    # flag==2 implies fullcheck

    responses = ['password cannot be Blank', 'Very Weak',
                 'Weak', 'Medium', 'Strong', 'Very Strong', 'Very Very Strong']

    if(flag == 0):
        pass
    elif(flag == 1):
        pass

    count = shallowCheck(password)
    if(count >= len(responses)):
        passwordStr = 'Likely Unbreakable!!!'
    else:
        passwordStr = responses[count]
    return passwordStr


request = input("Enter Password:")
print(checkPass(request))
