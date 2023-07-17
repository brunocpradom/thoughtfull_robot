from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List

from dotenv import load_dotenv
from RPA.Robocorp.WorkItems import WorkItems

load_dotenv()


SEARCH_TEXT=os.environ.get("SEARCH_TEXT")
NUMBER_OF_MONTHS=os.environ.get("NUMBER_OF_MONTHS")
SECTION=os.environ.get("SECTION")
ENV=os.environ.get("ENV")

@dataclass
class Config:
    search_text : str
    number_of_months : int
    section : List[str]

def get_work_item_variable():
    work_itens = WorkItems()
    work_itens.get_input_work_item()

    sections = work_itens.get_work_item_variable("SECTION")
    return Config(
        search_text = work_itens.get_work_item_variable("SEARCH_TEXT"),
        number_of_months = int(work_itens.get_work_item_variable("NUMBER_OF_MONTHS")),
        section = [section.strip() for section in sections.split(",")],
    )


def get_environment_variables():
    if ENV == 'LOCAL':
        return Config(
            search_text = SEARCH_TEXT,
            number_of_months = int(NUMBER_OF_MONTHS),
            section = [section.strip() for section in SECTION.split(",")],
        )
    return get_work_item_variable()
