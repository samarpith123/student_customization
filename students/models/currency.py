from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class Currency(models.Model):
    _name = 'student.currency'
    _description = 'Currency'
    _rec_name = 'name'

    name = fields.Char(string='Currency Name',required=True)
    currency_unit_label = fields.Char(string='Currency Unit Label')
    currency_subunit_label = fields.Char(string='Currency Subunit Label')
    symbol = fields.Char(string='Currency Symbol', required=True)
    rounding = fields.Float(string='Rounding Factor', required=True, default=0.01)
    active = fields.Boolean(string='Active', default=True, help="If the currency is active and can be used in transactions")
    rate = fields.Float(string='Exchange Rate', digits=(12, 6))
    fired = fields.Text() 
    drest = fields.Text()   
    read_t = fields.Text()
   