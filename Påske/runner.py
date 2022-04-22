import datetime
def isItEaster2023():
    print("Is it easter?")
    if datetime.datetime.now() == datetime.datetime(2023, 4, 9):
        print("it is easter.")
    else:
        print("it is not.")
 
isItEaster2023()

