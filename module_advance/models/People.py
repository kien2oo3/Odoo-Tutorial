from odoo import fields, models


class People(models.Model):
    _name = "people"
    _description = "This is people module"

    name = fields.Char(string="Name")

    # Binary field
    cv1 = fields.Binary(string="CV1")
    cv2 = fields.Binary(string="CV2", attachment=False)
    cv1_name = fields.Char(string="CV1 name")
    cv2_name = fields.Char(string="CV2 name")

    # HTML field
    description = fields.Html(string="Description")

    # Image field
    avatar = fields.Image(string="Image", max_width=1920, max_height=1920)

    # Selection field
    gender = fields.Selection(string="Gender", selection=[('male', '♂️ Male'), ('female', '♀️ Female')])

    # Date field
    birth_date = fields.Date(string="Birth date")

    # Date time field
    my_datetime = fields.Datetime(string="My datetime")

    def action_date(self):
        pass
