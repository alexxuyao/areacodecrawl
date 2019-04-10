# coding=UTF-8

from pyquery import PyQuery as pq
import time


def main():
    with open('./areas.txt', 'a+', encoding="utf-8") as f:

        break_city = False

        for pro in range(16, 99):
            for city in range(0, 99):
                for areaIndex in range(0, 99):

                    break_city = False

                    area_code = pro * 10000 + city * 100 + areaIndex
                    url = "http://qq.ip138.com/idsearch/index.asp?action=idcard&userid={}199302165529".format(area_code)
                    q = pq(url=url, encoding="gbk")
                    td = q('.tdc2')
                    text = td.eq(td.length - 1).remove('font').text()
                    text = text.split('\n')[0]
                    area = text.split(' ')

                    if len(area) > 2:
                        line = "{}\t{}\t{}\t{}\n".format(area_code, area[0], area[1], area[2])
                        print(line)
                        f.writelines(line)
                    else:
                        message = ""
                        if len(area) > 0:
                            message = area[0]
                        print("{}:{}".format(area_code, message))

                        if city == 0 and areaIndex == 0:
                            break_city = True

                        if areaIndex == 0:
                            break

                if break_city:
                    break


def stl56():
    with open('./areas-2.txt', 'a+', encoding="utf-8") as f:

        break_city = False

        for pro in range(10, 99):
            for city in range(0, 99):
                for areaIndex in range(0, 99):

                    break_city = False
                    title = ""
                    detect_count = 1

                    while True:
                        area_code = pro * 10000 + city * 100 + areaIndex
                        url = "http://www.stl56.com/idcard/{}.html".format(area_code)
                        q = pq(url=url, encoding="utf-8")
                        title = q('title').text()
                        if "网站防火墙" != title:
                            break
                        else:
                            print("firewall detect, sleep, {}", detect_count)
                            time.sleep(10 * detect_count)
                            detect_count = detect_count + 1

                    if len(title) > 0 and '_' in title:
                        area = title.split('_')[2]
                        line = "{}\t{}\n".format(area_code, area)
                        print(line)
                        f.writelines(line)
                    else:
                        print("{}:{}".format(area_code, title))

                        if city == 0 and areaIndex == 0:
                            break_city = True

                        if areaIndex == 0:
                            break

                if break_city:
                    break


if __name__ == '__main__':
    stl56()
