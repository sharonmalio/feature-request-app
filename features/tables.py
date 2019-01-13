from flask_table import Table, Col, LinkCol


class Results(Table):
    id = Col('Id', show=False)
    title = Col('Title')
    description = Col('Description')
    client = Col('Client')
    client_priority = Col('Client Priority')
    target_date = Col('Target Date')
    product_area = Col('Product Area')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
