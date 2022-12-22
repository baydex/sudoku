
def showMatrix(matrix, etiqueta = ""):
    print("-------")
    if etiqueta != "": print(etiqueta)
    for row in matrix:
        print(row)
    print("-------")

def extractMatrices(groups):
    matrices = 0
    for group in groups:
        matrices+=len(group.missingNumbers)

    return matrices
