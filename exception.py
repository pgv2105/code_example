def handle_exception(*argexceptions, function=None, method=None, _return=None, notrace=False):

    def decorator(func):

        normalize = lambda x: x.replace('"','').replace('\n', '. ')
        functionname = func.__name__
        @wraps(func)

        def wrapper(*args, **kwargs):

            try:     
                return func(*args, **kwargs)

            except argexceptions as e:
                trc = [] if notrace else [ normalize(x)  for x in  traceback.format_tb(e.__traceback__) ]

                trc.append(f'{type(e)} in {func.__name__}: {normalize(str(e))}')

                print(trc, level='ERROR')  

                if function: function() 

                if method:  getattr(args[0],method)()

                if _return: return _return()

        return wrapper

    return decorator