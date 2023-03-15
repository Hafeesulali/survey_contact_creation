{
    'name': 'Survey contact relation',
    'description': 'Contact Creation from Survey',
    'installable': True,
    'version': '16.0.1.0.0',
    'depends': ['base', 'survey'],
    'data': [
        'security/ir.model.access.csv',
        'views/survey_inherit_view.xml'
    ]
}
