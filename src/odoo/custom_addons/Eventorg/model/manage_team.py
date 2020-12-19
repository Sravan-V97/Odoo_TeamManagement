from odoo import api, fields, models, _
import math

class EmpTeams(models.Model):
    _name = 'emp.team'
    _description = 'team scheduling'
    _rec_name = 'team_name'

    team_id = fields.integer(string='team')
    team_name = fields.char(required=True)
    emp_name = fields.char(required=True)
    emp_dept = fields.char(string='department')
    
    active = fields.Boolean(default=True)