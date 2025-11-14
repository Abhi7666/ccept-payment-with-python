

     # Accept Payment with Python

This project allows users to generate UPI payment QR codes using Python.
By entering a UPI ID, the script automatically creates QR codes for **PhonePe**, **Paytm**, and **Google Pay**, making digital payments simple and fast.

---

## 🚀 **Features**

* Takes UPI ID input from the user
* Creates UPI payment URLs for PhonePe, Paytm, and Google Pay
* Generates QR codes using the `qrcode` library
* Saves each QR code as an image (`.png`)
* Opens the generated QR codes for preview


---

## 📦 **Tech Stack**

* **Python**
* **qrcode** library
* **Pillow (PIL)** for image display

---

## 📁 **Project Structure**

```
|-- payment_qr.py
|-- phone_pe_qr.png
|-- pay_tm_qr.png
|-- google_pay_qr.png
|-- README.md
```

---

## 📝 **How It Works**

1. User enters their UPI ID
2. Script creates a UPI payment URL for:

   * PhonePe
   * Paytm
   * Google Pay
3. QR codes are generated from these URLs
4. QR images are saved and displayed on screen

---

## ▶️ **How to Run**

1. Install required libraries:

   ```
   pip install qrcode pillow
   ```
2. Run the script:

   ```
   python payment_qr.py
   ```

---

## 📸 **Output**

* `phone_pe_qr.png`
* `pay_tm_qr.png`
* `google_pay_qr.png`

Each file contains a scannable UPI payment QR code.

---

## 💡 **Use Cases**

* Accept payments digitally
* Small business owners
* Freelancers
* Quick demo for Python beginners


