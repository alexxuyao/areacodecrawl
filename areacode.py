# coding=UTF-8

from pyquery import PyQuery as pq

def main():
    with open('C:/Users/Administrator/areas.txt', 'a+', encoding="utf-8") as f:

        breakCity = False

        for pro in range(16, 99):
            for city in range(0, 99):
                for areaIndex in range(0, 99):

                    breakCity = False

                    areacode = pro * 10000 + city * 100 + areaIndex
                    url = "http://qq.ip138.com/idsearch/index.asp?action=idcard&userid={}199302165529".format(areacode)
                    q = pq(url=url, encoding="gbk")
                    td = q('.tdc2')
                    area = td.eq(td.length - 1).remove('font').text().split(' ')
                    if len(area) > 2:
                        line = "{}\t{}\t{}\t{}\n".format(areacode, area[0], area[1], area[2])
                        print(line)
                        f.writelines(line)
                    else:
                        message = ""
                        if len(area) > 0:
                            message = area[0]
                        print("{}:{}".format(areacode, message))

                        if city == 0 and areaIndex == 0:
                            breakCity = True

                        if areaIndex == 0:
                            break

                if breakCity:
                    break


if __name__ == '__main__':
    main()
