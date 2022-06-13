import xlrd


def get_info_login():
    url = "https://sb.halome.dev/"
    sheet = read_info_login_from_file()
    pin = "123456"
    return url, sheet, pin


def get_info_login_anonymous():
    url = "https://sb.halome.dev/"
    phone_number = "84963594847"
    opt = "000000"
    return url, phone_number, opt


def read_info_login_from_file():
    # Give the location of the file
    loc = "../File/infoLogin.xlsx"
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    return sheet
    # username_pwd_list = []
    # for row in range(sheet.nrows):
    #     if row < sheet.nrows - 1:
    #         username_pwd = []
    #         for col in range(sheet.ncols):
    #             username_pwd.append(sheet.cell_value(row + 1, col))
    #         username_pwd_list.append(username_pwd)
    # return username_pwd_list