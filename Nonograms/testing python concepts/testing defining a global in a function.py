#testing defining a global in a function.py
def create_global():
    '''creates a global'''
    global tester
    tester = "This is defined in a function"

def test_global():
    print(tester)

# create_global()
create_global()
test_global()
