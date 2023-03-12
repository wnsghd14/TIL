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


1. null의 정의
- null이란 데이터의 정의가 없는 것
- null은 알수 없는 값
- null을 이용하여 숫자나 날짜 연산을 한다면 결과는 무조건 null
2. null 조회
- null 값을 조회 할 때는 조건절에 is null 또는 is not null을 사용
    - SELECT * From user where phone is (not) null;
3. 문자함수
- 데이터베이스내 함수들 가운데 내장함수
- 내장함수에서 문자를 다루는 문자함수
- 스크립트 실행
- lower/upper
    - select country_name as 원본, lower(원본) as 소문자, upper(원본) as 대문자, from country; 
- length
    - select country_name as 원본, length(원본) as 길이 from country; 
- substr
    - select country_name substr(country_name,2,2) from country; (2번째줄부터 2개)
- instr
    - select country_name instr(country_name,'A') from country;(A의 갯수를 세어준다. 대소문자 구분한다.)
- lapd/rapd
    - select country_name lpad(country_name,10,'A'),rpad(country_name,10,'A') from country;(왼쪽이나 오른쪽에 A를 넣어서 10글자를 만들어라)
- trim
    - select country_name trim(country_name)ltrim(country_name),trim(country_name)rtrim(country_name) from country; (공백제거)
- replace
    - select continent as 원본, replace(continent,'a','@') as replace from country; ('a'를 @로 치환)
4. 숫자함수
- round
    - select round(112.3456,1) r1,round(112.3456,2) r2,round(112.3456,-1) r3 from dual; (112.3456dml 자릿수 만큼에서 반올림해라. -1= 1의자리에서 반올림)
- ceil/floor
    - selcet ceil(26.3) r1, ceil(10.9),floor(26.3),floor(10.9) from dual; (ceil은 올림 floor는 버림)
- power (제곱해주는 함수) power(5,2)(5를 2제곱 해라.)

5. 날짜함수
- sysdate,systimestamp
    - sysdate = 현재 날짜 시간
    - systimestamp = 더욱 세세한 시간
- add_months,next_day,last_day(sysdate,6)
    - 말 그대로
- to_char
    - to_char(sysdate + 1 /24/ 60 / 60,'yyyy/mm/dd hh24:mi:ss') 1초후