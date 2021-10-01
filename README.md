# python-mydhl-api
Wrapper for the Bill-To-Box / BanqUP (UnifiedPost) API - v4

## Limitations

This package is limited to PurchaseInvoices at this moment.

## Getting started

### Install

Install with pip

```python
pip install python-billtobox-api
```

### Import

Import the package and the BillToBoxAPI.

```python
from billtobox.api import BillToBoxAPI
```

### Setup connection

Make the connection with your created CLIENTID and CLIENTSECRET.

```python
api = BillToBoxAPI(CLIENTID, CLIENTSECRET)
```


BillToBox authentcation is build on OAuth2. A basic script to obtain your first tokens can be found below.

```python
from billtobox.api import BillToBoxAPI

REDIRECT_URI = 'https://any-url-will-do.com/callback/'

api = BillToBoxAPI(CLIENTID, CLIENTSECRET)

authUrl = api.authHandler.getAuthURL(REDIRECT_URI)
print('visit url: ', authUrl)

response = input('paste response: ')
token = api.authHandler.retrieveToken(response, redirectUri=REDIRECT_URI)
```

When using the script above, any REDIRECT_URI will do. Simply copy and paste the response URI so the handler can obtain the right tokens. 

### UAT/Test mode

You can choose to make use of the UAT/Test environment instead of production by specifying an extra parameter demo and setting it to True.

```python
api = BillToBoxAPI(CLIENTID, CLIENTSECRET, demo=True)
```

Be aware that the UAT environment uses a different CLIENTID and CLIENTSECRET than the production environment.

## PurchaseInvoices

### Available fields

#### PurchaseInvoice

| Field | Remarks
|---------|---------|
| id |
| purchase_invoice_uuid | UUID
| purchase_invoice_number |
| client_creditor_purchase_invoice_number |
| client_creditor_number |
| creditor_number |
| client_number |
| amount |
| vat_amount |
| currency_code |
| creditor_currency_code |
| purchase_invoice_date |
| purchase_invoice_due_date |
| platform_id |
| invoice_lines | Contains an InvoiceLineList object

#### InvoiceLine

| Field |
|---------|
| id |
| service_name |
| service_description |
| service_quantity |
| service_price |
| service_vat |

### List

Get all the purchase invoices. You can limit the size or specify the page. The maximum size is 50, increase the page if you would to see more invoices.
Default page is 0 and default size is 50. Optionally you can specify the field to sort. Default field to sort by is client_id.

Returns a PurchaseInvoiceList object.

```python
purchaseInvoices = api.purchaseInvoices.list(page=0, size=50, sort='client_id')
# Is the same as
purchaseInvoices = api.purchaseInvoices.list()

for invoice in purchaseInvoices.items():
   print(invoice.id)
   print(invoice.amount)
   
   for line in invoice.invoice_lines.items():
      print(line.service_name)
      print(line.service_price)

```

### Get

Get a specific purchase invoice by its ID. Returns a PurchaseInvoice object.

```python
invoice = api.purchaseInvoices.get(ID)
print(invoice.id)
```

### Get by UUID

Get a specific purchase invoice by its UUID (different than the ID). Returns a PurchaseInvoice object.

At this moment there is no built-in function in the API to retrieve an invoice by its UUID.
This function will thus loop over all the invoices and returns the invoice with the requested UUID. This is the reason why the function may run slow if you have a lot of invoices in your account.

```python
invoice = api.purchaseInvoices.getByUUID(UUID)
print(invoice.id)
```

### Delete

Deletes a specific purchase invoice by its ID.

```python
invoice = api.purchaseInvoices.delete(ID)
```




