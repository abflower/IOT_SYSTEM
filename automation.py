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

    # If a dictionary is passed as kwargs, this is the syntax to use when calling
    # the function func(..., **dictionary_name)
            
    # def __init__(self, aut_id, name, service, params, condition_type, conditions, **kwargs):
    #     self.aut_id = aut_id
    #     self.name = name
    #     self.service = service
    #     self.params = params
    #     self.condition_type = condition_type
    #     self.conditions = conditions
    #     self.__dict__.update(kwargs)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def print_all_attrs(self):
        for k in self.__dict__:
            print('%s = %s'%(k, self.__dict__[k]))

# dictionary = {'say':'wow', 'yogurt':'dairy'}
# auto3 = automation(1, 'myname', 'tulup', 'params', **dictionary)
# auto3.print_all_attrs()

#print(dictionary.items())