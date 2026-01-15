
from odoo import fields, models # type: ignore

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "table describing your properties"
    
    
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string= "Available From", copy=False, default=lambda self: fields.Date.add(fields.Date.context_today(self),months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Garden Orientation',
                                          selection = [("north","North"),("east","East"),("south","South"),("west","West")])
    state = fields.Selection(string="State", 
                            copy=False, 
                            selection = [("new","New"),("offer Received","Offer Received") , ("offer Accepted","Offer Accepted"), ("sold","Sold") , ("cancelled","Cancelled")], 
                            required= True, 
                            default="new")
    active = fields.Boolean(string="Active", default=True)