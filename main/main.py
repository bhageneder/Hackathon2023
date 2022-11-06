#main script
import API_Suite.productSearchAPI as search
from SQLite_Suite import DBConnect, DBInsert, DBRetrieve


key = 'null'

if __name__ == "__main__":
    #result = search.productSearch("1122","womens shoes","0","1")
    data = DBRetrieve.get_all_data_from_table('products')
    for row in data:
        print(row)