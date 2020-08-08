# This is like try with resources in Java
# If you open a file with context manager, it will automatically 
# gets closed once not in use or even in case of exception

# Tear down of resources is automatically handled

# Example: Connecting to databse, creating file,

# Syntax: with __________________ as obj:
#           obj

# declared via class or via decorators

# Usage
# with open('sample.txt','w') as f:
#     f.write('Lorem ipsum dolor sit amet, consecteur')

# Implementation
class Open_File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # Setup method
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # Teardown method
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

# ======== Using contextlib ============

# contextmanager
with Open_File('sample.txt','w') as f:
    f.write('testing')

print(f.closed)