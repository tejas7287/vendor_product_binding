{
    'name': 'Vendor Product Binding',
    'version': '19.0.1.0.0',
    'summary': 'Bind products to vendors on Purchase Orders',
    'category': 'Purchase',
    'depends': ['purchase'],
    'data': [
        'views/purchase_order_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}