from odoo import fields, models # type: ignore

class estatePropertyType (models.Model):
    _name = "estate.property.type"
    _description = "Adtitonal info about the properties"
    _order = "sequence, name"

    name = fields.Char(required=True)
    property_id = fields.One2many("estate.property","property_type_id",string="Property Types")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    _unique_type_name = models.Constraint(
        'UNIQUE(name)',
        'No duplicated types allowed'
    )
