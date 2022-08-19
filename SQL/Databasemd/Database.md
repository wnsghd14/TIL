## Database

- 데이터베이스는 체계화된 데이터의 모임

- 여러사람이 공유하고 사용할 목적으로 통합관리되는 정보의 집합

- 논리적으로 연관된 자료의 모음으로 그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한것

- 

- 데이터베이스로 얻는 장점들
  
  - 데이터 중복 최소화(정확한 정보를 보장)
  
  - 데이터무결성
  
  - 데이터 일관성
  
  - 독립성(물리적/논리적)
  
  - 표준화
  
  - 보안유지

## RDB

- 관계형 데이터베이스
  
  - 서로 관련된 데이터를 저장하고 접근할수있는 데이터베이스 유형
  
  - 키와 값들의 간단한 관계를 표 형태로 정리한 데이터 베이스
  
  - 1 홍길동 제주 20
  
  - 2 김길동 서울 30
  
  - 3 박길동 독도 40

- 스키마
  
  - 데이터베이스에서 자료의 구조, 표현방법,관계등 전반적인 명세를 기술한것
  
  - id int
  
  - name text
  
  - address text
  
  - age int

- 테이블
  
  - 열(컬럼,필드)과 행(레코드,값)의 모델을 사용해 조직된 데이터 요소들의 집합
    
    - 열 (각 열에 고유한 데이터형식 지정)
    
    - 행(실제 데이터가 저장되는 형태)
    
    - 기본키(각 행의 고유값) : 반드시 설정해야하며 데이터베이스 관리 및 관계설정시 주요하게 활용됨!'PK'

- 관계형 데이터베이스 관리시스템
  
  - 관계형 모델을 기반으로 하는 데이터베이스 관리시스템
    
    - mysql /sqlite /postgresql /oracle /sql server
    
    - 본 수업에선 sqlite 사용

- SQLite
  
  - 서버형태가아닌 파일 형식으로 응용프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
  
  - 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임데비드 소프트웨어에도 많이 활용됨
  
  - 로컬에서 간단한 DB 구성을 할수 있으며, 오픈소스 프로젝트이기 때문제 자유롭게 사용가능
  
  - 데이터 타입:
    
    - integer,text,blob,real,numeric

- SQL(Structured Query Language)
  
  - 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적 프로그래밍 언어
  
  - 데이터베이스 스키마 생성 및 수정
  
  - 자료의 검색 및 관리
  
  - 데이터베이스 객체 접근 조정 관리
  
  - DDL(데이터정의언어) 관계형 데이터베이스 구조를 정의하기위한 명령어 
    
    - create drop alter
  
  - DML(데이터조작언어) 데이터를 저장 조회 수정 삭제등을 하기위한 명령어 
    
    - insert select update delete
  
  - DCL(데이터제어언어) 데이터베이스 사용자의 권한제어를 위해 사용하는 명령어 
    
    - grant revoke commit rollback

-  다음과 같은 스키마를 가지고 있는 classmates 테이블을 만들고 스키마를 확인해보세요.
  
  - column datatype
  
  - name Text
  
  - age INT
  
  - address TEXT

- 필드제약조건
  
  - NOT NULL: NULL값 입력금지
  
  - UNIQUE: 중복값입력금지(NULL은 중복가능)
  
  - PRIMARY KEY: 테이블에서 반드시하나. NOT NULL + UNIQUE
  
  - FOREIGN KEY: 외래키. 다른 테이블의 KEY
  
  - CHECK: 조건으로 설정된 값만 입력허용
  
  - DEFAULT : 기본설정값

- INSERT
  
  - 테이블에 단일 행 삽입
    
    - INSERT INTO 테이블_이름 () VALUES ()

- SELECT
  
  - 테이블에서 데이터를 조회
  
  - SELECT 문은 SQLite 에서 가장 기본이 되는 문이며 다양한 절(clause)과 함께 사용
    
    - ORDER BY,DISTINCT,WHERE,LIMIT,GROUP BY
  
  - LIMIT
    
    - 쿼리에서 반환되는 행수를 제한
    
    - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도함
  
  - WHERE
    
    - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
  
  - SELECT DISTINCT
    
    - 조회결과에서 중복행을 제거
    
    - DISTINCT 절은 SELECT 키워드 바로뒤에 작성해야함

- OFFSET
  
  - 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형
    
    - EX:LIMIT 2 2칸띄운 그이후 값이 나옴.

- DELETE 
  
  - 쿼리에서 어떠한 요소를 지움.

- PRIMARY KEY AUTOINCREMENT
  
  - EX: 5를 삭제한 이후 새로운 값을 INSERT 했을때 6부터 시작.

- UPDATE 
  
  - UPDATE 테이블 SET 컬럼=값 WHERE id
  
  - 해당하는 id 가 중점. 해당하는 id의 값 을 바꿔주세요
  
  - INSERT INTO 테이블이름 VALUES 값; 
  
  - SELECT * FROM 테이블이름 WHERE 조건;
  
  - UPDATE 테이블이름 SET 컬럼1,컬럼2 WHERE 조건;
  
  - DELETE FROM 테이블이름 WHERE 조건;

- WHERE
  
  - TABLE users 생성

### SQL 사용할수 있는 연산자

- BETWEEN 값1 AND 값2
  
  - 값 1과 값2 사이의 비교

- IN
  
  - 목록중에 값이 하나라도 일치하면 성공

- LIKE
  
  - 비교문자열과 형태일치
  
  - 와일드카드(%: 0개이상문자,  _ : 1개단일문자)

- IS NULL/IS NOT NULL
  
  - NULL여부를 확인할때는 항상-대신에 IS를 활용

- 부정연산자
  
  - 같지않다(!=,^=,<>)
  
  - ~와 같지않다(NOT 칼럼명 =)
  
  - ~보다 크지않다(NOT 칼럼 >)

- 연산자 우선순위
  
  - 1순위: 괄호
  
  - 2순위: NOT
  
  - 3순위: 비교연산자, SQL
  
  - 4순위:AND
  
  - 5순위:OR

- 집계함수
  
  - 값 집합에대한 계산을 수행하고 단일 값을 반환
    
    - 여러 행으로부터 하나의 결괏값을 반환하는 함수
  
  - SELECT 구문에서만 사용됨
  
  - 예시
    
    - COUNT(*)
      
      - 그룹의 항목수
    
    - AVG
      
      - 평균값계산
    
    - MAX
      
      - 그룹 내의 모든 최댓값
    
    - MIN
      
      - 그룹 내의 모든 최솟값
    
    - SUM
      
      - 모든값의 합

- LIKE
  
  - 패턴 일치를 기반으로 데이터를 조회하는 방법
  
  - SQLite 는 패턴구성을 위한 2개의 wildcards 를 제공
    
    - %
      
      - 0개 이상의 문자
    
    - _
      
      - 임의의 단일문자
      
      | 2%               | 2로 시작하는 값                 |
      | ---------------- | ------------------------- |
      | %2               | 2로 끝나는 값                  |
      | %2%              | 2가 들어가는 값                 |
      | _2%              | 아무값이 하나 있고 두번째가 2로 시작하는 값 |
      | 1___             | 1로 시작하는 4자리의 값            |
      | 2_%_______%/2__% | 2로 시작하고 적어도 3자리인 값        |
  
  - ex: SELECT * FROM WHERE 테이블이름 LIKE '패턴'
    
    - 정규표현식도 있긴함!(문자열 패턴매칭)

- ORDER BY
  
  - 조회결과집합을 정렬
  
  - SELECT 문에 추가하여 사용
  
  - 정렬순서를 위한 2개의 KEYWORD 제공
    
    - ASC - 오름차순
    
    - DESC - 내림차순

- 문자열 함수
  
  - SUBSTR(문자열,START,LENGTH): 문자열 자르기
    
    - 시작 인덱스는 1 , 마지막 인덱스는 -1
  
  - TRIM,LTRIM,RTRIM: 문자열 공백제거
  
  - LENGTH: 문자열 길이
  
  - REPLACE (문자열,패턴,변경값): 패턴에 일치하는 부분을 변경
  
  - UPPER,LOWER : 대소문자 변경
  
  - II : 문자열 합치기

- 숫자 함수
  
  - ABS:절대 값
  
  - SIGN:부호
  
  - MOD(숫자1,숫자2): 숫자1을 숫자 2로 나눈 나머지
  
  - CEIL,FLOOR,ROUND: 올림,내림,반올림
  
  - POWER(숫자1,숫자2):숫자 1 숫자 2의 제곱
  
  - SQRT :제곱근

- 집계함수 다시보기
  
  - 값 집합에 대한 계산을 수행하고 단일 값을 반환
    
    - 여러 행으로부터 하나의 결괏값을 반환하는 함수
  
  - SELECT 구문에서만 사용됨
  
  - 예시
    
    - 테이블 전체 행 수를 구하는 COUNT(*)
    
    - age 컬럼 전체 평균 값을 구하는 AVG(age)

- ALIAS
  
  - 칼럼명이나 테이블명이  길거나 다른 명칭으로 확인하고 싶을 때는 ALIAS를 활용
  - AS 를 생략하여 공백으로 표현할 수 있음
  - 별칭에 공백, 특수문자 등이 있는 경우 따움표로 묶어서 표기

- GROUP BY
  
  - SELECT 문의 optional 절
  
  - 행 집합세어 요약 행 집합을 만듬
  
  - 선택된 행 그룹을 하나 이상의 열 값으로 요약행으로 만듬
  
  - 문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야함
  
  - 지정된 컬럼의 값이 같은 행들로 묶음
  
  - 집계함수와 활용하였을때 의미가 있음
    
    - (SELECT * FROM users GROUP BY LAST_NAME;) => X
  
  - 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨짐

- HAVING
  
  - 집계함수는 WHERE 절의 조건식에서는 사용할 수 없음(실행 순서에 의해)
    
    - WHERE 로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞서 있기 때문
  
  - 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 HAVING 을 활용

- SELECT 문장 입력 순서
  
  - SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, OFFSET

- SELECT 문장 실행 순서
  
  - FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY
    
    - FROM 테이블을 대상으로
    
    - WHERE 제약조건에 맞춰서 뽑아서
    
    - GROUP BY그룹화한다
    
    - HAVING 그룹중에조건과맞는것을
    
    - SELECT 조회하여
    
    - ORDER BY 정렬하고
    
    - LIMIT,OFFSET 특정위치의 값을 가져온다.

- ALTER TABLE
  
  - 테이블 이름 변경: 
    
    - ALTER TABLE table_name RENAME TO new_name;
  
  - 새로운 COLUMN 추가: 
    
    - ALTER TABLE table_name ADD COLUMN column definition;
  
  - COLUMN 이름 수정: 
    
    - ALTER TABLE table_name RENAME COLUMN current_name TO new_name;
  
  - CLOLUMN 삭제:
    
    - ALTER TABLE table_name DROP COLUMN column_name;

### Case

- case문은 특정 상황에서 데이터를 변환하여 활용할수 있음

- else 를 생략하는 경우 null 값이 지정됨

- ```
  CASE
      WHEN 조건식 THEN 식
      WHEN 조건식 THEN 식
      ELSE 식
  END
  ```

### 서브쿼리

- 서브쿼리는 특정값을 메인쿼리에 반환하여 활용

- 실제 테이블에 없는 기준을 이용한 검색 가능

- 서브쿼리는 소괄호로 감사서 사용하며, 메인쿼리의 칼럼을 모두 사용가능

- 메인쿼리는 서브쿼리의 칼럼을 이용할수 없음

- 단일행 서브쿼리
  
  - 서브쿼리의 결과가 0또는 1개인 경우
  
  - 단일행 비교연산자와 함께 사용 ( =,>,<,<=,>=,<>)

- 다중행 서브쿼리
  
  - 서브쿼리 결과가 2개 이상인 경우
  
  - 다중행 비교 연산자와 함께 사용(IN,EXISETS 등)

- 다중컬럼 서브쿼리
