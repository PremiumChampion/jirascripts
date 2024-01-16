
import sys
import bs4
sys.modules["beautifulsoup4"] = bs4 # fix for confluence api

from atlassian import Confluence
from pathlib import Path
from time import sleep
from os.path import exists
import pathvalidate


confluence = Confluence(url='https://confluence-student.it.hs-heilbronn.de',
                        username='',
                        password=''
                        )

# get the filename by going to your homepage and opening the page information in the "..." menu
confluence_home_page_id = 1234

export_root_folder = "export"


def export_page(page_id: int, path: str):
    page = confluence.get_page_by_id(page_id, expand="metadata.children.descendants.ancestors.container.body")
    page_name = pathvalidate.sanitize_filename(page["title"])
    page_root_path = f"{path}\\{page_name}"
    print(f"exporting page {page_id} named {page_name}")
    Path(page_root_path).mkdir(parents=True, exist_ok=True)
    pdf_path = f"{page_root_path}\\{page_name}.pdf"
    pdf_file_existed_from_the_start = exists(pdf_path)
    if not pdf_file_existed_from_the_start:
        with open(pdf_path, "wb") as pdf_file:
            pdf_file.write(confluence.get_page_as_pdf(page_id))

    Path(f"{page_root_path}\\assets").mkdir(parents=True, exist_ok=True)
    if not pdf_file_existed_from_the_start:
        confluence.download_attachments_from_page(page_id, path=f"{page_root_path}\\assets")

    for child_page in confluence.get_child_pages(page["id"]):
        export_page(child_page["id"], page_root_path)

    if not pdf_file_existed_from_the_start:
        sleep(10) # escape rate limiting


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    export_page(confluence_home_page_id, f".\\{export_root_folder}")
