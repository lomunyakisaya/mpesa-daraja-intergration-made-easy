payment = {
    "MerchantRequestID": "29115-34620561-1",
    "CheckoutRequestID": "ws_CO_191220191020363925",
    "ResponseCode": "0",
    "ResponseDescription": "Request accepted",
    "CustomerMessage": "Enter your M-Pesa PIN",
    "amount": 1500,
    "phone": "254712345678",
    "status": "SUCCESS",
    "metadata": {
        "MpesaReceiptNumber": "QHT3AB12CD",
        "TransactionDate": 20261010123045,
        "PhoneNumber": 254712345678
    }
}
payer_phone = payment["phone"]
amount = payment["amount"]
if payment["status"] == "PENDING":
    print(f"About to receive {amount} from {payer_phone}")
if payment["status"] == "SUCCESS":
    print(f"Payment {payment['metadata']['MpesaReceiptNumber']} of {amount} from {payer_phone} was successful.")
else:
    print(f"Payment status is {payment['status']}, cannot process payment.")


