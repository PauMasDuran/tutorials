from odoo import fields, models # type: ignore

class estatePropertyTag (models.Model):
    _name = "estate.property.tag"
    _description = "Tags about the properties"
    _order = "name"


    name = fields.Char(required=True)

    _unique_tags_name = models.Constraint(
            'UNIQUE(name)',
            'No duplicated tags allowed'
        )