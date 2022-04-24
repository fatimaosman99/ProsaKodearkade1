import datetime
def isItEaster2023():
    print("This program tells when it is easter. It checks today's date and sees if it's easter. It only checks 2023's easter though.")
    print("Is it easter?")
    if datetime.datetime.now() == datetime.datetime(2023, 4, 9):
        print("it is easter.")
    else:
        print("it is not.")
 
isItEaster2023()

