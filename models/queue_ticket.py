from odoo import models, fields, api

class QueueTicket(models.Model):
    _name = 'queue.ticket'
    _description = 'Queue Management Ticket'

    name = fields.Char("Name", required=True)
    client_id = fields.Many2one('res.partner', required=True, domain=[('is_company','=', False)])
    service_id = fields.Many2one('queue.service', require=True)
    ticket_number = fields.Char('Number') # automatic sequence
    state = fields.Selection([
        ('draft', 'Draft'),('waiting', 'Waiting'),
        ('called', 'Called'),('done', 'Done'),
        ('cancelled', 'Cancelled')
    ],default='draft')
    scheduling_time = fields.Date('Date')
    qrcode = fields.Char('Qrcode')


    @api.onchange('service_id')
    def _onchange_service(self):
        self.name = self.service_id.name