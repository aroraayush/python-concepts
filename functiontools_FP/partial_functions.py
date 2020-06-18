from functools import partial

# Checking email for Gmail server, only username is required

def email(username, domain, extension):
    print(username + domain + extension)

# Syntax 
# def partial(func, *args, **keywords)
# Return a new partial object which when called will behave like func
# called with the positional arguments args and keyword arguments keywords. 
# If more arguments are supplied to the call, they are appended to args.

 # email_obj:  functools.partial(<function email at 0x109ab2488>, 'ayusharora009')
email_obj = partial(email, "test1")
email_obj2 = partial(email, "test2")

remaining_args = ["@gmail",".com"]

email_obj(*remaining_args)
email_obj2(*remaining_args)