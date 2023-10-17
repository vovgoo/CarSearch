from itertools import combinations

def null_test(number):
    null_test = [0,4,5]
    result = []
    for item in range(len(number)):
        if item in null_test and number[item] == "0":
            result.append("o")
        else:
            result.append(number[item])
    return "".join(result)

def number_mask(number):
    mask = [str,int,int,int,str,str,int,int,int]
    number = null_test(number)
    
    for item in range(len(number)):  
        if mask[item] == int:
            try:
                result = int(number[item])
            except:
                return False      
        elif(mask[item] == str):
            try:
                result = int(number[item])
                return False
            except:
                pass
    return True

def get_number_car(lists):
    for case in range(len(lists)):
        if len(lists) != 1:
            result = list(combinations(lists, case))
            for item in result:
                item = "".join(list(item))
                item = null_test(item)
                if (len(item) == 8 or len(item) == 9):
                    if(number_mask(item) == True):
                        return item
        else:
            result = lists[0]
            result = null_test(result)
            if (len(result) == 8 or len(result) == 9):
                if(number_mask(result) == True):
                    return result
    return False

    