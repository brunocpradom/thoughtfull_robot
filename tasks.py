from __future__ import annotations

import time
from dataclasses import asdict

from loguru import logger

from src.ScrappingNews.config import get_environment_variables
from src.ScrappingNews.services.csv import CsvParser
from src.ScrappingNews.services.ny_times import NYTimesScrapperService




if __name__ == "__main__":
    config = get_environment_variables()
    logger = logger
    logger.add("logs/logs.log", retention="5 days")

    robot = NYTimesScrapperService(config, logger)
    articles = robot.release_the_spider()
    CsvParser(logger).save_to_excel(articles)
