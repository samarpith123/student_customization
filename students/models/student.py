from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class StudentDetail(models.Model):
    _name = 'student.student'
    _description = 'Student Description'

    name  = fields.Char(string='Student Name',required=True)
    age = fields.Integer(string='Age')
    class_name = fields.Char(string='Class Name')
    user_id = fields.Many2one('res.users')
        
