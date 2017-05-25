#!/usr/bin/env python3
import os
from csv import reader
import click
from whois import whois
from scraper import save_internet_data
from models.Domain import Domain
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
        Domain.expiration_date != None,
        Domain.person_id != None,
        Domain.registrar_id != None).count()

    unscraped_domains = session.query(Domain).filter(
        Domain.expiration_date == None,
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
    domains = session.query(Domain).filter(
        Domain.expiration_date == None,
        Domain.person_id == None,
        Domain.registrar_id == None).all()

    for domain in domains:
        data = whois(domain)

        save_internet_data(data, session)

    session.close()


if __name__ == '__main__':
    cli()
