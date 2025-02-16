import os
import pytest
from zipfile import ZipFile


CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
PATH_TO_RESOURCES_DIR = os.path.join(CURRENT_DIR, "resources")
PATH_TO_ARCHIVE_DIR = os.path.join(CURRENT_DIR, "archive_folder")


@pytest.fixture(scope='session', autouse=True)
def create_zip_archive():
    if not os.path.exists(PATH_TO_ARCHIVE_DIR):
        os.mkdir(PATH_TO_ARCHIVE_DIR)
    zip_path = os.path.join(PATH_TO_ARCHIVE_DIR, "archived_file.zip")


    with ZipFile(zip_path,'w') as zip_file:
        for file in os.listdir(PATH_TO_RESOURCES_DIR):
            add_file = os.path.join(PATH_TO_RESOURCES_DIR, file)
            zip_file.write(add_file, os.path.basename(add_file))

    yield

    if os.path.exists("resources/archived_file.zip"):
        if os.path.isfile("resources/archived_file.zip"):
            os.remove("resources/archived_file.zip")

