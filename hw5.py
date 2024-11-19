import mysql.connector

# MySQL 연결 설정
try:
    connection = mysql.connector.connect(
        host="192.168.1.101",  
        port=4567,             
        user="esther",      
        password="Dptmej6408!",  
        database="madang"      
    )

    if connection.is_connected():
        print("MySQL에 성공적으로 연결되었습니다.")
        cursor = connection.cursor()

        while True:
            print("\n--- Menu ---")
            print("1. 데이터 삽입")
            print("2. 데이터 삭제")
            print("3. 데이터 검색")
            print("4. 종료")
            choice = input("선택: ")

            if choice == "1":
                title = input("책 제목: ")
                publisher = input("출판사: ")
                price = input("가격: ")

                insert_query = "INSERT INTO Book (bookname, publisher, price) VALUES (%s, %s, %s)"
                values = (title, publisher, price)

                cursor.execute(insert_query, values)
                connection.commit()
                print("데이터가 성공적으로 삽입되었습니다.")

            elif choice == "2":
                book_id = input("삭제할 책 ID: ")

                delete_query = "DELETE FROM Book WHERE bookid = %s"
                values = (book_id,)

                cursor.execute(delete_query, values)
                connection.commit()
                print("데이터가 성공적으로 삭제되었습니다.")   
                

            elif choice == "3":
                title = input("검색할 책 제목: ")
                search_query = "SELECT * FROM Book WHERE bookname LIKE %s"
                cursor.execute(search_query, (f"%{title}%",))

                # 검색 결과 출력
                rows = cursor.fetchall()
                print("\n--- 검색 결과 ---")
                if rows:
                    for row in rows:
                        print(f"ID: {row[0]}, 제목: {row[1]}, 출판사: {row[2]}, 가격: {row[3]}")
                else:
                    print("검색 결과가 없습니다.")


            elif choice == "4":
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 선택입니다. 다시 시도하세요.")

except mysql.connector.Error as e:
    print(f"오류 발생: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL 연결이 종료되었습니다.")
