# django-bitpay
A class to use the [BitPay Payment Gateway API](https://bitpay.com/bitcoin-payment-gateway-api) in a django project.

Read the [BitPay API documentation (PDF)](https://bitpay.com/downloads/bitpayApi.pdf).

New Invoices with new Bitcoin addresses are created each time the `CreateInvoice` method is called. BitPay links these addresses with your BitPay account and payments are stored in your BitPay balance. You can set up BitPay to pay out to your bank account daily, or split your incoming payments into Bitcoins and your desired currency ([more info](https://bitpay.com/accounting)).

###Note

I only used two optional fields, `redirectURL` and `itemDesc` in the code. There are lots more available in the [BitPay API docs (PDF)](https://bitpay.com/downloads/bitpayApi.pdf).


## Install
- Add the bitpay.py file to your project (anywhere you want)
- Apply for a new API key from [https://bitpay.com/api-keys](https://bitpay.com/api-keys) 
 - Add `BITPAY_API_KEY = 'yourkey'` to settings.py

## Usage

```
from bitpay import BitPay

bp = BitPay()
response = bp.CreateInvoice(total, currency, return_url, description)
```
You can then use `response['url']` to redirect the user to the invoice page, or alternatively show an [Embedded Invoice](https://bitpay.com/embedded-bitcoin-invoice) on your page.

## Todo

- Write a view that handles IPNs from BitPay