import os

  
def division(a:int|float ,b:int|float)-> float | ZeroDivisionError:  #function annotation
    """
    returns result of dividing a and b
    """
    try:
        return a/b 
    except:
        raise ZeroDivisionError ("Zero Division Error")
def deletefile(filename:str)-> None|FileNotFoundError:
    """
    Delete file
    """
    try:
        os.remove(filename)
    except:
        raise FileNotFoundError ("File not Found")

    