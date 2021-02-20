import time
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

        d = ''
        while True:
            d = feedparser.parse(trendsgoogle)
            time.sleep(1)
            print('[debug] {}'.format(d))
            if True:
                break

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
                list_trends.append('■ {}の検索トレンド'.format(pub_date))
            elif (prev == pub_date):
                int_ranking = int_ranking + 1
            else:
                int_ranking = 1
                list_trends.append('■ {}の検索トレンド'.format(pub_date))

            list_trends.append(str(int_ranking) + '. ' + title + '    ' + trf)
            prev = pub_date

        result = 'tmp'
        if is_dict_err:
            result = '[Err] dict_month do not have terget month.'
        else:
            for i in list_trends:
                if result != 'tmp':
                    result = result + '\r\n' + i
                else:
                    result = i

        dict_trends = {}
        dict_trends[0] = result

        return dict_trends
