from odoo import fields, models, api

class LandMasterData(models.Model):
    _name = 'land.master.data'
    _description = 'Master'

    name = fields.Char('Name', readonly=True)
    description = fields.Char('Description', readonly=True)
    details_ids = fields.One2many('land.master.data.line', 'master_id', string="Details")

    @api.model
    def create(self, vals):
        raise ValueError("Creating new records is not allowed for this model.")

    def write(self, vals):
        # Allow updates only for the 'details_ids' field
        if any(field not in ['details_ids'] for field in vals):
            raise ValueError("Editing records is not allowed for this model.")
        return super(LandMasterData, self).write(vals)

    def unlink(self):
        raise ValueError("Deleting records is not allowed for this model.")

class LandMasterDataLine(models.Model):
    _name = 'land.master.data.line'
    _description = 'Master Data Line'

    master_id = fields.Many2one('land.master.data', string="Master Data", ondelete="cascade")
    name = fields.Char('Name')

