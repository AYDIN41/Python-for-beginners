def ucgenMi(liste):

    if(abs(liste[2]) == (abs(liste[1]) ** 2 + abs(liste[0]) ** 2 ) ** 0.5):
        return True
    else:
        return False
liste1= [(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(ucgenMi,liste1)))
