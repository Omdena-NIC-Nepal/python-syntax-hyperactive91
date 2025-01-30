def format_string(name, age):
    name_new = name
    age_new = age
    return(f"My name is {name_new} and I am {age_new} years old")
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """

def conditional_check(number):
    num = number
    if num>10:
        return("Greater")
    elif num==10:
        return("Equal")
    else:
        return("Lesser")
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """

def loop_sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return(sum)

    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """

def list_operations(numbers):
    sum=0
    for i in numbers:
        sum+=i
    maximum=max(numbers)
    minimum=min(numbers)
    return(sum,maximum,minimum)


    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """

def dict_operations(students_dict):
    topstudents=[name for name, marks in students_dict.items() if marks>80]
    return(topstudents)
    

    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """

def set_operations(list1, list2):
    common=(x for x in list1 if x in list2)
    return(set(common))
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """

def arithmetic_ops(a, b):
    dict={"sum":a+b,"difference":a-b,"product":a*b,"quotient":a/b}
    return(dict)
    

    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """

def logical_ops(x, y):
    a=x and y
    b=x or y
    c=not x
    return({"and":a,"or":b,"not_x":c})
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """

def bitwise_ops(a, b):
    return({"and":a & b,"or":a | b,"xor": a ^ b})
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """

