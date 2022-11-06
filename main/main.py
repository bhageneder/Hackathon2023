#main script
import API_Suite.productSearchAPI as search
from SQLite_Suite import DBConnect, DBInsert, DBRetrieve


key = '930401d6a5mshe61534d11163938p1ecd97jsn6a9d82d02d3d'

if __name__ == "__main__":
    #result = search.productSearch("1122","womens shoes","0","1")
    data = DBRetrieve.get_all_data_from_table('products')
    for row in data:
        print(row)