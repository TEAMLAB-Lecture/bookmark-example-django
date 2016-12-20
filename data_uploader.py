import csv
# from bookmark.models import Bookmark
# bookmark = Bookmark(bookmark_name = row[0], bookmark_url = row[1], bookmark_desc = row[2])


def get_data():
    FILE_NAME = "data/bookmark_list.csv"
    with open(FILE_NAME, 'r') as csvfile:
        data_list = csv.reader(csvfile, delimiter=',', quotechar='"')
        result = list(data_list)

    return result

