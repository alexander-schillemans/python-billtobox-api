from .base import APIEndpoint

from billtobox.models.purchaseinvoices import PurchaseInvoice, PurchaseInvoiceList

class PurchaseInvoiceMethods(APIEndpoint):

    def __init__(self, api):
        super(PurchaseInvoiceMethods, self).__init__(api, 'purchase-invoices')
    
    def list(self, page=0, size=50, sort=None, platform_id=None):
        data = { 'page' : page, 'size' : size }
        if sort: data['sort'] = sort
        if platform_id: data['platform_id'] = platform_id
        
        url = self.endpoint
        status, headers, respJson = self.api.get(url, data)

        if status != 200: return PurchaseInvoice().parseError(respJson)

        return PurchaseInvoiceList().parse(respJson)
    
    def get(self, id):
        url = '{0}/{1}'.format(self.endpoint, id)
        data = None
        status, headers, respJson = self.api.get(url, data)

        if status != 200: return PurchaseInvoice().parseError(respJson)

        return PurchaseInvoice().parse(respJson)

    def getByUUID(self, uuid):
        page = 0
        size = 50
        data = { 'page' : page, 'size' : size }
        invoiceFound = False
        url = self.endpoint

        status, headers, respJson = self.api.get(url, data)
        if status != 200: return PurchaseInvoice().parseError(respJson)

        pList = PurchaseInvoiceList().parse(respJson)
        while(len(pList.items()) > 1):
            for invoice in pList.items():
                print('checking invoice uuid: ', invoice.purchase_invoice_uuid)
                if invoice.purchase_invoice_uuid == uuid: 
                    return invoice
            
            data['page'] += 1
            status, headers, respJson = self.api.get(url, data)

            if status != 200: return PurchaseInvoice().parseError(respJson)

            pList = PurchaseInvoiceList().parse(respJson)
        
        return None

    def delete(self, id):
        url = '{0}/{1}'.format(self.endpoint, id)
        data = None
        status, headers, respJson = self.api.delete(url, data)

        if status != 200: return PurchaseInvoice().parseError(respJson)

        return PurchaseInvoice().parse(respJson)