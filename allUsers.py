user = [
    {
      "name": "User",
      "regno": "15BIT0000",
      "gender": "male",
      "username": "play"
    
    }
]
    [
    {
      "name": "User",
      "regno": "15bce0000",
      "gender": "male",
      "username": "sud0159"
    },
    {
      "name": "User",
      "regno": "15BIT0000",
      "gender": "male",
      "username": "play"
    
    }
]
    [
    {
      "name": "User",
      "regno": "15BIT0000",
      "gender": "male",
      "username": "play"
    
    },
    {
      "name": "User",
      "regno": "15BIT0000",
      "gender": "male",
      "username": "play"
    
    },
    {
      "name": "User",
      "regno": "15BIT0000",
      "gender": "male",
      "username": "play"
    
    }
    
  ]


import xlsxwriter

workbook = xlsxwriter.Workbook('members.xlsx')
worksheet = workbook.add_worksheet()
for i in range(len(user)):
    worksheet.write('A'+str(i), 'Team'+str(i))
    if(len(user[i])==1):
        worksheet.write('B'+str(i), user[i][0]["name"])
    elif(len(user[i])==2):
        worksheet.write('B'+str(i), user[i][0]["name"])
        worksheet.write('C'+str(i), user[i][1]["name"])
    elif(len(user[i])==3):
        worksheet.write('B'+str(i), user[i][0]["name"])
        worksheet.write('C'+str(i), user[i][1]["name"])
        worksheet.write('D'+str(i), user[i][2]["name"])
    else:
        worksheet.write('B'+str(i), user[i][0]["name"])
        worksheet.write('C'+str(i), user[i][1]["name"])
        worksheet.write('D'+str(i), user[i][2]["name"])
        worksheet.write('E'+str(i), user[i][3]["name"])


    worksheet.write('F'+str(i), str(user[i][0]["phoneno"]))
    worksheet.write('G'+str(i), str(user[i][0]["email"]))
workbook.close()