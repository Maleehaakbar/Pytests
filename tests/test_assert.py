import pytest
from src.assert_exceptions import(
    division,
    deletefile
)
def test_division():
    """
    Test that a ZeroDivisionerror raised when divide by zero
    """
    with pytest.raises(ZeroDivisionError) as excinfo:
        division(1,1)
        assert str(excinfo.Value)=="Zero division error"

def test_delete_file_not_found_error():  
    """  
    Test that a FileNotFoundError is raised when the file does not exist  
    """  
    with pytest.raises(FileNotFoundError) as excinfo:  
        deletefile("non_existent_file.txt")  
    assert str(excinfo.value) == "File non_existent_file.txt not found"  

