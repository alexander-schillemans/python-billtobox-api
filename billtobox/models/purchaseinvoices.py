from .base import ObjectListModel, BaseModel, ListResult

class PurchaseInvoiceList(ListResult):

    def __init__(self):
        super().__init__(listObject=PurchaseInvoice)

class PurchaseInvoice(BaseModel):

    def __init__(self,
        id=None,
        purchase_invoice_uuid=None,
        purchase_invoice_number=None,
        client_creditor_purchase_invoice_number=None,
        client_creditor_number=None,
        creditor_number=None,
        client_number=None,
        amount=None,
        vat_amount=None,
        currency_code=None,
        creditor_currency_code=None,
        purchase_invoice_date=None,
        purchase_invoice_due_date=None,
        platform_id=None,
        invoice_lines=None
    ):

        super().__init__()

        self.id = id
        self.purchase_invoice_uuid = purchase_invoice_uuid
        self.purchase_invoice_number = purchase_invoice_number
        self.client_creditor_purchase_invoice_number = client_creditor_purchase_invoice_number
        self.client_creditor_number = client_creditor_number
        self.creditor_number = creditor_number
        self.client_number = client_number
        self.amount = amount
        self.vat_amount = vat_amount
        self.currency_code = currency_code
        self.creditor_currency_code = creditor_currency_code
        self.purchase_invoice_date = purchase_invoice_date
        self.purchase_invoice_due_date = purchase_invoice_due_date
        self.platform_id = platform_id
        self.invoice_lines = invoice_lines if invoice_lines else InvoiceLineList()

class InvoiceLineList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=InvoiceLine)


class InvoiceLine(BaseModel):

    def __init__(self,
        id=None,
        service_name=None,
        service_description=None,
        service_quantity=None,
        service_price=None,
        service_vat=None
    ):

        super().__init__()

        self.id = id
        self.service_name = service_name
        self.service_description = service_description
        self.service_quantity = service_quantity
        self.service_price = service_price
        self.service_vat = service_vat