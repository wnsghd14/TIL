1. sql명령문 개괄 
    1. 연산순서 정렬
        from-where-group by-having-select-order by
    2. 종류 쓰는 문제 
        DML - select, insert, delete, update
        DDL - alter, create, modify, drop
        TCL - rollback, commit, 
        DCL - grant, revoke,
2. SELECT
    1. distinct (집약) -> 중복값을 하나의 정보만 나오도록 하는것
    2. Distinct deptno,mgr 괄호를 친거랑 똑같은거다. = group by(deptno,mgr)
    3. As -> select: as 생략가능, 컬럼명에 띄어쓰기 ''직원 번호 ''
          -> from : as 사용불가!
    4. concat 연산자는 인수가 2개! 
        -> +  SQL server 
        -> || SQL oracle
3. 논리연산자 -> 연산순위 : NOT(조건) -> AND(조건) -> OR(조건)
    1. and : A and B 둘다 만족한다
    2. or : A or B 둘중 하나만
    3. not : A not B 둘다 아니다
4. SQL 연산자 :
    1. Between 1 and 2 : 1<= A =<2
    2. in (1,2,3) : A= 1 or 2 or 3
    3. LIKE __ : 미지의 한 글자, LIKE % : 0이상 글자
    4. ESCAPE : 와일드카드(_%)를 문자로 취급
        ename like 'A_A' => 'A@_A
    5. Rownum(oracle) : (Where) Rownum = 1 포함
    6. Top(SQL server) : 

5. 