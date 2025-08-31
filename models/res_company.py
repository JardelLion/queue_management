from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    queue_service_ids = fields.One2many("queue.service", 'company_id')
