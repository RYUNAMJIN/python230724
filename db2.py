# db2.py

import sqlite3

#연결객체 생성(파일에 저장)
con = sqlite3.connect("c:\\work\\sample.db")
#커서객체
cur = con.cursor()
#테이블 구조 생성
cur.execute("create table if not exists PhoneBook" +
            " (id integer primary key autoincrement, " +
            " name text, phoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values " + 
            " ('홍길동','010-111');")

#입력 파라미터 처리
name = "전우치"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values " + 
            " (?,?);", (name, phoneNumber))

#다중으로 행 입력
datalist = (("이순신","010-333"),("박문수","010-444"))
cur.executemany("insert into PhoneBook (name, phoneNum) values " + 
            " (?,?);", datalist)

#검색구분
cur.execute("select * from PhoneBook;")
print(cur.fetchall())
#작업완료
con.commit()
