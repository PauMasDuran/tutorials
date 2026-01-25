from odoo import fields, models, api # type: ignore
from odoo.exceptions import UserError

class estatePropertyOffer (models.Model):
    _name = "estate.property.offer"
    _description = "Tags about the properties"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(copy = False, selection= [("accepted","Accepted"),("refused","Refused")])
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property',required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline", store=True)
    property_type_id = fields.Many2one("estate.property.type",related="property_id.property_type_id",store=True)

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
    
    # Button Methods

    def confirm_status(self):
        self.ensure_one()
        
        for record in self:
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id

        other_offers = self.property_id.offer_ids - self
        other_offers.write({'status': 'refused'})


    def refused_status(self):
        for record in self:
            record.status = "refused"

    #sql constrains 
    
    _positive_price = models.Constraint(
        'CHECK(price >= 0)',
        'The price offer of a property can not be negative') 

    #inheritance

    @api.model
    def create(self, vals):

        offer = super().create(vals)

        if offer.property_id and offer.price >= offer.property_id.get_expected_price() * 0.9:
            offer.property_id.offer_created()
        else:
            raise UserError("The price is not within 90 percent the expected price.")

        return offer

    """@api.model
    def create(self, vals_list):
        # vals_list is always a list of dictionaries
        for vals in vals_list:
            property_id = vals.get('property_id')
            if property_id:
                property = self.env['estate.property'].browse(property_id)
                if 'price' in vals and vals['price'] < property.get_expected_price() * 0.9:
                    raise UserError("The price is not within 90 percent of the expected price.")

        offers = super().create(vals_list)

        # Update properties after creation
        for offer in offers:
            if offer.property_id:
                offer.property_id.offer_created()

        return offers"""

    