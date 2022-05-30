from webserver import keep_alive
import requests

channelID = 976397425734467624

headers = {
    "authorization":
    "980747240740094042":"OTgwNzQ3MjQwNzQwMDk0MDQy.Gw9obf.A2SVy5yT6sNXoPMH1GmMX7RsBkTPu1FGDAyXRU
"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
