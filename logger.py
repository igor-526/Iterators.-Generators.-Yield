import datetime
def logger(function):
    def func(lists):
        with open("log.txt", "a") as log:
            log.write(f'{datetime.datetime.now()}')
        result = function(lists)
        return result
    return func