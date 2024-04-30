from __future__ import annotations
import subprocess

import time
from dataclasses import asdict

from loguru import logger as loguru_logger
from robocorp.tasks import task

from src.ScrappingNews.config import get_environment_variables
from src.ScrappingNews.services.csv import CsvParser
from src.ScrappingNews.services.ny_times import NYTimesScrapperService

def get_last_commit_author_and_branch():
    # Get the author of the last commit
    author = subprocess.check_output(['git', 'log', '-1', '--pretty=%an']).decode().strip()
    
    # Get the name of the current branch
    branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()
    
    return author, branch

@task
def task():
    config = get_environment_variables()
    logger = loguru_logger
    logger.add("logs/logs.log", retention="5 days")
    author, branch = get_last_commit_author_and_branch()
    logger.info(f"Author of last commit: {author}")
    logger.info(f"Branch: {branch}")
    # robot = NYTimesScrapperService(config, logger)
    # articles = robot.release_the_spider()
    # CsvParser(logger).save_to_excel(articles)


if __name__ == "__main__":
    task()
