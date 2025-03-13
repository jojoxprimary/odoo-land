from odoo import fields, models

class PropertyListData(models.Model):
    _name = 'property.list.data'
    _description = 'Property List Data'

    name = fields.Char('Name', required=True)
    code = fields.Char('Property Code')
    certifying_company = fields.Selection([
        ('csi', 'CSI'),
        ('psc', 'PSC'),
        ('ppc', 'PPC'),
        ('phi', 'PHI'),
    ],'Certifying Company')

    land_type = fields.Many2one(
    'land.master.data.line', 
    string='Land Type',
    domain="[('master_id', '=', 6)]" # id of Land Types master
    )

    property_address = fields.Text(string='Property Address')
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one(
    'res.country.state', string="Province",
    domain="[('country_id', '=', country_id)]"  
    )
    city_id = fields.Many2one(
    'res.country.city', string="City/Municipality", 
    domain="[('state_id', '=', state_id)]"
    )
    pin = fields.Char(string='Pin')
    latitude = fields.Char(string='Latitude')
    longitude = fields.Char(string='Longitude')



    