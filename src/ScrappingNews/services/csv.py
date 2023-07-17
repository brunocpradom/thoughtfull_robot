from __future__ import annotations

from dataclasses import asdict
from typing import List

from loguru import logger as loguru_logger
from RPA.Excel.Files import Files

from src.ScrappingNews.models import Article

class CsvParser:
    def __init__(self, logger:loguru_logger):
        self.logger = logger
        self.lib = Files()

    def save_to_excel(self, data: List[Article]):
        self.logger.info("Generating excel file")
        self.lib.create_workbook(path = "./output/output.xlsx")
        self.lib.create_worksheet("Articles", content=[asdict(a) for a in data], header=True)
        self.lib.save_workbook()
        self.logger.success("Done")
