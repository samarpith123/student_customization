from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class PlayerRegistration(models.Model):
    _name = 'students.player'
    _description = 'Player Registration'

    name = fields.Char (string = 'First Name', required = True) 
    last_name = fields.Char (string = 'Last Name', required = True)
    email= fields.Char (string = 'Email Address',required = True)
    permanent_address = fields.Char (string = 'Permanent Address')
    date_of_birth = fields.Date (string = 'Date Of Birth')
    city = fields.Char (string = 'City')
    permanent_address = fields.Char (string = 'Permanent Address',required = True)
    date_of_birth = fields.Date (string = 'Date Of Birth',required = True)
    city = fields.Char (string = 'City',required = True)
    user_id = fields.Many2one('res.users')
    state = fields.Selection([
    ('select', 'Select'),
    ('andhra_pradesh', 'Andhra Pradesh'),
    ('arunachal_pradesh', 'Arunachal Pradesh'),
    ('assam', 'Assam'),
    ('bihar', 'Bihar'),
    ('chhattisgarh', 'Chhattisgarh'),
    ('goa', 'Goa'),
    ('gujarat', 'Gujarat'),
    ('haryana', 'Haryana'),
    ('himachal_pradesh', 'Himachal Pradesh'),
    ('jharkhand', 'Jharkhand'),
    ('jk', 'Jammu and Kashmir'),
    ('karnataka', 'Karnataka'),
    ('kerala', 'Kerala'),
    ('madhya_pradesh', 'Madhya Pradesh'),
    ('maharastra', 'Maharastra'),
    ('maharashtra', 'Maharashtra'),
    ('manipur', 'Manipur'),
    ('meghalaya', 'Meghalaya'),
    ('mizoram', 'Mizoram'),
    ('nagaland', 'Nagaland'),
    ('odisha', 'Odisha'),
    ('punjab', 'Punjab'),
    ('rajasthan', 'Rajasthan'),
    ('sikkim', 'Sikkim'),
    ('tamil_nadu', 'Tamil Nadu'),
    ('telangana', 'Telangana'),
    ('tripura', 'Tripura'),
    ('uttar_pradesh', 'Uttar Pradesh'),
    ('uttarakhand', 'Uttarakhand'),
    ('west_bengal', 'West Bengal')], required=True, default='select')

    mother_name = fields.Char (string = 'Mother Name', required = True)
    father_name = fields.Char (string = 'Father Name', required = True)
    gender = fields.Selection ([('select','Select'),('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],string = 'Gender', required = True, default='select')
    contact = fields.Char (string = 'Student Contact No', required = True)
    parent_contact = fields.Char (string = 'Parent Contact No', required = True)
   
    year = fields.Char (string='Year Of Study', required = True)
    semester = fields.Char (string='Semester', required = True)
    states = fields.Selection([('drafted','Drafted'),('confirmed','Confirmed'),('rejected','Rejected')],string='Status',default='drafted')
    space = fields.Char('',readonly=True)
