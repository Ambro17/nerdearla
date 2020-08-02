from .entities import ( 
    Sponsor,
    SponsorType,
    Company,
    OpenPosition,
)
from typing import List


EVIL_CORP = Company(
    name='Evil Inc.',
    description='Lorem',
    website='www.evil.inc',
    open_positions=[
        OpenPosition(title='Sr Python Dev', url='www.carrers.com', company='Evil'),
        OpenPosition(title='Jr Python Dev', url='www.carrers.com', company='Evil'),
    ],
    technologies=['Python', 'React', 'GraphQL'],
)

NICE_CORP = Company(
    name='Good Inc.',
    description='Desc',
    website='www.good.inc',
    open_positions=[
        OpenPosition(title='QA Engineer', url='www.carrers.com', company='Good Inc'),
        OpenPosition(title='SDET', url='www.carrers.com', company='Good Inc'),
    ],
    technologies=['Pytest', 'Selenium'],
)

COMPANIES = [EVIL_CORP, NICE_CORP]


def get_sponsors() -> List[Sponsor]:
    return [
        Sponsor(
           company=EVIL_CORP,
           category=SponsorType.EXABYTE,
        )
    ]


def get_open_opportunities() -> List[OpenPosition]:
    return [
        open_position 
        for company in COMPANIES
        for open_position in company.open_positions
    ]