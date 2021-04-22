import re


def shallowCheck(password):
    # print('In Shallow Check')
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
    # print('In Deep Check')
    listCheckpass = password+'\n'
    common200 = open('Assets\\200_common_password.txt')
    common200_lst = common200.readlines()
    res = listCheckpass in common200_lst
    index = None
    if(res):
        index = common200_lst.index(listCheckpass)
    return(res, index)


def fullCheck(password):
    # print('In Full Check')
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
    checkResponseFlag = False

    responses = ['password cannot be Blank', 'Very Weak',
                 'Weak', 'Medium', 'Strong', 'Very Strong', 'Very Very Strong']

    if(flag == 0):
        count = shallowCheck(password)
    elif(flag == 1):
        deepResponse = deepCheck(password)
        if(deepResponse[0]):
            checkResponseFlag = True
        else:
            count = shallowCheck(password)

    elif(flag == 2):
        fullResponse = fullCheck(password)
        if(fullResponse[0]):
            checkResponseFlag = True
        else:
            count = shallowCheck(password)
    else:
        return False
    # count = shallowCheck(password)
    if(checkResponseFlag):
        if(flag == 1):
            # assuming it takes 1.25 sec to bruteforce 1 password
            time = (deepResponse[1]+1)*1.25
            res_str = 'It would take Approx {} secs to crack this password!\n\
            This password was {} th in the wordlist'.format(str(time), str(deepResponse[1]+1))
            return res_str
        elif(flag == 2):
            # assuming it takes 1.25 sec to bruteforce 1 password
            time = (fullResponse[1]+1)*1.25
            res_str = 'It would take Approx {} secs to crack this password!\n\
            This password was {} th in the wordlist'.format(str(time), str(fullResponse[1]+1))
            return res_str
    else:
        if(count >= len(responses)):
            return 'The password is '+'Likely Unbreakable!!!'
        else:
            return 'The password is '+responses[count]


# request = input("Enter Password: ")

# print(shallowCheck('Bu$Hy'))
