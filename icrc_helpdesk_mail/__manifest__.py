{
    'name': 'ICRC - Helpdesk mail channel and helpdesk team integration',
    'version': '16.0.1.0.0',
    'summary': 'ICRC ',
    'description': '',
    'category': 'Helpdesk',
    'author': 'DAJ MI 5',
    'depends': [
        'helpdesk_mgmt', 'mail'
    ],
    'data': [
        "views/icrc_mail_views.xml",
        "views/helpdesk_team_view.xml"
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}