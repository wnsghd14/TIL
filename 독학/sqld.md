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
        1. Top(SQL server) : 상위N개 (컬럼명)
        2. SELECT enpno,sal where rownum <= 3 order by sal desc
5. NULL
    1. NULL의 정의 부재, 모르는값
    2. NULL + 2, NULL + 4, null * null = ? 알수없음(unknown)
    3. where 조건절에서 unknown이라면 False 와 비슷하다.
    4. 정렬 상 의미
        1. oracle infinity
        2. SQLserver -infinity
    5. nvl=(값1,값2), nvl2(값1,값2), isnull(값1,값2,값3), (같null다값)1nullif(값1,값2), (coalesce=null아닌 첫번째값)(값1,값2 ...)
6. 정렬
    1. 정렬의 특성 = 가장 마지막에 실행, 성능저하가능성, null값과의 관계
    2. 컬럼번호 정렬 = 출력되는 컬럼의 수 보다 큰 값 불허 
    3. 인수 두개 정렬 = sal desc, ename asc (sal이 같으면 ename 오름차순)
    4. select ename order by sal => 가능하다.
