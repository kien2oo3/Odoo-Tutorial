from odoo import models, fields
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is Estate Property"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Date availability")
    expected_price = fields.Float(string="Expected price", required=True)
    selling_price = fields.Float(string="Selling price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden area")
    garden_orientation = fields.Selection([("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")], string="Garden orientation")



