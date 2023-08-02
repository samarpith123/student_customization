from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class MobilePayment(models.Model):

    _name = 'student.payment'
    _description = 'Mobile Payment'

    payment_date = fields.Date(string='Payment Date')
    customer_id = fields.Many2one('student.student')
    amount = fields.Float()
    currency_id = fields.Many2one('res.currency')
    mobile_desk = fields.Char(string=' Mobile desk')