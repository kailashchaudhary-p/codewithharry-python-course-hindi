#Match status in python 
def http_status(status):
    match status:
        case 100:
           return "continue"
        case 200:
            return "ok"
        case 500:
            return "unknown error"
        case _:
            return "invalid"
print(http_status(100))#when we give 100 it will return continue
print(http_status(200))#when we give 200 it will return ok