#pip install qrcode
#pip install pillow
#taking UPI Id input
upi_id = input("enter your UPI Id = ")
#upi;//pa?=UPI_ID&pn=NAME=amount&CU=CURRENCY&tn=MESSAGE
#DEFINING THE PAYMENT URL BASED ON THE UPI AND THE PAYMENT APP 
#YOU AN MODIFIY THESE URL BASED ON THE PAYMENT APP YOU WANT TO SUPPORT
phonepe_Url = f'upi//pay?ga={Upi_id}&pn=recipient%20NAME&mc=123'
paytm_Url = f'upi//pay?ga={Upi_id}&pn=recipient%20NAME&mc=123'
google_pay_Url = f'upi//pay?ga={Upi_id}&pn=recipient%20NAME&mc=123'
#create QR code code to image file(ptional)
phonepe_qr = qrcode.make(phonepe_Url)
paytm_qr = qrcode.make(paytm_Url)
google_pay_qr = qrcode.make(google_pay_Url)
#save the qr code to image file(optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png") 
#display the qrcode (you may need to install pil/pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()