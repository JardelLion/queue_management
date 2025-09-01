{
    'name': "Queue Management",
    'summary': "Gestão de Filas para Bancos, Agências e Atendimentos",
    'description': """
        Permite agendamento online e emissão de tickets para reduzir o tempo de espera.
    """,
    'author': "Jardel Elias Bernardo",
    'website': "https://github.com/JardelLion",
    'category': 'Services/Queue',
    'version': '1.0',
    'odoo_version': '18.0',
    'depends': ['base','contacts', 'website'],
    'data': [
        'security/ir_rules.xml',
        'security/ir.model.access.csv',
        'views/res_company_views.xml',
        'views/queue_service_views.xml',
        'views/queue_ticket_views.xml',
        'views/menus.xml',
        'views/resgister_company_template.xml'
    ],
    'assets': {
        'web.assets_backend': [
            # css/js aqui
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
