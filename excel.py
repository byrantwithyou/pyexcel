from xlwt import Workbook
import xlwt
import os
book = Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 0")
style = xlwt.XFStyle()
align = xlwt.Alignment()
align.horz = xlwt.Alignment.HORZ_CENTER
align.vert = xlwt.Alignment.VERT_CENTER
style.alignment = align
sheet1.write_merge(0, 1, 0, 0, "编号", style=style)
sheet1.write_merge(0, 1, 1, 1, "方向", style=style)
sheet1.write_merge(0, 1, 2, 2, "小汽车", style=style)
sheet1.write_merge(0, 0, 3, 5, "大车", style=style)
sheet1.write_merge(1, 1, 3, 3, "公交", style=style)
sheet1.write_merge(1, 1, 4, 4, "货车", style=style)
sheet1.write_merge(1, 1, 5, 5, "其他", style=style)
files = [file for file in os.listdir("./data") if "txt" in file]
currentID = ""
currentRow = 2
for file in files:
  if file[:6] != currentID:
    currentID = file[:6]
    sheet1.write(currentRow, 0, currentID, style=style)
  sheet1.write(currentRow, 1, file[6: -4], style=style)
  stat = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0
  }
  with open(os.path.join("data", file)) as f:
    for line in f:
      for char in line:
          if char in ["1", "2", "3", "4"]:
            stat[char] += 1
  sheet1.write(currentRow, 2, stat["1"], style=style)
  sheet1.write(currentRow, 3, stat["2"], style=style)
  sheet1.write(currentRow, 4, stat["3"], style=style)
  sheet1.write(currentRow, 5, stat["4"], style=style)
  currentRow += 1
  sheet1.col(0).width = 10000
  sheet1.col(1).width = 20000
  book.save("output.xls")
