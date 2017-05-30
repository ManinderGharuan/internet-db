#!/usr/bin/env python3
import os
from time import sleep
from random import choice
from csv import reader, DictReader
import click
from whois import whois
from scraper import save_internet_data
from models.Domain import Domain
from models.Country import Country
from db import get_session


@click.group()
def cli():
    pass


@cli.command(name="import")
@click.argument('path', type=click.Path(exists=True))
def import_csv(path):
    """Import file and save domains in database"""
    file = os.path.abspath(path)
    session = get_session()

    try:
        with open(file) as csvfile:
            csv_reader = reader(csvfile)

            with click.progressbar(iterable=csv_reader, show_pos=True) as bar:
                for row in bar:
                    domain = session.query(Domain) \
                                    .filter(Domain.name == row[1]).first()

                    if not domain:
                        domain = Domain(name=row[1])
                        session.add(domain)
                        session.commit()
    except OSError as error:
        print("Error in import path: ", error)
    finally:
        session.close()


@cli.command()
def status():
    """Return Scraped domain count and unscraped domain count"""
    session = get_session()
    total_domains = session.query(Domain).count()

    scraped_domains = session.query(Domain).filter(
        Domain.person_id != None,
        Domain.registrar_id != None).count()

    unscraped_domains = session.query(Domain).filter(
        Domain.person_id == None,
        Domain.registrar_id == None).count()

    click.echo("Total Domains are: " +
               click.style('{}'.format(total_domains), fg='yellow'))
    click.echo("Total Scraped Domains: " +
               click.style('{}'.format(scraped_domains), fg='green'))
    click.echo("Not Scraped: " +
               click.style('{}'.format(unscraped_domains), fg='red'))

    session.close()


@cli.command()
def scrap():
    session = get_session()
    domain = None
    domains = session.query(Domain).filter(
        Domain.person_id == None,
        Domain.registrar_id == None).all()

    try:
        with click.progressbar(iterable=domains, show_pos=True) as bar:
                for domain_object in bar:
                    domain = domain_object.name
                    data = whois(domain)

                    save_internet_data(domain, data, session)
                    sleep(choice(range(6, 10)))
    except Exception as error:
        print("Exception in scrap command: ", error, "\nDomain is: ", domain)
    finally:
        session.close()


@cli.command(name="import-country")
@click.argument('path', type=click.Path(exists=True))
def import_country(path):
    """Import file to save countries in database"""
    file = os.path.abspath(path)
    session = get_session()

    try:
        with open(file) as csvfile:
            csv_reader = DictReader(csvfile)

            with click.progressbar(iterable=csv_reader, show_pos=True) as bar:
                for row in bar:
                    country = session.query(Country) \
                                    .filter(Country.name == row['Name'],
                                            Country.code == row['Code']).first()

                    if not country:
                        country = Country(name=row['Name'], code=row['Code'])
                        session.add(country)
                        session.commit()
    except OSError as error:
        print("Error in import path: ", error)
    finally:
        session.close()


if __name__ == '__main__':
    cli()
