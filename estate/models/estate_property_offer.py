from odoo import fields, models # type: ignore

class estatePropertyOffer (models.Model):
    _name = "estate.property.offer"
    _description = "Tags about the properties"

    price = fields.Float()
    status = fields.Selection(copy = False, selection= [("accepted","Accepted"),("refused","Refused")])
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property',required=True)