import traceback

try:
    raise Exception("This is the error message.")
except:
    print(traceback.format_exc())
