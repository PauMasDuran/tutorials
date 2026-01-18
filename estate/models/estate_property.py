
from odoo import fields, models, api # type: ignore

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "table describing your properties"
    
    
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string= "Available From", copy=False, default=lambda self: fields.Date.add(fields.Date.context_today(self),months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True, compute="_best_offer")
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


    # foreign keys
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    salesman_id = fields.Many2one('res.users', string="Salesman")
    tag_id = fields.Many2many('estate.property.tag', string="Tags")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")


    #Computed Fields
    total_area = fields.Float(string="Total Area", compute="_compute_total_area")

    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _best_offer(self):
        
        for record in self:
            prices = record.offer_ids.mapped("price")
            record.selling_price = max(prices) if prices else 0

    