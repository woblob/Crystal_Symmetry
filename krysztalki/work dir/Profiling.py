import cProfile, pstats, io
from functools import wraps

def profiler(sortby):
    def wraper(fnc):    
        @wraps(fnc)
        def inner(*args, **kwargs):        
            pr = cProfile.Profile()
            pr.enable()
            for i in range(1):
                retval = fnc(*args, **kwargs)
            pr.disable()
            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s)
            ps.sort_stats(sortby).print_stats()
            print(s.getvalue())
            return retval#, ps
        return inner
    return wraper

def profile_old(fnc):    
    """A decorator that uses cProfile to a function"""    
    @wraps(fnc)
    def inner(*args, **kwargs):        
        pr = cProfile.Profile()
        pr.enable()
        for i in range(1):
            retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner