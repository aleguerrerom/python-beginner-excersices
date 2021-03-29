# Your code here!!
def sing():
    cancion = ""
    for i in range (10):
        if i == 4:
            cancion = cancion + ("whisper words of wisdom, let it be, let it be,")
        elif i == 8:
            cancion = cancion + ("there will be an asnwer, let it be")
        else :
            cancion = cancion + ("let it be,")
    return cancion

print(sing())
        





