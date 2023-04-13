import multiprocessing
import random
import threading
import time

import dearpygui.dearpygui as dpg
import configparser
from multiprocessing import Process

import os
import requests
import ssl
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=540, height=780)
#,always_on_top=True
dpg.create_context()




width, height, channels, data = dpg.load_image("jett.png")
with dpg.texture_registry():
    jett = dpg.add_static_texture(width, height, data)


width, height, channels, data = dpg.load_image("yoru.png")
with dpg.texture_registry():
    yoru = dpg.add_static_texture(width, height, data)


width, height, channels, data = dpg.load_image("reyna.png")
with dpg.texture_registry():
    reyna = dpg.add_static_texture(width, height, data)

width, height, channels, data = dpg.load_image("phoenix.png")
with dpg.texture_registry():
    phoenix = dpg.add_static_texture(width, height, data)

width, height, channels, data = dpg.load_image("neon.png")
with dpg.texture_registry():
    neon = dpg.add_static_texture(width, height, data)

width, height, channels, data = dpg.load_image("raze.png")
with dpg.texture_registry():
    raze = dpg.add_static_texture(width, height, data)

def ajan(ajann):
    print(ajann +" seçildi")
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.set('ajan-secimi', 'ajan', ajann)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)



def run_instalock():
    while True:
        lockfile = "".join(
            [os.getenv("LOCALAPPDATA"), r"\Riot Games\Riot Client\Config\lockfile"]
        )
        with open(lockfile, "r") as f:
            data = f.read().split(":")

        base_url = f"{data[4]}://127.0.0.1:{data[2]}"
        s = requests.Session()
        s.auth = ("riot", data[3])
        if exit_vakti:
            break

        r = s.get(base_url + "/entitlements/v1/token", verify=ssl.CERT_NONE)

        print(r.text)
        base64_access = (r.json()["accessToken"])

        r2 = requests.post("https://entitlements.auth.riotgames.com/api/token/v1", headers={
            "Authorization": f'Bearer {base64_access}',
            "Content-Type": "application/json"})

        entitlements_token = (r2.json()["entitlements_token"])



        valorant_server = "eu"
        print(valorant_server)

        r = requests.get("https://auth.riotgames.com/userinfo", headers={
            "Authorization": f'Bearer {base64_access}',
            "Content-Type": "application/json"})

        uuid = (r.json()["sub"])

        while True:
            if exit_vakti:
                break
            r = requests.get(f"https://glz-{valorant_server}-1.{valorant_server}.a.pvp.net/pregame/v1/players/{uuid}",
                             headers={
                                 "X-Riot-Entitlements-JWT": entitlements_token,
                                 "Authorization": f"Bearer {base64_access}"
                             })
            if (r.status_code) == 404:
                print("seçim ekranı bekleniyor")
            if (r.status_code) != 404:
                break
        if exit_vakti:
            break

        matchid = (r.json()["MatchID"])

        config = configparser.ConfigParser()
        config.sections()

        config.read('config.ini')

        ajanadı = config['ajan-secimi']['ajan']



        ajanlar = {"jett":"add6443a-41bd-e414-f6ad-e58d267f4e95",
                   "raze":"f94c3b30-42be-e959-889c-5aa313dba261",
                   "neon":"bb2a4828-46eb-8cd1-e765-15848195d751",
                   "reyna":"a3bfb853-43b2-7238-a4f1-ad90e9e46bcc",
                   "phoenix":"eb93336a-449b-9c1b-0a54-a891f7921d69",
                   "yoru":"7f94d92c-4234-0a36-9646-3a87eb8b5c89"}

        ajanid = ajanlar[ajanadı]

        for a in range(5):
            r = requests.post(
                f"https://glz-{valorant_server}-1.{valorant_server}.a.pvp.net/pregame/v1/matches/{matchid}/lock/{ajanid}",
                headers={
                    "X-Riot-Entitlements-JWT": entitlements_token,
                    "Authorization": f"Bearer {base64_access}"
                })

            print(r.text)
            if exit_vakti:
                break

        if exit_vakti:
            break


def instalock():

    startstop = dpg.get_value("start-stop")
    print(startstop)

    global exit_vakti
    exit_vakti = False
    if startstop == True:
        global t
        t = threading.Thread(target=run_instalock)
        t.start()
    else:
        print("-"*50)
        exit_vakti = True
        t.join()










def run_chatspammer():
    while True:
        try:
            if exit_vakti_chat:
                break
            lockfile = "".join(
                [os.getenv("LOCALAPPDATA"), r"\Riot Games\Riot Client\Config\lockfile"]
            )
            with open(lockfile, "r") as f:
                data = f.read().split(":")

            base_url = f"{data[4]}://127.0.0.1:{data[2]}"
            s = requests.Session()
            s.auth = ("riot", data[3])
            break
        except Exception as E:
            print(E)

    r = s.get(base_url + "/entitlements/v1/token", verify=ssl.CERT_NONE)

    print(r.text)
    base64_access = (r.json()["accessToken"])

    r2 = requests.post("https://entitlements.auth.riotgames.com/api/token/v1", headers={
        "Authorization": f'Bearer {base64_access}',
        "Content-Type": "application/json"})

    entitlements_token = (r2.json()["entitlements_token"])

    r = s.get(base_url + "/product-session/v1/external-sessions", verify=ssl.CERT_NONE)

    for test in r.json():
        pass

    liste = ["na", "latam", "br", "eu", "ap", "kr"]

    """for a in (r.json()[test]["launchConfiguration"]["arguments"]):
        if exit_vakti_chat:
            break

        if "ares-deployment=" in a:
            break"""

    #valorant_server = str(a).replace("-ares-deployment=", "")
    valorant_server = "eu"
    print(valorant_server)

    r = requests.get("https://auth.riotgames.com/userinfo", headers={
        "Authorization": f'Bearer {base64_access}',
        "Content-Type": "application/json"})

    uuid = (r.json()["sub"])

    while True:
        if exit_vakti_chat:
            break

        while True:
            if exit_vakti_chat:
                break
            r = requests.get(f"https://glz-{valorant_server}-1.{valorant_server}.a.pvp.net/core-game/v1/players/{uuid}",
                             headers={
                                 "X-Riot-Entitlements-JWT": entitlements_token,
                                 "Authorization": f"Bearer {base64_access}"
                             })
            print(r.text)

            if (r.status_code) == 404:
                print("maç ekranı bekleniyor")
                if exit_vakti_chat:
                    break
            if (r.status_code) != 404:
                matchid = (r.json()["MatchID"])
                break

        print(matchid)

        while True:
            try:
                r = s.get(base_url + f"/chat/v6/conversations/ares-coregame", verify=ssl.CERT_NONE, headers={
                    "Authorization": f'Bearer {base64_access}'})
                time.sleep(0.4)
                print(r.json())
                cid = (r.json()["conversations"][0]["cid"])
                cid = cid.replace("blue", "all").replace("red", "all")
                print(cid)
            except Exception as E:
                print(E)

                print("alo")


            if exit_vakti_chat:
                break

            for line in open("spam.txt","r"):
                print(line.strip())
                if exit_vakti_chat:
                    print("Break atılıyor.")
                    break

                r = s.post(base_url + "/chat/v6/messages/", verify=ssl.CERT_NONE, headers={
                    "Authorization": f'Bearer {base64_access}',
                    "Content-Type": "application/json"}, json={
                    "cid": cid,
                    "message": str(line),
                    "type": "groupchat"
                })
                print(r.text)
                if "RPC_ERROR" in r.text:
                    print("Break atıldı")
                    break









def chatspammer():
    startstop = dpg.get_value("start-stop-chat")
    print(startstop)

    global exit_vakti_chat
    exit_vakti_chat = False
    if startstop == True:
        global t
        t = threading.Thread(target=run_chatspammer)
        t.start()
    else:
        print("-" * 50)
        exit_vakti_chat = True
        t.join()














with dpg.window(tag='w_main',no_close=True,no_scrollbar=True,no_resize=True,no_move=True,no_collapse=True,no_title_bar=True, width=540, height=780):
    with dpg.collapsing_header(label="Instalock", tag='instalock_header'):
        dpg.add_checkbox(label="Active", callback=instalock, tag="start-stop")
        dpg.add_image_button(jett, width=100, height=100,callback=ajan, tag="jett")

        dpg.add_image_button(yoru, width=100, height=100,pos=(120,54),callback=ajan, tag="yoru")

        dpg.add_image_button(reyna, width=100, height=100,pos=(232,54),callback=ajan, tag="reyna")

        dpg.add_image_button(phoenix, width=100, height=100, pos=(344, 54), callback=ajan, tag="phoenix")

        dpg.add_image_button(neon, width=100, height=100, callback=ajan, tag="neon")

        dpg.add_image_button(raze, width=100, height=100, callback=ajan, pos=(120, 164), tag="raze")
    with dpg.collapsing_header(label="Chat Spammer", tag='chatspam_header'):
        dpg.add_checkbox(label="Active", callback=chatspammer, tag="start-stop-chat")
        dpg.add_text("Random EZ messages (BETA)")









dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
