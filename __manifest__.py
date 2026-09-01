{
    'name': 'Etiquetas de Envío por Bulto',
    'version': '17.0.1.0.0',
    'category': 'Inventory/Delivery',
    'summary': 'Impresión de etiquetas de envío (4 por hoja) para órdenes de entrega',
    'description': """
Etiquetas de Envío por Bulto
=============================
Agrega un botón "Imprimir Etiquetas" en las órdenes de entrega (stock.picking)
que genera un PDF con etiquetas de envío, 4 por página (2x2), incluyendo:

- Fecha
- Localidad
- Dirección
- Referencia (texto libre, ej: "Es un PH")
- Destinatario (RECIBE)
- Teléfono
- Numeración de bulto (BULTO X / N)
- Campo de Notas

La cantidad de bultos y la referencia se configuran directamente en la
orden de entrega antes de imprimir.
""",
    'author': 'Custom',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
        'report/label_report.xml',
        'report/label_templates.xml',
    ],
    'installable': True,
    'application': False,
}
