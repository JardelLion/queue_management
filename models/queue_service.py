from odoo import models, fields

class QueueService(models.Model):
    _name = 'queue.service'
    _description = 'Queue Management Service'

    name = fields.Char('Name')
    average_time = fields.Float('Average Time')
    company_id = fields.Many2one('res.company',string='Company')