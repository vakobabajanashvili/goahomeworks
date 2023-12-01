import requests

payload = {
    'content' : '.'
}

author = {
    'authorization':'MTA0OTk5NDYxMTkzMTc0MjIzOA.Guxq4x.vuldAVpwREiU-vFo3-WhS_v9an39ZbMLUlEWxQ'
}

for i in range(5):
    payload = {
        'content':'https://images-ext-2.discordapp.net/external/mWwmqXp46OVHUc-AyfxoQKJWjOkRaV9VVYFu_uVJTBs/https/media.tenor.com/XyenxWhdZb0AAAPo/wink-winking.mp4'
    }
    r = requests.post('https://discord.com/api/v9/channels/1146128309047013479/messages', data=payload, headers=author)