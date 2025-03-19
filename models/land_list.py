from odoo import fields, models
class LandListData(models.Model):
    _name = 'land.list.data'
    _description = 'Land List Data'

    property_id = fields.Many2one(
        'property.list.data',
        string = 'Property Name',
        required = True
    )
    name = fields.Char('Land Identification Name', required=True)
    certifying_company = fields.Selection([
        ('csi', 'CSI'),
        ('psc', 'PSC'),
        ('ppc', 'PPC'),
        ('phi', 'PHI'),
    ],'Certifying Company')
    land_type = fields.Many2one(
        'land.master.data.line',
        string = 'Land Type',
        domain = "[('master_id.name', '=', 'Land Types')]"
    )
    land_transaction_type = fields.Many2one('land.master.data.line',
        string = 'Land Transaction Type',
        domain = "[('master_id.name', '=', 'Land Transaction Types')]"
    )
    nature_of_deed = fields.Char('Nature of Deed')
    area_unit_of_measurement = fields.Selection([
        ('squaremeter', 'Square Meter'),
        ('squarefoot', 'Square Foot'),
        ('squareyard', 'Square Yard')
    ],'Area Unit of Measurement')

    # property_id = fields.Many2one('property.list.data', string='Property')

