import requests
from bs4 import BeautifulSoup


class DataFetcher(object):
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url', "https://www.iplt20.com/news/113978/vivo-ipl-2018-player-auction-list-announced")

    def get_page_source(self, **kwargs):
        url = kwargs.get('url', self.url)
        response = requests.get(url)
        if response.ok:
            return self.beautify(response.content)

    @staticmethod
    def beautify(page_source):
        soup = BeautifulSoup(page_source, 'html.parser')
        return soup

    def get_data(self):
        source = self.get_page_source()
        div = source.find('div', {'class': 'main-article__body'})
        table = div.find('tbody')

        # table = source.find('table', {'id': 'collapsibleTable1'}).find('tbody')
        # print(table.find('td'))
        # table = source.find('table', {'class': 'ipl-table'}).find('tbody')

        records = table.find_all('tr')
        data = []
        for record in records[1:]:
            table_data = [i.text.strip() for i in record.find_all('td')]
            detail = {
                'set_no': table_data[1],
                'set': table_data[1],
                'set': table_data[1],
            }
            data.append(detail)


if __name__ == "__main__":
    d = DataFetcher(url="https://www.iplt20.com/news/113978/vivo-ipl-2018-player-auction-list-announced")
    # d = DataFetcher(url="https://en.wikipedia.org/wiki/List_of_2018_Indian_Premier_League_personnel_changes")
    # d = DataFetcher(url="https://www.news18.com/ipl-auction-2018/")
    d.get_data()
