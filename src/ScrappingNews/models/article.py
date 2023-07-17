from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Article:
    title : str
    date : str
    description : str
    picture_filename : str
    count_of_search_phrases : int = 0
    contains_money : bool = False

    def __post_init__(self):
        money_sign = ["$", "R$", "€", "£"]
        if any(money in self.description for money in money_sign) \
            or any(money in self.title for money in money_sign):
            self.contains_money = True

    def set_count_search_phrases(self, search_phrase):
        self.count_of_search_phrases = self.description.count(search_phrase) + self.title.count(search_phrase)
