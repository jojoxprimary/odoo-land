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
    