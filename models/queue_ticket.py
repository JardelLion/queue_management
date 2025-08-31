from odoo import models, fields

class QueueTicket(models.Model):
    _name = 'queue.ticket'
    _description = 'Queue Management Ticket'

    name = fields.Char("Name")
    client_id = fields.Many2one('res.partner')
    service_id = fields.Many2one('queue.service')
    ticket_number = fields.Char('') # automatic sequence
    state = fields.Selection([
        ('draft', 'Draft'),('waiting', 'Waiting'),
        ('called', 'Called'),('done', 'Done'),
        ('cancelled', 'Cancelled')
    ],default='draft')
    scheduling_time = fields.Date('Date')
    qrcode = fields.Char('Qrcode')



