import mysql.connector
import os.path
import sys
import datetime
import time
import random
import requests
from bs4 import BeautifulSoup
import pymysql
import pandas as pd


try:
    # MySQL 서버 연결 설정
    connection = mysql.connector.connect(
        host="192.168.56.101",
        port=4567,
        user="lee",
        password="1017",
        database="Bank"
    )

   
    cursor = connection.cursor()


    class AccountCreate:

        def __init__(self, userAccount, userName, userBalance=0):
            self.userAccount = userAccount
            self.userName = userName
            self.userBalance = userBalance

            bankinform.append([userAccount,userName,userBalance]) # 계좌 이름 잔액 저장
            allAccount.append(userAccount)
            

            # 최초 입금 기록 저장
            accountfile = userAccount + ".txt"
            with open(accountfile, 'a', encoding="UTF-8") as f:
                time = datetime.datetime.now()
                f.write("{} : {} 원 입금하였습니다".format(time, self.userBalance))
                f.write("\n")



    class BankManager:

        # 계좌 확인
        def accountCheck(account):
            if account in allAccount:
                print("계좌 생성 실패")
                print("이미 존재하는 계좌번호입니다.")
            else:
                return True
            
        # 1번 계좌 개설
        def create(): # 헷갈려서 이름 변경 
            # 추천 계좌 생성 
            first = '%02d'%random.randint(0,99)
            now = datetime.datetime.now()
            second = now.strftime("%Y%m%d")
            third = '%06d'%random.randint(0,999999)
            recommend = first + "-" + second + "-" + third
            print("* 원하는 번호로 계좌를 생성 할 수 있습니다.\
                \n\n 추천 계좌 번호 : \
                    \n<< {} >>\
                        \n===========================================".format(recommend))
            print("* 계속 진행하길 원하면 y , 첫 화면으로 가길 원하면 n 을 입력해주세요.")
            a = input()
            if a=="y":
                account = input(" - 계좌 번호: ")
                if BankManager.accountCheck(account): # 중복확인
                    name = input(" - 이름 입력: ")
                    print("\n* 계좌개설을 위해 소정의 금액을 입금이 필요합니다.\
                        \n* 얼마를 입금하시겠습니까?\n")
                    bal = int(input(" - 첫 입금 금액: "))
                    print("\n* 개설이 완료 되셨습니다. 첫화면으로 이동합니다.")
                    
                    # 입력 받은 데이터를 AccountCreate 클래스로 
                    AccountCreate(account, name, bal)
            elif a=="n":
                BankSystem.lobby()        
        
            
        
        # 2번 입금 
        def deposit():
            print("* 입금처리를 진행할 계좌번호를 입력해주세요\n")
            print("* 계속 진행하길 원하면 y , 첫 화면으로 가길 원하면 n 을 입력해주세요.")
            a = input()
            if a=="y":
                inputaccount = input("계좌: ") # 계좌번호 입력
                if inputaccount in allAccount: # 계좌번호가 존재하면 금액 입력
                    inputmoney = int(input("금액: ")) # 금액 입력
                    for account in bankinform: # 계좌번호 찾기 
                        if inputaccount == account[0]: # 
                            account[2] = int(account[2]) + inputmoney # 계좌번호 잔액에 금액 추가
                            print("\n* {}원 입금이 완료 되었습니다. 첫화면으로 이동합니다.".format(inputmoney))  # 입금 되었는지 확인          
                            BankSystem.pyHistoryD(inputmoney)           
                                        


                    # 입금 내역 기록
                    myaccount = inputaccount + ".txt"
                    with open(myaccount, 'a', encoding='UTF-8') as f:
                        time = datetime.datetime.now()
                        f.write("{} : {} 원 입금하였습니다".format(time, inputmoney))
                        f.write("\n")
                        
                # 계좌번호 없을 경우
                else:
                    print("===== [!] 없는 계좌번호 입니다 =====")
                    print("* 첫 화면으로 돌아갑니다 ")
                    
                BankSystem.lobby() 
            else :
                BankSystem.lobby() 


        # 3번 출금
        def withdraw():
            print("* 출금처리를 진행할 계좌번호를 입력해주세요\n")
            print("* 계속 진행하길 원하면 y , 첫 화면으로 가길 원하면 n 을 입력해주세요.")
            a = input()
            if a=="y":
                inputaccount = input("계좌: ")
                if inputaccount in allAccount:
                    inputmoney = int(input("금액: "))
                    for account in bankinform:
                        if inputaccount == account[0]:
                            if int(account[2]) >= inputmoney:
                                account[2] = int(account[2]) - inputmoney
                                myaccount = inputaccount + ".txt"
                                with open(myaccount, 'a', encoding='UTF-8') as f:    
                                    time = datetime.datetime.now()
                                    f.write("{} : {} 원 출금하였습니다".format(time, inputmoney))
                                    f.write("\n")
                            else:
                                print("잔액이 모자랍니다")
                                print("첫화면으로 돌아갑니다")
                        else:
                            pass    # 다음 거 찾아주기 
                else:    # 없는 계좌면 
                    print("없는 계좌번호 입니다")
                    print("첫화면으로 돌아갑니다")
            else:
                print("첫 화면으로 돌아갑니다")
                BankSystem.lobby() 
                

        # 4번 잔액조회
        def showBalance():
            print("* 잔액조회 하고 싶은 계좌번호를 입력해주세요\n")
            print("* 계속 진행하길 원하면 y , 첫 화면으로 가길 원하면 n 을 입력해주세요.")
            a = input()
            if a=="y":
                inputaccount = input("계좌를 입력해주세요: ")
                if inputaccount in allAccount:
                    for account in bankinform:
                        if inputaccount == account[0]:
                            print("{} 계좌의 잔액은 {} 원입니다".format(account[0], account[2]))
                            print("첫 화면으로 돌아갑니다")
                else:   # 없는 계좌면 
                    print("없는 계좌번호 입니다")
                    print("5초 후에 첫 화면으로 돌아갑니다")
            else:
                print("첫 화면으로 돌아갑니다")
                BankSystem.lobby() 

                        
        # 5번 계좌 입출금 이력 조회
        def accountInfo():
            print("* 입출금 이력을 조회할 계좌번호를 입력해주세요\n")
            print("* 계속 진행하길 원하면 y , 첫 화면으로 가길 원하면 n 을 입력해주세요.")
            a = input()
            if a=="y":
                inputaccount = input("계좌 번호: ")
                accountfile = inputaccount + '.txt'
                if os.path.isfile(accountfile):
                    with open(accountfile, 'r', encoding='UTF-8') as f:
                        datas = f.readlines()
                        cnt=0
                        for data in datas:
                            cnt+=1
                            print('[{}] {}'.format(cnt,data),end="")
                else:
                    print("이력이 없습니다")
                    print("첫 화면으로 돌아갑니다")
            else:
                print("첫 화면으로 돌아갑니다")
                BankSystem.lobby() 



        # 환율 .. 어떻게 하징
        def exchangeCurrent( ):
            print("* 환율을 조회할 수 있는 메뉴입니다. \n")
            print("* 계속 진행하길 원하면 y , 첫 화면으로 가길 원하면 n 을 입력해주세요.")
            a = input()

            if a=="y":
                address = f'https://finance.naver.com'
                addition = '/marketindex/?tabSel=exchange#tab_section'

                #환율 테이블 안에서 꺼내와야하므로 2번에 걸쳐서  
                res = requests.get(address +addition)
                soup = BeautifulSoup(res.text, 'html.parser')
                frame = soup.find('iframe', id="frame_ex1")
                frameaddr = address + frame['src'] #frame내 src값 찾아서 연결된 주소 확인하기 

                res1 = requests.get(frameaddr) # frame내의 연결된 주소 읽어오기 
                frame_soup = BeautifulSoup(res1.text, 'html.parser')
                items = frame_soup.select('body > div > table > tbody > tr')

                #bs4 요소 빼주기
                for item in items:
                    name = item.select('td')[0].text.replace("\n","")# 줄바꿈없애고
                    name = name.replace("\t", "") # 탭없애고
                    price = item.select('td')[1].text
                    print(name + "\t" + price)

            else:
                    print("첫 화면으로 돌아갑니다")
                    BankSystem.lobby()     

    class BankSystem:
        def lobby():
            while True:
                print(" \n====== Seojin Lee의 은행 ======\n")
                print("= 이용하시기 원하는 메뉴번호를 입력해주세요=")
                print(" [1] 계좌 개설")
                print(" [2] 입금 처리")
                print(" [3] 출금 처리")
                print(" [4] 잔액 조회")
                print(" [5] 입출금 이력 조회")
                print(" [6] 환율 조회")
                print(" [7] 프로그램 종료")
                print("\n======================================")
            
                try:
                    work = input("원하시는 번호를 입력하세요!   ")
                    work1= int(work)
                    if work1 >= 8:
                        raise Exception
                except Exception:
                    print("\n* 잘못 입력하셨습니다 !!!! 번호를 다시 확인해주세요")
                    time.sleep(2)
                else:
                    if work == "1":
                        print("\n============= [1] 계좌 개설 ===============")
                        BankManager.create()
                        print("============================================")
                        time.sleep(2)
                    elif work == "2":
                        print("\n============= [2] 입금 처리 ===============")
                        BankManager.deposit()
                        print("============================================")
                        time.sleep(2)
                    elif work == "3":
                        print("\n============= [3] 출금 처리 ===============")
                        BankManager.withdraw()
                        print("============================================")
                        time.sleep(2)
                    elif work == "4":
                        print("\n============= [4] 잔액 조회 ===============")
                        BankManager.showBalance()
                        print("============================================")
                        time.sleep(5)
                    elif work == "5":
                        print("\n============= [5] 입출금 기록 ===============")
                        BankManager.accountInfo()
                        print("\n============================================")
                        time.sleep(2)
                    elif work == "6":
                        print("\n============= [6] 환율 조회 ===============")
                        BankManager.exchangeCurrent()
                        print("============================================")
                        time.sleep(5)
                    elif work == "7":
                        print("=============================================")
                        with open('bankaccountlist.txt', 'w') as f:
                            for data in bankinform:
                                save = str(data[0]) + ":" + str(data[1]) + ":" + str(data[2]) + "\n"
                                f.write(save)
                        
                        conn = pymysql.connect(host="localhost", port=4567, db="Bank", passwd="1017", user="bank_user")
                        cur = conn.cursor()
                        result = pd.read_sql_query('select * from history',conn)
                        print(result)
                        cur.close()
                        conn.close()          
                        print("\n종료합니다")
                        sys.exit()
                
        def pyHistoryD(x):
            conn = pymysql.connect(host="localhost", port=4567, db="Bank", passwd="1017", user="bank_user")
            cur = conn.cursor()
                
            sql =''' 
            insert into history(계좌번호,이름,입출금,금액,잔액)
            values(%s,%s,%s,%s,%s);
            '''
            for data in bankinform:                      
                cur.execute(sql,(str(data[0]),str(data[1]),"입금",int(x),int(data[2])))
            conn.commit()
            cur.close()
            conn.close()
        
        
        
        def pyHistoryW(x):
            conn = pymysql.connect(host="localhost", port=4567, db="Bank", passwd="1017", user="bank_user")
            cur = conn.cursor()
                
            sql =''' 
            insert into history(계좌번호,이름,입출금,금액,잔액)
            values(%s,%s,%s,%s,%s);
            '''
            for data in bankinform:                      
                cur.execute(sql,(str(data[0]),str(data[1]),"출금",int(x),int(data[2])))
            conn.commit()
            cur.close()
            conn.close()
        

    bankinform = []
    allAccount = []


    if __name__ == "__main__":
        if os.path.isfile('bankaccountlist.txt'): # 이전 정보 확인
            with open('bankaccountlist.txt', 'r') as f:
                datas = f.readlines()

                # bankinform에는 실제 [[계좌,이름,금액],[계좌,이름,금액]]형식으로 들어가있음          
                for data in datas:
                    bankinform.append(data[:-1].split(":")) #줄바꿈은 제외하기위해서 -1까지

            for account in bankinform: # 계좌번호 리스트 저장
                allAccount.append(account[0])
        else:
            pass

        BankSystem.lobby()


except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    # 연결 닫기
    if 'connection' in locals():
        connection.close()
