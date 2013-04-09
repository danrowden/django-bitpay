# django-bitpay
A class to use the [BitPay Payment Gateway API](https://bitpay.com/bitcoin-payment-gateway-api) in a django project.

[BitPay API documentation (PDF)](https://bitpay.com/downloads/bitpayApi.pdf)


## Usage
- Add the bitpay.py file to your project (anywhere you want).
- Add your BitPay API key to your settings file
	- Apply for a new API key from [https://bitpay.com/api-keys](https://bitpay.com/api-keys) 
	- Add **BITPAY_API_KEY = 'yourkey'** to settings.py
- Install **requests** library: **pip install requests** or **easy_install request**
- Load the BitPay class into your views.py: **from bitpay import BitPay**
- 
