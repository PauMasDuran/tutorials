from odoo import fields, models # type: ignore

class estatePropertyType (models.Model):
    _name = "estate.property.type"
    _description = "Adtitonal info about the properties"

    name = fields.Char(required=True)

    _unique_type_name = models.Constraint(
        'UNIQUE(name)',
        'No duplicated types allowed'
    )
