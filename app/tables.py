from flask_table import Table, Col
 
class Results(Table):
    id = Col('Id', show=False)
    title = Col('Title')
    description = Col('Description')
    client = Col('Client')
    client_priority = Col('Clien Priority')
    target_date = Col('Target Date')
    product_area = Col('Product Area')