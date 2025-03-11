from odoo import models, fields

class CountryCity(models.Model):
    _name = 'res.country.city'
    _description = 'City'
    _rec_name = 'name'  # This will display the city name in the dropdown

    name = fields.Char("City Name", required=True)
    state_id = fields.Many2one('res.country.state', string="State", required=True)

