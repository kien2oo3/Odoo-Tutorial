from odoo import fields, models

class EstateBase(models.AbstractModel):
    _name = 'estate.property.base'
    _description = 'Base logic for Estate Property'
    _auto = False # Không tạo bảng trong DB
    my_base = fields.Char(string="My base", default="my base")