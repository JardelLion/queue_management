from odoo import http
from odoo.http import request

class CompanyRegistration(http.Controller):
    @http.route("/register_company", type='http', auth='public', website=True)
    def register_form(self, **kwargs):
        return request.render('queue_management.register_company_template')


    @http.route("/register_company/submit", type='http', auth='public', method=['POST'], website=True)
    def register_submit(self, **kwargs):
        company = request.env['res.company'].sudo().create({
            'name': kwargs.get('name'),
            'email': kwargs.get("email"),
            'phone': kwargs.get('phone')
        })
        internal_group = request.env.ref('base.group_user')
        user = request.env['res.users'].sudo().create({
            'name': kwargs.get("name"),
            "login": kwargs.get("email"),
            'email': kwargs.get("email"),
            'company_id': company.id,
            'company_ids': [(6, 0, [company.id])],
            'groups_id': [(6, 0, [internal_group.id])]
        })

        return request.render("queue_management.register_success_template", {
            'company': company
        })

