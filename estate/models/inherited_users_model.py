from odoo import fields, models #type:ignore

class InheritedUsersModel(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property','salesman_id', string="property_ids", domain=[('state', 'not in', ('sold', 'cancelled'))])

