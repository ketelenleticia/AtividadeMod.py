def calcular_media(listanotas):
    media=sum(listanotas)/len(listanotas)
    return media

def verificar_situacao(media):
    if media >=7:
        return "aprovado"
    elif media>5 and media <= 6.9:
        return "recuperaçao"
    else:
        return "reprovado"
