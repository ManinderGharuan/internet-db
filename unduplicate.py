def unduplicate(session, table, data={}):
    """
    Returns new inserted class object if there is no duplicate,
    otherwise duplicate object

    `session`: db session
    `table`: table class (from model)
    `data`: dictionary of column_name and its value which want to insert
    """
    table_name = table.__tablename__.lower()
    query = session.query(table)
    result = None

    if table_name == 'country':
        result = query.filter(table.code == data['code']).first()

        if not result:
            result = query.filter(table.name == data['code']).first()

    if table_name == 'domain':
        result = query.filter(table.name == data['name']).first()

        if result:
            result.creation_date = data['creation_date']
            result.last_update_date = data['last_update_date']
            result.expiration_date = data['expiration_date']
            result.person = data['person']
            result.registrar = data['registrar']
            result.referral_url = data['referral_url']
            result.whois_server = data['whois_server']
            result.status = data['status']

    else:
        result = query.filter_by(**data).first()

    if not result:
        result = table(**data)
        session.add(result)

    return result
