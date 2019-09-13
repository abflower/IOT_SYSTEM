# This file contains the automation class

# every automation has
# - id
# - name
# - parameters
# - name of the service used (this is also used to define conditions)
# - day(s) of execution
# - time range of execution
# - condition of execution

class automation():
    # with the following method I can set an arbitrary number 
    # of properties to the class passing n labelled arguments.

    # positional arguments, used to assign value to some of the 
    # properties, become compulsory at the moment of the creation
    # of an instance of the class. 
    # Also these args CAN be passed as labelled ones. 
            
    def __init__(self,aut_id,name, **kwargs):
        self.aut_id = aut_id
        self.name = name
        self.__dict__.update(kwargs)

    def print_all_attrs(self):
        for k in self.__dict__:
            print('%s = %s'%(k, self.__dict__[k]))

dictionary = {'musta':'wow', 'yougurt':'dairy'}
auto3 = automation(1, 'papaya')
auto3.print_all_attrs()

#print(dictionary.items())