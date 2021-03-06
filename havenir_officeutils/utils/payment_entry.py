import frappe
from frappe.utils import flt, get_datetime, getdate, add_days, date_diff, nowdate, today
from frappe.model.document import Document

def update_customer(self,cdt):
    if self.party_type == 'Customer' and self.payment_type == 'Receive':
        customer = frappe.get_doc('Customer',self.party)
        customer.db_set('last_payment_date',self.posting_date)
        customer.db_set('last_payment_amount',self.paid_amount)
    elif self.party_type == 'Supplier' and self.payment_type == 'Pay':
        customer = frappe.get_doc('Supplier',self.party)
        customer.db_set('last_payment_date',self.posting_date)
        customer.db_set('last_payment_amount',self.paid_amount)    
