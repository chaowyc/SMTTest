import os
import commands
import xlsxwriter
import datetime
import KThread

def CluTime(caseName):
    return commands.getoutput('time -o res.txt -a z2 -smt caseName')

class Timeout(Exception):
    """function run timeout"""

def timeout(seconds):
    def timeout_decorator(func):
        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):
            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))
        def _(*args, **kwargs):
            result = []
            new_kwargs = {  # create new args for _new_func, because we want to get the func return val to result list
                'oldfunc': func,
                'result': result,
                'oldfunc_args': args,
                'oldfunc_kwargs': kwargs
            }
            thd = KThread(target=_new_func, args=(), kwargs=new_kwargs)
            thd.start()
            thd.join(seconds)
            alive = thd.isAlive()
            thd.kill()  # kill the child thread
            if alive:
                raise Timeout(u'function run too long, timeout %d seconds.' % seconds)
            else:
                return result[0]
        _.__name__ = func.__name__
        _.__doc__ = func.__doc__
        return _
    return timeout_decorator

def OpenDir(inputDir):
    files = os.listdir(inputDir)
    for item in files:
        if item[0] == '.':
            pass
        elif os.path.isdir(inputDir + '/' + item):
            OpenDir(inputDir + '/' + item)
        elif os.path.isfile(inputDir + '/' + item):
            if item.endswith('.txt'):
                pass
            else:
                print inputDir + '/' + item
                s = inputDir + '/' + item
                start = datetime.datetime.now()

                output = CluTime(s)
                end = datetime.datetime.now()
                return inputDir + '/' + item