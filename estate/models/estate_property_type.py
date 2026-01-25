from odoo import fields, models, api # type: ignore

class estatePropertyType (models.Model):
    _name = "estate.property.type"
    _description = "Adtitonal info about the properties"
    _order = "sequence, name"

    name = fields.Char(required=True)
    property_id = fields.One2many("estate.property","property_type_id",string="Property Types")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    offer_ids = fields.One2many("estate.property.offer","property_type_id", string="Offers")
    offer_count = fields.Integer(compute="_count_offers", string=" Offers")

    _unique_type_name = models.Constraint(
        'UNIQUE(name)',
        'No duplicated types allowed'
    )

    @api.depends("offer_ids")
    def _count_offers(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

