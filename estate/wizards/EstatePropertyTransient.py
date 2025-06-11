from odoo import models, fields

class EstatePropertyTransient(models.TransientModel):
    _name = "estate.property.transient"
    _description = "This is Estate Property Transient"

    name = fields.Char(string="Name", required=True)
    expected_price = fields.Float(string="Expected price", required=True)

    def action_create_estate_property(self):
        self.env['estate.property'].create({
            'name': self.name,
            'expected_price': self.expected_price
        })
