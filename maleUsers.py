maleUsers = [
    {
      "name": "User1",
      "regno": "15BIT0000",
      "gender": "male",
      "username": "play"
    
    },
    {
      "name": "User2",
      "regno": "15bce0000",
      "gender": "male",
      "username": "sud0159"
    },
  ]

import xlsxwriter

workbook = xlsxwriter.Workbook('male.xlsx')
worksheet = workbook.add_worksheet()
for i in range(len(maleUsers)):
    worksheet.write('A'+str(i), maleUsers[i]["name"])
    worksheet.write('B'+str(i), maleUsers[i]["regno"])


workbook.close()