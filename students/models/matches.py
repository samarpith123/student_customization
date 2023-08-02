from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class BadmintonMatch(models.Model):
    _name = 'badminton.match'
    _description = 'Badminton Match'

    player_ids = fields.Many2many('badminton.player', string='Players')
    court_id = fields.Many2one('badminton.court', string='Court')
    date = fields.Date(string='Date')
    winner_id = fields.Many2one('badminton.player', string='Winner', compute='_compute_winner', store=True)



    @api.depends('player_ids', 'player_ids.matches_won')
    def _compute_winner(self):
        if self.player_ids:
            sorted_players = self.player_ids.sorted(key=lambda p: p.matches_won, reverse=True)
            return sorted_players[0]
        return False