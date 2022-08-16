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

- UPDATE 테이블 SET 컬럼=값 WHERE id
  
  - 해당하는 id 가 중점. 해당하는 id의 값 을 바꿔주세요
