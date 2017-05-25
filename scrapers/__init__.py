from whois import whois
from db.db import get_session
from scrapers.top_1mScraper import top_1mScraper
from scrapers import top_1million_sitesScraper
from models.NewCountry import NewCountry
from models.NewState import NewState
from models.NewCity import NewCity
from models.NewCountryStateCity import NewCountryStateCity
from models.NewLocation import NewLocation
from models.NewOrganization import NewOrganization
from models.NewPerson import NewPerson
from models.NewEmail import NewEmail
from models.NewPersonEmails import NewPersonEmails
from models.NewRegistrar import NewRegistrar
from models.NewNameServer import NewNameServer
from models.NewDomain import NewDomain
from models.NewDomainNameServers import NewDomainNameServers

session = get_session()


def run_scraper():
    for data in top_1mScraper():
        print("Saving Data from", data)

        save_internet_data(whois(data))

    for data in top_1million_sitesScraper():
        print("Saving Data from", data)

        save_internet_data(whois(data))


def save_internet_data(data):
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

    ncountry = NewCountry(country_code, country).insert(session)
    nstate = NewState(state).insert(session)
    ncity = NewCity(city).insert(session)

    ncsc = NewCountryStateCity(ncountry, nstate, ncity).insert(session)

    nlocation = NewLocation(address, ncsc, zip_code).insert(session)
    norg = NewOrganization(org).insert(session)
    nperson = NewPerson(person_name, nlocation, norg,
                        person_phone_number).insert(session)

    for email in emails:
        nemail = NewEmail(email).insert(session)

        NewPersonEmails(nperson, nemail).insert(session)

    nregistrar = NewRegistrar(registrar, registrar_phone_number,
                              registrar_url).insert(session)

    ndomains = []
    nservers = []

    if type(domain_names) is not list:
        domain_names = [domain_names]

    for domain in domain_names:
        ndomain = NewDomain(
            domain, creation_date, updated_date,
            expiration_date, nperson, nregistrar,
            referral_url, whois_server, str(status)
        ).insert(session)

        ndomains.append(ndomain)

    for server in name_servers:
        nserver = NewNameServer(server).insert(session)

        nservers.append(nserver)

    for domain in ndomains:
        for server in nservers:
            NewDomainNameServers(domain, server).insert(session)


session.close()
