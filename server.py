import os
import logging
import aiohttp
from aiogram import Bot, Dispatcher, executor, types

from categories import Categories
import exceptions
import expenses


API_TOKEN = "5754987037:AAGPua5X3mS5LBklVCREPaLqxlqmWH7GWgY"