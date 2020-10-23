def add(a, b):
    return float(a) + float(b)


def subtraction(a, b):
    return float(a) - float(b)


def multiply(a, b):
    return float(a) * float(b)


def division(a, b):
    return float(a) / float(b)


def reverse(a):
    return -float(a)


def Calculator_rules(result = []):
    multiply_count = result.count('*')
    division_count = result.count('/')
    add_count = result.count('+')
    subtraction_count = result.count('-')

    """for element in result:
        if element == '1' or element == '2' or element == '3' or element == '4' or element =='5' or element == '6' or element == '7' or element == '8' or element == '9':
            element_index = result.index(element)
            while (result[element_index+1] == '1' or result[element_index+1] == '2' or result[element_index+1] == '3' or result[element_index+1] == '4' or result[element_index+1] == '5' or result[element_index+1] == '6' or result[element_index+1] == '7' or result[element_index+1] == '8' or result[element_index+1] == '9' or result[element_index+1] == '0'):
                print(element_index)
                new_element = element.join(result[element_index+1])
                print(new_element)
                del(result[element+1])
            result.insert(element_index, new_element)"""

    for element in result:
        #如果遇到'.'的处理
        if element == '.':
            element_index = result.index(element)
            new_element2 = []
            for i in range(element_index-1, element_index+2):
                new_element1 = str(result[i])
                new_element2.append(new_element1)
            for i in range(element_index-1, element_index+2):
                result.pop(element_index-1)
            new_element = float("".join(new_element2))
            result.insert(element_index-1, new_element)
    
    #如果遇到*或/的处理
    while(multiply_count>=1 or division_count>=1):
        for element in result:
            if element == '*':
                element_index = result.index(element)
                result.insert(element_index-1, multiply(result[element_index-1], result[element_index+1]))
                for i in range(element_index, element_index+3):
                    del(result[element_index])
                multiply_count = multiply_count -1
            if element == '/':
                element_index = result.index(element)
                result.insert(element_index-1, division(result[element_index-1], result[element_index+1]))
                for i in range(element_index, element_index+3):
                    del(result[element_index])
                division_count = division_count -1
    
    #如果遇到+或-的处理
    while(add_count>=1 or subtraction_count>=1):
        for element in result:
            if element == '+':
                element_index = result.index(element)
                result.insert(element_index-1, add(result[element_index-1], result[element_index+1]))
                for i in range(element_index, element_index+3):
                    del(result[element_index])
                add_count = add_count -1
            if element == '-':
                element_index = result.index(element)
                result.insert(element_index-1, subtraction(result[element_index-1], result[element_index+1]))
                for i in range(element_index, element_index+3):
                    del(result[element_index])
                subtraction_count = subtraction_count -1

    for element in result:
        #如果遇到取反的处理
        if element == '+/-':
            element_index = result.index(element)
            result.insert(element_index-1, reverse(float(result[element_index-1])))
            for i in range(element_index, element_index+2):
                result.pop(element_index)

    """if len(result) == 1:
        return float(result)
    else:
        return result"""
    return result

"""print(Calculator_rules(['2', '.', '3', '*', '2', '.', '4', '+', '6', '/', '2', '+/-'])) """        
