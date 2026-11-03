import requests
import datetime
import base64
from Mpesa import settings

class STKPUSH:

    access_url=settings.MPESA_ACCESS_URL
    consumer_key=settings.CONSUMER_KEY
    consumer_secret=settings.CONSUMER_SECRET
    stkpush_url=settings.MPESA_STK_PUSH_URL
    shortcode=settings.SHORTCODE
    passkey=settings.DARAJA_PASSKEY
    callback_url=settings.DARAJA_CALLBACK_URL
    

    def __init__(self, phone, amount, product_name):
        self.phone = str(phone).strip()
        #print(self.phone)
        if len(self.phone) != 12:
            raise ValueError("Phone must be in formart +254********")
        self.amount=int(amount)
        #print(self.amount)
        if self.amount < 1:
            raise ValueError("Amount must be greater than 0")
        self.account_ref = product_name
        print(self.account_ref)
        if not self.account_ref:
            raise ValueError("You Must Have a Product to Buy")

    def get_access_token(self):

        response=requests.get(self.access_url, params={"grant_type": "client_credentials"}, auth=(self.consumer_key, self.consumer_secret),timeout=300, allow_redirects=False)

        #print(response)
        data=response.json()
        access_token = data.get("access_token")
        
        #print(access_token)
        if not access_token:
            raise ValueError(f"Missing access_token in {data}")
        return data["access_token"]
    
    

    def stkpush(self):
        access_token=self.get_access_token()
        print("Step 1: Access Token Retrieved")

        timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        password_string=(self.shortcode + self.passkey + timestamp)
        #print(f"Password String: {password_string}")
        password=base64.b64encode(password_string.encode()).decode()
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        payload={
            "BusinessShortCode": self.shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": self.amount,
            "PartyA": self.phone,
            "PartyB": self.shortcode,
            "PhoneNumber": self.phone,
            "CallBackURL": settings.DARAJA_CALLBACK_URL,
            "AccountReference": self.account_ref[:11],# Limit the account reference to 11 chars
            "TransactionDesc": "Hotel Payment"
        }
        response=requests.post(self.stkpush_url, json=payload, headers=headers)
        print(f"Step 2: STK Push Response: {response.status_code} - {response.text}")
        response.raise_for_status()
        return response.json()


        
            


        