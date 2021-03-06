from typing import List, Optional
from enum import Enum
import strawberry


Link = str


@strawberry.interface
class Person:
    name: str
    email: str
    interests: List[str]
    open_to_job_offers: bool

    def interested_in(self, topic):
        interests = [i.lower() for i in self.interests] or []
        return topic.lower() in interests


@strawberry.type
class Speaker(Person):
    job: str
    bio: str = ""
    talk: Optional['Talk'] = None


@strawberry.type
class Visitor(Person):
    resume_link: str = ''
    github_profile: str = ''


@strawberry.enum
class Topic(Enum):
    PYTHON = 'Python'
    REST = 'Rest'
    DIVERSITY = 'Diversity'


@strawberry.type
class Talk:
    name: str
    topic: Topic
    description: str
    year: str
    speaker: Speaker
    video: str


@strawberry.type
class ScheduleInfo:
    when: str
    start: str
    end: str
    starting_in: str


@strawberry.type
class UpcomingTalk:
    name: str
    topic: Topic
    year: str
    description: str
    speaker: Speaker
    schedule: ScheduleInfo


@strawberry.type
class OpenPosition:
    title: str
    url: Link
    company: 'Company'


@strawberry.type
class Company:
    name: str
    tagline: str
    website: Link
    open_positions: List[OpenPosition]
    technologies: List[str]


@strawberry.enum
class SponsorType(Enum):
    DIAMANTE = 'Diamante'
    ORO = 'Oro'
    PLATA = 'Plata'
    BRONCE = 'Bronce'


@strawberry.type
class Sponsor:
    company: Company
    category: SponsorType
