from dataclasses import dataclass
from enum import Enum

weekday = Enum("weekday", 'MONDAY TUESDAY WEDNESDAY THURSDAY FRIDAY SATURDAY SUNDAY NONE', start=0)

@dataclass
class Gym:
  name: str
  bogo_day: int
  student_day: int
  lady_day: int
  happy_day: int

gyms = []

gyms.append(Gym('RCC',
  weekday.TUESDAY.value,
  weekday.THURSDAY.value,
  weekday.WEDNESDAY.value,
  weekday.NONE.value))

gyms.append(Gym('NJRG',
  weekday.WEDNESDAY.value,
  weekday.MONDAY.value,
  weekday.TUESDAY.value,
  weekday.NONE.value))

gyms.append(Gym('Method',
  weekday.NONE.value,
  weekday.FRIDAY.value,
  weekday.NONE.value,
  weekday.NONE.value))

gyms.append(Gym('Gravity Vault',
  weekday.MONDAY.value,
  weekday.WEDNESDAY.value,
  weekday.NONE.value,
  weekday.FRIDAY.value))
