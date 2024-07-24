
import sys

def fun_pal(arg_cmd):
    if arg_cmd == arg_cmd[::-1]:
        return True, arg_cmd[::-1]
    else:
        return False, arg_cmd[::-1]

arg_cmd = (sys.argv[1])
print(arg_cmd)
print(fun_pal(arg_cmd))