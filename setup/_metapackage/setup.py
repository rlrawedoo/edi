import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-edi",
    description="Meta package for oca-edi Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_einvoice_generate>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_facturx>=15.0dev,<15.1dev',
        'odoo-addon-base_edi>=15.0dev,<15.1dev',
        'odoo-addon-base_facturx>=15.0dev,<15.1dev',
        'odoo-addon-edi_account_oca>=15.0dev,<15.1dev',
        'odoo-addon-edi_exchange_template_oca>=15.0dev,<15.1dev',
        'odoo-addon-edi_oca>=15.0dev,<15.1dev',
        'odoo-addon-edi_storage_oca>=15.0dev,<15.1dev',
        'odoo-addon-edi_webservice_oca>=15.0dev,<15.1dev',
        'odoo-addon-webservice>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
