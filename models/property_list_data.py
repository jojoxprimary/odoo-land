from odoo import fields, models

class PropertyListData(models.Model):
    _name = 'property.list.data'
    _description = 'Property List Data'

    name = fields.Char('Name')
    code = fields.Char('Property Code')
    certifying_company = fields.Selection([
        ('csi', 'CSI'),
        ('psc', 'PSC'),
        ('ppc', 'PPC')
    ],'Certifying Company')

    area = fields.Char('Area')
    remarks = fields.Char('Remarks')

    # property_address = fields.Text('Property Address')
    # country = fields.Many2one('res.country', 'Country')
    # state = fields.Many2one('res.country.state', 'State')
    # city = fields.Many2one('res.city', 'City')
    # locality = fields.Many2one('res.locality', 'Locality')
    # pin = fields.Char('Pin')
    # latitude = fields.Char('Latitude')
    # longitude = fields.Char('Longitude')


    