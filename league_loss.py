import requests
from dotenv import load_dotenv
import os
import json
from utils import getMatchResult, createMessage
import time

load_dotenv()

response = requests.get(f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{os.getenv("USER_NAME")}/{os.getenv("USER_TAG")}', params= {"api_key": os.getenv("RIOT_KEY")})

leagueName = response.json()

puuid = leagueName["puuid"]

partidas_cache = []

while True:
    matches = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=5', params= {"api_key": os.getenv("RIOT_KEY")})

    partidas = matches.json()

    novas_partidas = [p for p in partidas if p not in partidas_cache]

    if not novas_partidas:
        createMessage([], os.getenv("USER_PHONE"))
    else:
        partidas_cache.extend(novas_partidas)

        resultados = [getMatchResult(partida, puuid) for partida in partidas]

        createMessage(resultados, os.getenv("USER_PHONE"))
    
    time.sleep(3600)



