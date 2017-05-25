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


def save_internet_data(data, session):
    country_code = data['country']
    country = None
    state = data['state']
    city = data['city']
    address = data['address']
    zip_code = data['zipcode']
    org = data['org']
    person_name = data['name']
    person_phone_number = None
    emails = data['emails']
    registrar = data['registrar']
    registrar_phone_number = None
    registrar_url = None
    name_servers = data['name_servers']
    domain_names = data['domain_name']
    creation_date = data['creation_date']
    updated_date = data['updated_date']
    expiration_date = data['expiration_date']
    referral_url = data['referral_url']
    whois_server = data['whois_server']
    status = data['status']

    if type(address) is list:
        address = ', '.join(address)

    if type(creation_date) is list:
        creation_date = creation_date[0]

    if type(updated_date) is list:
        updated_date = updated_date[0]

    if type(expiration_date) is list:
        expiration_date = expiration_date[0]

    new_country = Country(code=country_code, name=country)
    session.add(new_country)
    session.commit()

    new_state = State(name=state)
    session.add(new_state)
    session.commit()

    new_city = City(name=city)
    session.add(new_city)
    session.commit()

    new_csc = CountryStateCity(
        country=new_country,
        state=new_state,
        city=new_city)
    session.add(new_csc)
    session.commit()

    new_location = Location(
        address=address,
        country_state_city=new_csc,
        zip_code=zip_code)
    new_org = Organization(name=org)
    session.add(new_location)
    session.commit()
    session.add(new_org)
    session.commit()

    new_person = Person(
        name=person_name,
        location=new_location,
        organization=new_org,
        phone_number=person_phone_number)
    session.add(new_person)
    session.commit()

    for email in emails:
        new_email = Email(email=email)

        pe = PersonEmails(person=new_person, email=new_email)

        session.add(new_email)
        session.commit()
        session.add(pe)
        session.commit()

    new_registrar = Registrar(
        name=registrar,
        phone_number=registrar_phone_number,
        url=registrar_url)

    session.add(new_registrar)
    session.commit()

    new_domains = []
    new_servers = []

    if type(domain_names) is not list:
        domain_names = [domain_names]

    for domain in domain_names:
        new_domain = Domain(
            name=domain,
            creation_date=creation_date,
            last_update_date=updated_date,
            expiration_date=expiration_date,
            person=new_person,
            registrar=new_registrar,
            referral_url=referral_url,
            whois_server=whois_server,
            status=str(status))

        new_domains.append(new_domain)

        session.add(new_domain)
        session.commit()

    for server in name_servers:
        new_server = NameServer(url=server)

        new_servers.append(new_server)

        session.add(new_server)
        session.commit()

    for domain in new_domains:
        for server in new_servers:
            dns = DomainNameServers(
                domain=domain,
                name_server=server)

            session.add(dns)
            session.commit()
