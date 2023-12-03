import mysql.connector

try:
    # MySQL 서버 연결 설정
    connection = mysql.connector.connect(
        host="192.168.56.101",
        port=4567,
        user="lee",
        password="1017",
        database="madang"
    )

    # 커서 생성
    cursor = connection.cursor()

    # Book 테이블에서 데이터 가져오기
    cursor.execute("SELECT * FROM Book")
    book_records = cursor.fetchall()

    # Customer 테이블에서 데이터 가져오기
    cursor.execute("SELECT * FROM Customer")
    customer_records = cursor.fetchall()

    # Book 데이터 출력
    print("Book Table:")
    for row in book_records:
        book_id, book_name, price, publisher = row
        print(f"Book ID: {book_id}, Book Name: {book_name}, Price: {price}, Publisher: {publisher}")

    # Customer 데이터 출력
    print("\nCustomer Table:")
    for row in customer_records:
        cust_id, name, address, phone = row
        print(f"Customer ID: {cust_id}, Name: {name}, Address: {address}, Phone: {phone}")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    # 연결 닫기
    if 'connection' in locals():
        connection.close()
