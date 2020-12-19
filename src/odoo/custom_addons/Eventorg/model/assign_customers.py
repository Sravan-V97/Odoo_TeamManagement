from odoo import api, fields, models, _

class CustTeam(models.Model):
    _name = 'cust.team'
    _description = 'team scheduling'
    _rec_name = 'team_name'

    customer_id = fields.Many2one(string='customer',required=True)
    customer_name = fields.Char(related='customer_id.name')
    team_id = fields.integer(string='team',required=True)
    team_name = fields.Char(required=True)

    active = fields.Boolean(default=True)