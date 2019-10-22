import json
from datetime import datetime


def python_to_json():
    """将python类型转化成json类型"""

    d = {
        'name': 'python书籍',      # str
        'sale_price': 64.4,       # float
        'origin_price': 55,       # int
        'pub_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # datetime 
        'store': ['京东', '淘宝'],  # list
        'author': ('张三', '李四', 'Jone'),  # tuple
        'is_valid': True,  # true
        'is_sale': False,  # false
        'meta': {                      # dict
            'isbn': 'abc-124',
            'pages': 300
        },
        'desc': None           # none
    }

    rest = json.dumps(d, indent=2)
    print(rest)

def json_to_python():
    """将json转换成python"""

    data = '''
        {
            "name": "python书籍",
            "origin_price": 66,
            "pub_date": "2019-10-21 19:22:00",
            "store": ["京东", "淘宝"],
            "author": ["张三", "李四", "jone"],
            "is_valid": true,
            "is_sale": false,
            "meta": {
                "isbn": "abc-343",
                "pages": 300
            },
            "desc": null
        }
    '''

    rest = json.loads(data)
    print(rest)

def json_to_python_form_file():
    """ 从文件中读取json内容，并将其转换成python对象 """

    f = open('./static/book.json', 'r')
    s = f.read()
    print(s)
    rest = json.loads(s)
    print(rest)
    f.close()

if __name__ == "__main__":
    # python_to_json()
    # json_to_python()
    json_to_python_form_file()
