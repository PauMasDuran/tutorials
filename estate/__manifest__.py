

{
    'name': "Estate",
    'summary': "tutorial module",
    'category': "Tutorials",
    'depends': [
        'base_setup'
    ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menu.xml',
        'views/estate_list_view.xml',
        'views/estate_form_view.xml',
        'views/estate_search_view.xml'
    ]
}