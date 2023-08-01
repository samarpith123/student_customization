from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class Mobiles(models.Model):

    _name = 'student.mobile'
    _description = 'Student Mobiles'

    name = fields.Char()
    brand = fields.Char(string='Brand')
    price = fields.Float(string='Price')
    specifications = fields.Text(string='Specifications')
    image = fields.Binary(string="Mobile Image")
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='end date')
    
