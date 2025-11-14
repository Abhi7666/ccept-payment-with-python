import qrcode

#taking UPI id as input

upi_id = input("enter your upi id : ")

# defining payment url based on upi id and payment app

phone_pe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
pay_tm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr code for each payment app

phone_pe_qr = qrcode.make(phone_pe_url)
pay_tm_qr = qrcode.make(pay_tm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the qr code to image file

phone_pe_qr.save('phone_pe_qr.png')
pay_tm_qr.save('pay_tm_qr.png')
google_pay_qr.save('google_pay.png')

# display qr code(you need to install pillow library/PIL)

phone_pe_qr.show()
pay_tm_qr.show()
google_pay_qr.show()