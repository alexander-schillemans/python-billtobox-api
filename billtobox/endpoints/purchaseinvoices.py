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