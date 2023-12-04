import mysql.connector
import os.path
import sys
import datetime
import time
import random
import requests
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

    ###
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
        def accountCreate():
            account = input("계좌 입력: ")
            if BankManager.accountCheck(account):
                name = input("이름 입력: ")
                bal = int(input("첫 금액 입금: "))
                AccountCreate(account, name, bal)
        
        
        # 2번 입금 
        def addBalance():
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
                                        
                                        
                    # 입금 내역 기록
                    myaccount = inputaccount + ".txt"
                    with open(myaccount, 'a', encoding='UTF-8') as f:
                        time = datetime.datetime.now()
                        f.write("{} : {} 원 입금하였습니다".format(time, inputmoney))
                        f.write("\n")
                        
                # 계좌번호 없을 경우
                else:
                    print("없는 계좌번호 입니다")
            else :
                print("첫 화면으로 돌아갑니다")


        # 3번 출금
        def withdrawBalance():
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
                            pass
                else:
                    print("없는 계좌번호 입니다")
                    print("첫화면으로 돌아갑니다")
            else:
                print("첫 화면으로 돌아갑니다")
                

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
            else:
                print("첫 화면으로 돌아갑니다")


                        
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
            else:
                print("첫 화면으로 돌아갑니다")

        # 환율 .. 어떻게 하징
        def exchangeCurrent( ):
            print("* 환율을 조회할 수 있는 메뉴입니다. \n")
            print("* 계속 진행하길 원하면 y , 첫 화면으로 가길 원하면 n 을 입력해주세요.")
            a = input()

            if a=="y":
                print("um..")
            else:
                print("첫 화면으로 돌아갑니다")


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
                    work = input("원하시는 번호를 입력하세요! : ")
                    work1= int(work)
                    if work1 >= 8:
                        raise Exception
                except Exception:
                    print("\n* 잘못 입력하셨습니다 !!!! 번호를 다시 확인해주세요")
                    time.sleep(2)
                else:
                    if work == "1":
                        BankManager.accountCreate()
                    elif work == "2":
                        BankManager.addBalance()
                    elif work == "3":
                        BankManager.withdrawBalance()
                    elif work == "4":
                        BankManager.showBalance()
                    elif work == "5":
                        BankManager.accountInfo()
                    # elif work == "5":
                        
                    elif work == "7":
                        with open('bankaccountlist.txt', 'w') as f:
                            for data in bankinform:
                                save = str(data[0]) + ":" + str(data[1]) + ":" + str(data[2]) + "\n"
                                f.write(save)
                        print("종료합니다")
                        sys.exit()
                


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
