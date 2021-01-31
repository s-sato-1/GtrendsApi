import feedparser


class APIClient(object):
    def __init__(self):
        """
        """
        pass

    def get_gtrends(self) -> {int, str}:
        """
        """
        trendsgoogle = 'https://trends.google.co.jp/trends/trendingsearches/daily/rss?geo=JP'
        query = 'https://www.google.com/search?q=%22{}%22'
        int_ranking = 1
        is_dict_err = False
        prev = ''

        dict_month = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'Aug': '08',
            'Sept': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12',
        }

        list_trends = []

        d = feedparser.parse(trendsgoogle)
        for entry in d.entries:
            title = entry.title
            trf = entry.ht_approx_traffic
            arr = entry.published.split(' ')
            month = dict_month.get(arr[2])
            if (month is None):
                is_dict_err = True
                break
            pub_date = arr[3] + '/' + month + '/' + arr[1]

            if (prev == ''):
                list_trends.append('++ 毎日の検索トレンド - 【' + pub_date + '】')
            elif (prev == pub_date):
                int_ranking = int_ranking + 1
            else:
                int_ranking = 1
                list_trends.append('++ 毎日の検索トレンド - 【' + pub_date + '】')

            list_trends.append(str(int_ranking) + '. ' + title + '    ' + trf + '\r\n' + query.format(title))
            prev = pub_date

        dict_trends = {}

        for i in range(len(list_trends)):
            dict_trends[i] = list_trends[i]

        return dict_trends
