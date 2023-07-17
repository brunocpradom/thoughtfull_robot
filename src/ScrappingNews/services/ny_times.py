from __future__ import annotations

import os
import time
from dataclasses import asdict
from datetime import datetime
from datetime import timedelta
from typing import List

import requests
from loguru import logger as loguru_logger
from RPA.Browser.Selenium import By
from RPA.Browser.Selenium import Selenium

from src.ScrappingNews.config import Config
from src.ScrappingNews.config import get_environment_variables
from src.ScrappingNews.models import Article
from src.ScrappingNews.models import Section

class NYTimesScrapperService():
    url = "https://www.nytimes.com/"

    def __init__(self, config: Config, logger: loguru_logger):
        self.robot = Selenium()
        self.config : Config = config
        self.logger = logger


    def select_sections(self, section : List[str]) -> None:
        self.logger.info("selecting sections")
        self.robot.click_element_when_visible("//div[@role='form' and @data-testid='section']//button")
        for section in self.config.section:
            self.robot.click_element_if_visible(f"//input[contains(@value,'{Section(section).value}')]")
        self.logger.success("sections selected")

    def select_date_range(self, date_range : int) -> None:
        self.logger.info("selecting date range")
        self.robot.click_element_when_visible("//div[@role='form' and @aria-label='Date Range']//button")
        self.robot.click_element_when_visible("//button[@value='Specific Dates']")

        end_date = (datetime.now() - timedelta(days=self.config.number_of_months*30)).strftime("%m/%d/%Y")
        self.robot.input_text('//*[@id="startDate"]', datetime.now().strftime("%m/%d/%Y"))
        self.robot.input_text('//*[@id="endDate"]', end_date)
        self.robot.press_keys("//input[@id='endDate']", "ENTER")
        self.logger.success("date range selected")

    def sort_by_newest(self):
        self.logger.info("sorting by newest")
        self.robot.click_element_when_visible("//select[@data-testid='SearchForm-sortBy']")
        self.robot.click_element_when_visible("//option[@value='newest']")
        self.logger.success("sorted")

    def get_picture(self, element):
        try:
            img_source = element.find_element(By.CLASS_NAME, "css-rq4mmj").get_attribute("src")
            file_name = os.path.basename(img_source.split("?")[0])
            with open(f"output/imgs/{file_name}", 'wb') as file:
                file.write(requests.get(img_source).content)
            return img_source

        except Exception as error:
            self.logger.error("error getting picture")
            self.logger.error(error)
            return "-"

    def get_articles(self) -> List[Article]:
        self.logger.info("getting articles")
        articles_list = list()
        elements = self.robot.get_webelements("class:css-1l4w6pd")

        for element in elements:
            article = Article(
                title = element.find_element(By.CLASS_NAME, "css-2fgx4k").text,
                description = element.find_element(By.CLASS_NAME, "css-16nhkrn").text,
                date = element.find_element(By.CLASS_NAME, "css-17ubb9w").text,
                picture_filename = self.get_picture(element),
                count_of_search_phrases= 0,
                contains_money= False
            )
            article.set_count_search_phrases(self.config.search_text)
            articles_list.append(article)
        self.logger.success("articles retrieved")
        return articles_list

    def make_search(self, search_text : str) -> None:
        self.logger.info("making search")
        self.robot.click_element_when_visible("//button[@data-test-id='search-button']")
        self.robot.input_text("//input[@data-testid='search-input']", search_text)
        self.robot.click_element_when_visible("//button[@data-test-id='search-submit']")
        self.logger.success("search made")


    def release_the_spider(self) -> List[Article]:
        try:
            self.logger.info(asdict(self.config))
            self.robot.open_available_browser(self.url)
            self.make_search(self.config.search_text)
            self.select_sections(self.config.section)
            self.select_date_range(self.config.number_of_months)
            self.sort_by_newest()
            time.sleep(3)
            articles = self.get_articles()
            self.robot.close_all_browsers()
            return articles

        except Exception as error:
            self.robot.close_all_browsers()
            self.logger.error(error)
            raise error
