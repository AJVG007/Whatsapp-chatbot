import requests

# Configura tus datos
phone_number_id = "309958495536131"
access_token = "EAAU4k10gIZAoBPGJSUkqjJye4KAgZCvhtAh2ewPnywP6ajM3sZAnsKEXdwSIzmhOWqTcSZABaARNZCCeBV987sgsEEZATSWOFBlZAt7fQZC2rUqYtgy1ZADge0D8gxRO4tHVMKitb8jkL7ihi4NbsWqMSThATO1SJ0F3A6eq0ZATjz2lT48A9AcuVPGNhDWkzDEiSZBxr3LMs3ceJl3"
recipient_phone = "5212721310919"

# Construye la solicitud
url = f"https://graph.facebook.com/v19.0/{phone_number_id}/messages"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
payload = {
    "messaging_product": "whatsapp",
    "to": recipient_phone,
    "type": "text",
    "text": {
        "body": "¿Recibes este mensaje desde WhatsApp Cloud API?"
    }
}

# Enviar
response = requests.post(url, headers=headers, json=payload)

# Mostrar resultado
print(f"Status Code: {response.status_code}")
print("Response:")
print(response.json())
