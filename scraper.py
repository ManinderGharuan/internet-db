from dateutil.parser import parse
from models.Country import Country
from models.State import State
from models.City import City
from models.CountryStateCity import CountryStateCity
from models.Location import Location
from models.Organization import Organization
from models.Person import Person
from models.Email import Email
from models.PersonEmails import PersonEmails
from models.Registrar import Registrar
from models.NameServer import NameServer
from models.Domain import Domain
from models.DomainNameServers import DomainNameServers
from unduplicate import unduplicate


def _parse_datetime(string):
    """
    Returns datetime

    Converts string into python datetime
    """
    try:
        return parse(string, fuzzy=True)
    except ValueError:
        raise Exception("Unknown datetime format : ", string)


def save_internet_data(domain, data, session):
    country_code = data.get('country')
    state_name = data.get('state')
    city_name = data.get('city')
    address = data.get('address')
    zip_code = data.get('zipcode')
    org = data.get('org')
    person_name = data.get('name')
    emails = data.get('emails')
    registrar = data.get('registrar')
    name_servers = data.get('name_servers')
    domain_name = domain
    creation_date = data.get('creation_date')
    updated_date = data.get('updated_date')
    expiration_date = data.get('expiration_date')
    referral_url = data.get('referral_url')
    whois_server = data.get('whois_server')
    status = data.get('status')

    if type(address) is list:
        address = ', '.join(address)

    if type(city_name) is list:
        city_name = str(city_name)

    if type(person_name) is list:
        person_name = str(person_name)

    if type(creation_date) is list:
        creation_date = creation_date[0]

    if type(updated_date) is list:
        updated_date = updated_date[0]

    if type(expiration_date) is list:
        expiration_date = expiration_date[0]

    if type(emails) is not list:
        emails = [emails]

    if type(org) is list:
        org = str(org)

    if type(zip_code) is list:
        zip_code = str(zip_code)

    if type(creation_date) is str:
        creation_date = _parse_datetime(creation_date)

    if type(updated_date) is str:
        updated_date = _parse_datetime(updated_date)

    if type(expiration_date) is str:
        expiration_date = _parse_datetime(expiration_date)

    country = unduplicate(
        session,
        Country,
        {'code': country_code}
    )

    state = unduplicate(
        session,
        State,
        {'name': state_name}
    )

    city = unduplicate(
        session,
        City,
        {'name': city_name}
    )

    csc = unduplicate(
        session,
        CountryStateCity,
        {'country': country,
         'state': state,
         'city': city}
    )

    location = unduplicate(
        session,
        Location,
        {'address': address,
         'country_state_city': csc,
         'zip_code': zip_code}
    )

    org = unduplicate(
        session,
        Organization,
        {'name': org}
    )

    person = unduplicate(
        session,
        Person,
        {'name': person_name,
         'location': location,
         'organization': org}
    )

    for email_address in emails:
        email = unduplicate(
            session,
            Email,
            {'email': email_address}
        )

        unduplicate(
            session,
            PersonEmails,
            {'person': person,
             'email': email}
        )

    rgst = unduplicate(
        session,
        Registrar,
        {'name': registrar}
    )

    servers = []

    if type(name_servers) is not list:
        name_servers = [name_servers]

    domain = unduplicate(
            session,
            Domain,
            {'name': domain_name,
             'creation_date': creation_date,
             'last_update_date': updated_date,
             'expiration_date': expiration_date,
             'person': person,
             'registrar': rgst,
             'referral_url': referral_url,
             'whois_server': whois_server,
             'status': str(status)}
        )

    for server_name in name_servers:
        server = unduplicate(
            session,
            NameServer,
            {'url': server_name}
        )

        servers.append(server)

    for server_object in servers:
        unduplicate(
            session,
            DomainNameServers,
            {'domain': domain,
             'name_server': server_object}
        )

    session.commit()
