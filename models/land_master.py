from odoo import fields, models
# All master list
class LandMasterData(models.Model):
    _name = 'land.master.data'
    _description = 'Master'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    details_ids = fields.One2many('land.master.data.line', 'master_id', string="Details")

# Each master data lists
class LandMasterDataLine(models.Model):
    _name = 'land.master.data.line'
    _description = 'Master Data Line'

    master_id = fields.Many2one('land.master.data', string="Master Data", ondelete="cascade")
    name = fields.Char('Name')

