import requests
import os
import pywhatkit as kit

def getMatchResult(partida, puuid):
    partida = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/{partida}', params= {"api_key": os.getenv("RIOT_KEY")})
    for info in partida.json()["info"]["participants"]:
        if info.get("puuid") == puuid:
            return info.get("win")

def createMessage(resultados, phone):
    if len(resultados) == 0:
        kit.sendwhatmsg_instantly(phone, "Vai jogar filho o bot tem que funcionar aqui")
    else:
        derrotas = sum(1 for result in resultados if result is False)
        kit.sendwhatmsg_instantly(phone, f"Parabéns pelas {derrotas} derrotas atuais!")