from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta


class Mobile(models.Model):

    _name = 'student.mobile'
    _description = 'Student Mobiles'
    

    customer_id = fields.Many2one('student.student',string='Customer')
    brand = fields.Char()
    specifications = fields.Char()
    price = fields.Float()
    start_date = fields.Date()
    end_date = fields.Date()
    image = fields.Binary()