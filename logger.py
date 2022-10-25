import datetime
def logger(function):
    def func(*args, **kwargs):
        result = function(*args, **kwargs)
        with open(kwargs['path'], "a") as log:
            log.write(f'{datetime.datetime.now()}\n')
            log.write(f'Вызвана фурнкция {function} с аргументами {args}\n\n')
        return result
    return func