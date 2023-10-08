'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

str_s = input("Write the second you want to convert: ")
total_second = int(str_s)


hours = total_second // 3600
second_still_remining = total_second % 3600

minuts = second_still_remining // 60
second_finaly_remining = second_still_remining %60

print("hour: ", hours,"\n" ,"minut: ",minuts , "\n" , "second: " , second_finaly_remining)