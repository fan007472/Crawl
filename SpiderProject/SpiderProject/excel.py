# -*-coding:utf-8-*-

import xlrd


class ExcelUtil:


    def readExcel(self):
        wb = xlrd.open_workbook("D:\\浦东新区小学.xls")
        sheet = wb.sheet_by_index(0)
        max_rows = sheet.nrows
        max_rows = 4
        for i in range(1, max_rows):
            school = sheet.cell_value(i, 3)  #
            district = sheet.cell_value(i, 5)  # 学期
            print("{} 学区是 {}".format(school, district))


def main():
    t= ExcelUtil()
    t.readExcel()

if __name__ == '__main__':
    main()
