from odoo import models, fields

class Player(models.Model):
    _name = 'player'
    _description = 'Player'

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Image', attachment=True)
    country = fields.Char(string='country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    birth_date = fields.Datetime(string='Date of Birth')
    position = fields.Char(string='Position', groups = "module-1.group_player_manager")
    height = fields.Float(string='Height')
    weight = fields.Float(string="Weight")
