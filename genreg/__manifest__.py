{
    'name': 'General Register Test',
    'category' : 'General Register',
    'version': '0.1',
    'author': "Martin Pradny",
    "depends": [
        "base",
        "web",
    ],
    'data': [
        'data/genreg_data.xml',
        'security/ir.model.access.csv',
        'security/genreg_security.xml',
        'data/genreg.confidentiality.csv',
        'data/genreg.record.format.csv',
        'data/genreg.record.doctype.csv',
        'views/genreg_record_views.xml',
        'views/genreg_record_format_views.xml',
        'views/genreg_register_views.xml',
        'views/genreg_confidentiality_views.xml',
        'views/genreg_record_doctype_views.xml',
        'views/genreg_register_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'genreg/static/src/js/copy_doc_ref_button.js',
            'genreg/static/src/js/copy_doc_ref_template.xml',
        ],
    },
    "application": True,
    "license": "LGPL-3",
}