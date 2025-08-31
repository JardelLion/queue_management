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
    'depends': ['contact', 'website'],
    'data': [
        'security/ir.access.model.csv',
        'views/queue_service_views.xml',
        'views/queue_ticket_views.xml'
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
