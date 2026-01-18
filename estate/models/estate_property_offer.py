from odoo import fields, models, api # type: ignore

class estatePropertyOffer (models.Model):
    _name = "estate.property.offer"
    _description = "Tags about the properties"

    price = fields.Float()
    status = fields.Selection(copy = False, selection= [("accepted","Accepted"),("refused","Refused")])
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline", store=True)

    @api.depends("create_date","validity")
    def _compute_date_deadline(self):
        
        for record in self:
            base_date = (
                record.create_date.date()
                if record.create_date
                else fields.Date.context_today(record)
            )
            record.date_deadline = fields.Date.add(
                base_date,
                days=record.validity
            )

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                base_date = (
                    record.create_date.date()
                    if record.create_date
                    else fields.Date.context_today(record)
                )
                record.validity = (record.date_deadline - base_date).days
            else:
                record.validity = 7