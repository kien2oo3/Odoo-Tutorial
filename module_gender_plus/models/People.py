from odoo import fields, models


class People(models.Model):
    _inherit = 'people'

    # Selection field
    gender = fields.Selection(selection_add=[('3d', '👬 3D')], ondelete = {'3d':'cascade'})