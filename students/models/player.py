from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class BadmintonPlayer(models.Model):
    _name = 'badminton.player'
    _description = 'Badminton Player'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    country = fields.Char(string='Country')
    ranking = fields.Integer(string='Ranking')
    matches_played = fields.Integer(string='Matches Played')
    matches_won = fields.Integer(string='Matches Won')
    matches_lost = fields.Integer(string='Matches Lost')