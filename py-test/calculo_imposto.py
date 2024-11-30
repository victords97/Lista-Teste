def calcular_imposto(renda):
    if renda <= 2500:
        return 0
    elif renda <= 5000:
        return renda * 0.1
    else:
        return renda * 0.2