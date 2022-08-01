import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-purchase-workflow",
    description="Meta package for oca-purchase-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-procurement_purchase_no_grouping>=15.0dev,<15.1dev',
        'odoo-addon-product_form_purchase_link>=15.0dev,<15.1dev',
        'odoo-addon-purchase_analytic_global>=15.0dev,<15.1dev',
        'odoo-addon-purchase_blanket_order>=15.0dev,<15.1dev',
        'odoo-addon-purchase_default_terms_conditions>=15.0dev,<15.1dev',
        'odoo-addon-purchase_delivery_split_date>=15.0dev,<15.1dev',
        'odoo-addon-purchase_deposit>=15.0dev,<15.1dev',
        'odoo-addon-purchase_discount>=15.0dev,<15.1dev',
        'odoo-addon-purchase_last_price_info>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_line_menu>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_no_zero_price>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_product_recommendation>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_qty_change_no_recompute>=15.0dev,<15.1dev',
        'odoo-addon-purchase_order_type>=15.0dev,<15.1dev',
        'odoo-addon-purchase_partner_selectable_option>=15.0dev,<15.1dev',
        'odoo-addon-purchase_receipt_expectation>=15.0dev,<15.1dev',
        'odoo-addon-purchase_receipt_expectation_manual>=15.0dev,<15.1dev',
        'odoo-addon-purchase_receipt_expectation_manual_split>=15.0dev,<15.1dev',
        'odoo-addon-purchase_reception_notify>=15.0dev,<15.1dev',
        'odoo-addon-purchase_request>=15.0dev,<15.1dev',
        'odoo-addon-purchase_request_tier_validation>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
