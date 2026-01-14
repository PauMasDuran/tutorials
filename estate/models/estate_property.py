
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
                                          selection = [("North","north"),("East","east"),("South","south"),("West","west")])
    state = fields.Selection(string="State", copy=False, selection=[("New","new"),("Offer Received","offer Received") , ("Offer Accepted","offer Accepted"), ("Sold","sold") , ("Cancelled","cancelled")], required= True, default="New")
    active = fields.Boolean(string="Active", default=True)