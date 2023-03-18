\1. **정답 : \**4\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a1)

 

해설 : 상급종합병원에는 한 명의 혹은 여러 명의 의사가 근무하고 모델링으로는 의사가 없을 수도 있다.

진료는 의사만 할 수 있고 의사는 진료를 하지 않을 수도 있다.



![img](https://blog.kakaocdn.net/dn/d2YhKO/btrC1i4VJj1/LUagKEKzbigI2GoXLhRsVK/img.png)두 엔터티간 관계에서 수행되는 경우의 수 (관계차수)





\2. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a2)

 

해설 : 

**성능 데이터 모델링 고려사항**

\1) 정규화를 수행하여 데이터베이스 모델의 유연성을 확보한다.

\2) 데이터베이스의 전체 용량, 월간, 연간 증감율을 예측한다.

\3) **애플리케이션의 트랜잭션의 유형(CRUD: Create Read Update Delete)을 파악한다.**

\4) 합계 및 정산 등을 수행하는 반정규화를 수행한다.(성능향상을 위한 튜닝)

\5) 기본키와 외래키, 수퍼타입과 서브타입 등을 조정한다.

\6) 성능관점에서 데이터 모델을 검증하고 확인한다.

 

**[ 3가지 모델링 알아두기 ]**

- 개념적 모델링: 개체와 개체들 간의 관계에서 ER다이어그램을 만드는 과정
- 논리적 모델링: ER다이어그램을 사용하여 관계 스키마 모델을 만드는 과정
- 물리적 모델링: 관계 스키마 모델의 물리적 구조를 정의하고 구현하는 과정

 



\3. **정답 : \**3\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a3)

 

해설 : **논리적 모델은 비즈니스 정보의 논리적 구조 및 구축을 파악할 수도 있다**.

즉, 핵심 엔터티와 키 엔터티등을 식별하고 모델링하여 데이터베이스 **구조를 모델링**한다.



![img](https://blog.kakaocdn.net/dn/qlNiw/btrC3dnMJAx/Vq1eGUfqprbLSmOFW3cAxk/img.png)데이터 모델링 과정 by yunamom



 

 



\4. **정답 : \**3\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a4)

 

해설 : 이용내역 엔터티에서 **이용일자 + 사원번호가 기본키(PK) 이므로 일자가 같은 날에 여러 콘도를 이용할 수 없다.**

 

사원, 이용 내역( (**1 : M**) **→** 1명의 사원은 이용내역이 있을수도 있고 없을수도 있다.)

콘도이용정보, 이용 내역( (**1 : 0 or 1 : 1** ) : M **→** 콘도 이용정보가 있을수도 있고 없을수도 있으며 콘도 이용정보가 이용내역에 있을수도 있고 없을수도 있다.)

 



\5. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a5)

 

해설 : 정규화(Normalization)는 함수적 종속성에 따라서 **테이블을 분해하는 과정**으로 데이터 **중복을 제거**해서 모델의 독립성을 향상시킨다. 그리고 **정규화를 수행하지 않으면 발생되는 문제가 갱신이상** (이상현상(Anoma-ly) 삽입, 삭제, 수정 이상현상이 있다.) 이고,

**데이터베이스 보안과 관련이 있는 것은 뷰(View) 이다.**

 



\6. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a6)

 

해설 : **기본키(PK)**는 엔터티를 대표하는 키로 최소성(Not Null)과 유일성(중복 없음)을 만족해야 한다.

**외래키(FK)**는 두 개의 테이블 간에 연결을 설정하기 위한 Key이다. 한 테이블의 기본키를 참조하는 다른 테이블의 칼럼이다.

 

파생속성 **→** 어떤 데이터를 기반으로 만들어진 데이터, 예) 주식의 가격의 평균데이터 등 

 



\7. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a7)

 

해설 : **엔터티는 관계를 2개 이상 가질 수 있다.**

| **엔터티 특징**   | **설명**                                                     |
| ----------------- | ------------------------------------------------------------ |
| **식별자**        | - 엔터티는 유일한 식별자가 있어야 한다. 예) 를 들어 회원ID, 계좌번호 |
| **인스턴스 집합** | - 2개 이상의 인스턴스가 있어야 한다. 예) 고객정보는 2명이상 있어야 한다. |
| **속성**          | - **엔터티는 반드시 속성을 가지고 있다.**                    |
| **관계**          | - 엔터티는 다른 엔터티와 최소 한 개 이상 관계가 있어야 한다. - 엔터티의 관계 **→** **집합과 집합간의 관계** 예) 고객 엔터티에서 고객 계좌개설, 고객 회원등급 부여, 고객 배송지 주소 등등 |
| **업무**          | - 엔터티는 업무에서 관리되어야 하는 집합이다. 예) 고객, 계좌 |

####  **엔터티의 종류** 

| **종류**                                           | **설명**                                                     |
| -------------------------------------------------- | ------------------------------------------------------------ |
| **독립 엔티티** **[Kernel Entity, Master Entity]** | 사람, 물건, 장소 등과 같이 현실세계에 존재하는 엔터티        |
| **업무중심 엔터티** **[Transaction Entity]**       | Transaction이 실행되면서 발생하는 엔터티                     |
| **종속 엔터티** **[Dependent Entity]**             | 주로 1차 정규화로 인해 관련 중심엔티티로부터 분리된 엔터티   |
| **교차 엔티티** **[Intersaction Entity]**          | **M:M의 관계를 해소**하려는 목적으로 만들어진 엔터티 [ex> M:M -> 1:M] |

\1. 유형과 무형에 따른 엔터티 종류

   \* 유형과 무형으로 구분하는 기준은 물리적 형태의 존재 여부

| **종  류**      | **설  명**                                                   |
| --------------- | ------------------------------------------------------------ |
| **유형 엔터티** | 업무에서 도출되며 지속적으로 사용되는 Entity                 |
| **개념 엔터티** | 개념적으로 사용되는 Entity 유형 엔터티는 물리적 형태가 있지만, 개념 엔터니는 물리적 형태가 없다 |
| **사건 엔터티** | 비즈니스 프로세스를 실행하면서 생성되는 Entity               |

 \2. 발생시점에 따른 엔터티 종류

| **종  류**                          | **설  명**                                                   |
| ----------------------------------- | ------------------------------------------------------------ |
| **기본 엔터티** **[Basic Entity]**  | **다른 엔터티로부터 영향을 받지 않고 독립적으로 생성**되는 엔터티 **키 엔터티[Key Entity]**라고도 함 |
| **중심 엔터티** **[Main Entity]**   | 기본 엔터티와 행위 엔터티 간의 중간에 있는 엔터티 기본 엔터티로부터 발생되고 행위 엔터티를 생성하는 엔터티 |
| **행위 엔터티** **[Active Entity]** | **2개 이상의 엔터티로부터 발생**하는 엔터티 지속적으로 정보가 추가되고 변경되는 엔터티 |

 



\8. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a8)

 

해설 : **상품은 주문을 한 개 이상 반드시 가져야 하는 것이 아니라 안 가질 수도 있다.**

표기법 문제를 볼때 O 동그라미를 유의해서 보면 문제를 쉽게 풀수있습니다.

O = or (있을수도 있고 or 없을수도 있다.)

 



\9. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a9)

 

해설 : ERD 표기법 중 IE 표기법은 관계의 1:N 관계에서 N쪽에 새발을 표시하고 선택,

필수 참여관계에서 선택 참여(or)에 O, 필수 참여에 | 로 표시한다.

 



\10. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a10)

 

해설 : 같은학년은 입학 날짜가 모두 같게 생성되기 때문에 뒤에 같은 값이 붙음으로써 최소의 수가 아니므로 잘못된 모델링이다.

#### 식별자의 특징

1. 유일성 : 주식별자에 의해 엔터티내에 모든 인스턴스들이 유일하게 구분되어야 함
2. 최소성 : 주식별자를 구성하는 속성의 수는 유일성을 만족하는 최소의 수가 되어야 함
3. 불변성 : 지정된 주식별자 값은 자주 변하지 않는 것이어야 함
4. 존재성 : 주식별자가 지정이 되면 반드시 값이 들어와야 함(NOT NULL)

| **식별자 분류**         | **식별자**                                                   | **설명**                                                     |
| ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **대표성여부** ** **    | **주식별자**                                                 | - 엔터티 내에서 각 행을 구분할 수 있는 구분자이며, 타 엔터티와 참조관계를 연결할 수 있는 식별자 (ex. 사원번호, 고객번호) |
| **보조식별자**          | - 엔터티 내에서 각 행을 구분할 수 있는 구분자이나 대표성을 가지지 못해 참조관계 연결을 못함(ex. 주민등록번호) |                                                              |
| **스스로** **생성여부** | **내부식별자**                                               | - 엔터티 내부에서 스스로 만들어지는 식별자(ex. 고객번호)     |
| **외부식별자**          | - 타 엔터티와의 관계를 통해 타 엔터티로부터 받아오는 식별자(ex. 주문엔터티의 고객번호) |                                                              |
| **속성의 수**           | **단일식별자**                                               | - 하나의 속성으로 구성된 식별자(ex. 고객엔터티의 고객번호 )  |
| **복합식별자**          | - 둘 이상의 속성으로 구성된 식별자(ex. 주문상세엔터티의 주문번호+상세순번) |                                                              |
| **대체여부**            | **본질식별자**                                               | - 업무(비즈니스)에 의해 만들어지는 식별자(ex. 고객번호)      |
| **인조식별자**          | - 업무적으로 만들어지지는 않지만 원조식별자가 복잡한 구성을 가지고 있기 때문에 인위적으로 만든 식별자(ex. 주문엔터티의 주문번호(고객번호+주문번호+순번)) |                                                              |

 



\11. **정답 : \**4\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a11)

 

해설 : **Connect by 계층형 쿼리**는 데이터를 선택하여 계층적인 순서 그대로 리턴하는데 사용된다.

현재 행과 다른 행은 Prior라는 키워드를 통해 구별된다. 

Prior는 상위 행을 참조하는 것으로 문제에서는 "방금 전 행의 COL2 값이 현재 행의 COL1 값인 모든 행을 찾아라" 라는 의미이다.

```
CONNECT BY COL1 = PRIOR COL2;
```

WHERE 절에 COL3이 3인행은 제외. **→** COL3 이 4인것부터 시작***\*→ CONNECT BY COL1 = PRIOR COL2\**** 

**COL1(D)  COL2(B)     COL3(4)   \**→ 1개\****

 

**COL1(B) COL2(A)     COL3(2)   \**→ COL2(B)의 값과 같은 COL1(B) 1개\****

 

**COL1(A) COL2(NULL) COL3(1)    \**→ \*\*\*\*COL2(A)의 값과 같은 COL1(A) 1개\*\*\*\*\****

**COL1 중에 NULL 은 없으므로 종료**

***\**\*\*\*1 + 1 + 1 = 3개\*\*\*\*\****

 

**💡알아두기**

```
CONNECT BY PRIOR 자식 = 부모 (부모 → 자식) (순 ↓ 방향)
CONNECT BY PRIOR 부모 = 자식 (자식 → 부모) (역 ↑ 방향)

CONNECT BY 자식 = PRIOR 부모 (자식 → 부모) (역 ↑ 방향)
CONNECT BY 부모 = PRIOR 자식 (부모 → 자식) (순 ↓ 방향)
```

| **구분**              | **설명**                                                     |
| --------------------- | ------------------------------------------------------------ |
| **START WITH**        | 계층구조 전개의 시작 위치를 지정하는 구문, 루트 데이터를 지칭 |
| **CONNECT BY**        | 다음에 전개될 자식 데이터를 지정, 자식 데이터는 CONNECT BY 절에 주어진 조건을 만족해야함(JOIN) |
| **PRIOR**             | CONNECT BY 절에 사용되며 현재 읽은 칼럼을 지정               |
| **PRIOR 자식**        | 부모형태를 사용하면 계층구조에서 부모 -> 자식 방향으로 순방향 전개 |
| **PRIOR 부모**        | 자식 형태를 사용하면 자식 -> 부모 방향으로 역방향 전개       |
| **NOCYCLE**           | 데이터를 전개하면서 이미 나타났던 동일한 데이터가 전개중에 다시 나타나는 경우 CYCLE이 생성. CYCLE이 발생한 데이터는 런타임 오류를 방생시켜 NOCYCLE 구문을 통해 CYCLE이 발생하는 경우 이후 데이터 전개를 방지 |
| **ORDER SIBLINGS BY** | 형제노드(동일 LEVEL) 사이 데이터 정렬                        |
| **WHERE**             | 모든 전개를 수행한 뒤 지정조건을 통해 데이터 필터링          |

| **구분**          | **설명**                                                     |
| ----------------- | ------------------------------------------------------------ |
| CONNECT_BY_ROOT   | 계층형 쿼리에서 최상위 로우를 반환하는 연산자다. 연산자이므로 CONNECT_BY_ROOT 다음에는 표현식이 온다. |
| CONNECT_BY_ISLEAF | CONNECT BY 조건에 정의된 관계에 따라 해당 로우가 최하위 자식 로우이면 1을, 그렇지 않으면 0을 반환하는 의사 컬럼이다. |

 

 



\12. **정답 : \**3\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a12)

 

해설 : 대용량 데이터를 조인할 때 후행 테이블에 인덱스가 없으면 Nested Loop조인을 사용하면 안 된다. 물론 옵티마이저가 이런 경우에 자동으로 Nested Loop조인으로 실행하지 않고 Hash조인 혹은 Sort Merge, Full Scan을 사용한다.

| **방 법**                                                    | **설 명**                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **중첩 반복 조인** **(Nested Loop Join)**                    | - 좁은 범위에 유리 - 유리순차적으로 처리하며, Random Access 위주 - 후행(Driven) 테이블에는 조인을 위한 인덱스가 생성되어 있어야 함 - 실행속도 = 선행 테이블 사이즈 * 후행 테이블 접근횟수 |
| **색인된 중첩 반복 조인, 단일 반복 조인** **(Single Loop Join)** | - 후행(Driven) 테이블의 조인 속성에 인덱스가 존재할 경우 사용 - 선행 테이블의 각 레코드들에 대하여 후행 테이블의 인덱스 접근 구조를 사용하여 직접 검색 후 조인하는 방식 |
| **정렬 합병 조인** **(Sort Merge Join)**                     | - Sort Merge 조인은 해당 테이블의 인덱스가 없을때 수행이 된다. - 테이블을 정렬(Sort) 한 후에 정렬된 테이블을 병합(Merge) 하면서 조인을 실행한다. - 조인 연결고리의 비교 연산자가 범위 연산( >, < )인 경우 Nested Loop 조인보다 유리 - 두 결과집합의 크기가 차이가 많이 나는 경우에는 비효율적 |
| **해시 조인** **(Hash Join)**                                | - 해시(Hash)함수를 사용하여 두 테이블의 자료를 결합하는 조인 방식 - Nested Loop 조인과 Sort Merge 조인의 문제점을 해결 - 대용량 데이터 처리는 상당히 큰 hash area를 필요로 함으로, 메모리의 지나친 사용으로 오버헤드 발생 가능성 |

 



\13. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a13)

 

해설 : GRANT(권한부여), REVOKE(권한회수)

**DCL(Data Control Language) 데이터 제어어**

 



\14. **정답 : \**4\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a14)

 

해설 : RENAME은 DDL(Data Definition Language) 데이터정의어 에 속한다.

| **구분**                  | **종류**                                                     |
| ------------------------- | ------------------------------------------------------------ |
| **DDL (데이터 정의어)**   | CREATE, DROP, MODIFY(오라클), ALTER(SQL서버), RENAME, TRUNCATE |
| **DML (데이터 조작어)**   | SELECT, INSERT, DELETE, UPDATE                               |
| **DCL (데이터 제어어)**   | GRANT, REVOKE                                                |
| **TCL (트랜잭션 제어어)** | COMMIT, ROLLBACK, SAVE POINT                                 |

 



\15. **정답 : \**3\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a15)

 

해설 :BAN 칼럼으로 그룹핑하고 DISTINCT를 사용해서 중복된 이름을 제거하고 카운팅한다.

 



\16. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a16)

 

해설 : 보기 1번은 6개를 반환하고 나머지는 모두 4개를 반환한다.

NULLIF의 특징 : 두 개의 값이 같으면 NULL, 같지 않으면 첫 번째 값을 반환한다.

 

 



\17. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a17)

 

해설 :NULL은 비교에서 애초에 제외되어 IN() 연산자 안에 NULL이 있어도 비교연산을 수행하지 않는다.

주어진 테이블의 COL1 속성값 1, 2값을 갖는 행만 조회된다.

 




\18. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a18)

 

해설 : 조회결과값 순서를 나열하면

DNAME, JOB별 소계 **→** DNAME 별 소계 **→** JOB 별 소계 **→** 전체 집계 

모든 조합 가능한 소계와 집계가 조회 되었으므로 빈칸에 들어갈 그룹함수는 CUBE(DEPTNO, JOB) 입니다.

```
SQL> SELECT DNAME,JOB,SUM(SAL) FROM TEST18 GROUP BY CUBE(DNAME,JOB);   

DNAME		     JOB		    SUM(SAL)
-------------------- --------------------
					       45000
		     CLERK		       12000
		     MANAGER		       15000
		     PRESIDENT		       18000
SALES					       24000
SALES		     CLERK			7000
SALES		     MANAGER			8000
SALES		     PRESIDENT			9000
RESEARCH				       15000
RESEARCH	     CLERK			4000
RESEARCH	     MANAGER			5000
RESEARCH	     PRESIDENT			6000
ACCOUNTING					6000
ACCOUNTING	     CLERK			1000
ACCOUNTING	     MANAGER			2000
ACCOUNTING	     PRESIDENT			3000

16 rows selected.

SQL> SELECT DNAME,JOB,SUM(SAL) FROM TEST18 GROUP BY ROLLUP(DNAME,JOB); 

DNAME		     JOB		    SUM(SAL)
-------------------- --------------------
SALES		     CLERK			7000
SALES		     MANAGER			8000
SALES		     PRESIDENT			9000
SALES					       24000
RESEARCH	     CLERK			4000
RESEARCH	     MANAGER			5000
RESEARCH	     PRESIDENT			6000
RESEARCH				       15000
ACCOUNTING	     CLERK			1000
ACCOUNTING	     MANAGER			2000
ACCOUNTING	     PRESIDENT			3000
ACCOUNTING					6000
					       45000

13 rows selected.

SQL> SELECT DNAME,JOB,SUM(SAL) FROM TEST18 GROUP BY GROUPING SETS(DNAME,JOB);

DNAME		     JOB		    SUM(SAL)
-------------------- -------------------- ----------
ACCOUNTING					6000
RESEARCH				       15000
SALES					       24000
		     CLERK		       12000
		     PRESIDENT		       18000
		     MANAGER		       15000

6 rows selected.

SQL> SELECT DNAME,JOB,SUM(SAL) FROM TEST18 GROUP BY CUBE(DNAME);       
SELECT DNAME,JOB,SUM(SAL) FROM TEST18 GROUP BY CUBE(DNAME)
             *
ERROR at line 1:
ORA-00979: not a GROUP BY expression
```

 

4번 보기에 CUBE(DNAME) 이렇게 큐브를 작성하는건 의미가 없다.

| **구분**         | **설명**                                                     |
| ---------------- | ------------------------------------------------------------ |
| **ROLLUP**       | - 전체합계와 소그룹 간의 소계를 계산하는 ROLLUP 함수  예) GROUP BY ROLLUP (DEPTNO); → DEPTNO 합계(소계), 전체 합계를 조회 |
| **CUBE**         | - CUBE는 제시한 칼럼에 대해서 결합 가능한 모든 집계를 계산한다. - 다차원 집계를 제공하여 다양하게 데이터를 분석할 수 있다.  예) GROUP BY CUBE(DEPTNO, JOB); → DEPTNO 합계, JOB 합계, DEPTNO & JOB 합계, 전체 합계를 조회 **조합할 수 있는 모든 경우의 수가 조합된다. \*시스템에 부하를 많이 주는 단점이 있음** |
| **GROUPING SET** | - 원하는 부분의 소계만 손쉽게 추출하여 계산할 수 있는 GROUPING SETS 함수 |

 



\19. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a19)

 

해설 : C2 값으로 오름차순 정렬하고 CASE문으로 B, A, S 등급을 부여한다. 전체등급이 300점을 넘는 등급이 없기 때문에 S등급은 없고

100 이상인 C1의 6번만 A등급을 받는다.

 



\20. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a20)

 

해설 : 집계 함수에서 COUNT(*) 함수는 조건절이 거짓일 때 0을 반환한다.

 



\21. **정답 : \**4\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a21)

 

해설 : 똑같은게 두번 나와서 문법오류 이다. 



![img](https://blog.kakaocdn.net/dn/c25pmP/btrC7yleGIv/xAQkakLA7WkctVcK9etgRK/img.png)



 

\1) SUM(급여) OVER() : 전체 급여의 합계 / AVG(급여) OVER() : 평균 급여

\2) UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING → **시작부터 끝까지의 전체 합계**

```
2)
SUM(SAL) 
 OVER(PARTITION BY JOB 
          ORDER BY EMPNO RANGE
      BETWEEN UNBOUNDED PRECEDING
      AND UNBOUNDED FOLLOWING
      ) SAL1
      
[결과 예시]
SAL   SAL2
----------
10     60
20     60
30     60
```

\3) UNBOUNDED PRECEDING AND CURRENT ROW → **누적 합계**

```
3)
SUM(SAL)
 OVER(PARTITION BY JOB
          ORDER BY JOB RANGE
      BETWEEN UNBOUNDED PRECEDING
      AND CURRENT ROW
      ) SAL2


[결과 예시]
SAL   SAL2
----------
10     10
20     30
30     60
```

#### ✨**OVER절 이란 무엇인가?**

**[ OPEN ]**

#### ✨**WINDOW FUNCTION**

**[ OPEN ]**

#### ✨**WINDOW 절**

**[ OPEN ]**

 



\22. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a22)

 

해설 : PL/SQL은 절차형 언어로 PL/SQL 내부에서 테이블을 생성할 수 있다.

PL/SQL내부에서 테이블을 생성하는 이유는 임시 테이블로 잠깐 사용하기 위한 용도가 많다.

 

 



\23. **정답 : \**3\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a23)

 

해설 : CREATE INDEX [인덱스명] ON [테이블명] [칼럼명]

```
인덱스 생성 / 삭제 구문
-- 생성
  CREATE INDEX 인덱스명
  ON 테이블명 ( 속성명 , 속성명,…)
-- 삭제
  DROP INDEX 인덱스명
  ON 테이블명
  
-- 수정
인덱스 삭제 후 다시 만들어주는 방법을 사용해야 한다
 
-- 인덱스 조회
SELECT 테이블명, 인덱스명, 컬럼명
FROM ALL_IND_COLUMNS
WHERE TABLE_NAME = '테이블명'
```

 



\24. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a24)

 

해설 : ROLLBACK (이전 상태로 되돌리기) 이므로 TEST24의 COUNT(*) **→** 3개

```
SAVEPOINT [세이브포인트 명]

ROLLBACK TO [저장된 세이브포인트 명]

-- SAVEPOINT 로 저장하고 ROLLBACK TO 로 저장된 곳으로 돌아간다.
```

예) 게임할때 세이브포인트 저장후, 저장된 그 순간으로 되돌아감

 



\25. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a25)

 

해설 : MINUS (차집합) 1을 제외하게 되므로 2, 3이 출력된다.



![img](https://blog.kakaocdn.net/dn/uyAa1/btrC7yTPEdH/wo3TDK41CEe005SabjShe0/img.png)



 



\26. **정답 : \**3\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a26)

 

해설 : EXISTS(존재하는), NOT EXISTS(존재하지 않은) 이므로

CUSTOMERS 테이블에서 존재하지 않는 고객ID 식별을 위해서는 NOT EXISTS를 사용하고

WHERE절에 CUSTOMER.ID = ORDER.ID 를 사용해야 한다.

 



\27. **정답 : \**4\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a27)

 

해설 : <>(같지않은), ANY (**다수의 비교값 중 하나라도 만족하면 TRUE** ) 이므로 보기 4번은 모든 행이 출력된다.

 

**예) EMP 테이블에 DEPTNO(10, 20, 30) , DEPT 테이블에 DEPTNO(10, 20, 30, 40) 라는 데이터가 있다고 가정했을때**



![img](https://blog.kakaocdn.net/dn/pzBUg/btrC8TW1nnh/efVswVMYMXwKasJ2slG1Hk/img.png)보기 1번

![img](https://blog.kakaocdn.net/dn/cFf7L4/btrC6Hp1jUE/KCLmmT983hsZpB5E8B876K/img.png)보기 2번

![img](https://blog.kakaocdn.net/dn/sAwM6/btrC7AwYBD3/ecAQ92ga5sTaf81dbGSRj1/img.png)보기 3번

![img](https://blog.kakaocdn.net/dn/PqpgI/btrC9mklGP0/llP84CIBPFXzfOFbPh9VHk/img.png)보기 4번





 

\28. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a28)

 

해설 : 인덱스에 대해서 연산을 하면 인덱스가 변형이 되므로 인덱스를 사용할수가 없다.

 

 



\29. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a29)

 

해설 : 분산 데이터베이스는 네트워크를 통해서 여러개의 데이터베이스를 물리적으로 분리한 데이터베이스이다.

**분산 데이터베이스 장점과 단점**

| **장점**                                                     | **단점**                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 데이터베이스 신뢰성과 가용성이 높다.                         | 데이터베이스가 여러 네트워크를 통해서 분리되어 있기 때문에 관리와 통제가 어렵다. |
| 분산 데이터베이스가 병렬 처리를 수행하기 때문에 빠른 응답이 가능 | 보안관리가 어렵다.                                           |
| 분산 데이터베이스를 추가하여 시스템 용량 확장이 쉽다.        | 데이터 무결성 관리가 어렵다.                                 |
|                                                              | 데이터베이스 설계가 복잡함                                   |

 



\30. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a30)

 

해설 : 실행계획 (Execution Plan)

실행계획이란 SQL을 실행하기 위한 절차와 방법을 의미한다.

\- SQL개발자가 SQL을 작성하여 실행할 때, SQL을 어떻게 실행할 것인지를 계획하게 된다. 즉, SQL실행계획을 수립후 SQL을 실행한다.

\- 옵티마이저는 SQL의 실행계획을 수립하고 SQL을 실행하는 데이터베이스 관리 시스템의 소프트웨어이다.

```
SQL> SET AUTOTRACE ON;
SQL> SELECT*FROM TEST30;

DNAME		     JOB			 SAL
-------------------- -------------------- ----------
ACCOUNTING	     CLERK			1000
ACCOUNTING	     MANAGER			2000
ACCOUNTING	     PRESIDENT			3000
RESEARCH	     CLERK			4000
RESEARCH	     MANAGER			5000
RESEARCH	     PRESIDENT			6000
SALES		     CLERK			7000
SALES		     MANAGER			8000
SALES		     PRESIDENT			9000

9 rows selected.


Execution Plan -- 실행계획
----------------------------------------------------------
Plan hash value: 2195686282

----------------------------------------------------------------------------
| Id  | Operation	  | Name   | Rows  | Bytes | Cost (%CPU)| Time	   |
----------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |	   |	 9 |   333 |	 2   (0)| 00:00:01 |
|   1 |  TABLE ACCESS FULL| TEST30 |	 9 |   333 |	 2   (0)| 00:00:01 |
----------------------------------------------------------------------------

Note
-----
   - dynamic sampling used for this statement (level=2)


Statistics
----------------------------------------------------------
	  4  recursive calls
	  0  db block gets
	  8  consistent gets
	  0  physical reads
	  0  redo size
	921  bytes sent via SQL*Net to client
	519  bytes received via SQL*Net from client
	  2  SQL*Net roundtrips to/from client
	  0  sorts (memory)
	  0  sorts (disk)
	  9  rows processed
```

 



\31. **정답 : \**3\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a31)

 

해설 : 파티션 인덱스의 경우 파티션 키에 대해서 인덱스를 생성할 수 있고 파티션 키에 대해서 생성한 인덱스를 GLOBAL인덱스라고 한다.

파티션이라는것은 어떤 특정한 기준으로 분할하는것이다. (컬럼이 파티션 Key 가 된다.)

 



\32. **정답 : \**3\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a32)

 

해설 : 숫자와 NULL 을 더하면 NULL 이므로 0,  10 + 12 = 22

```
WHEN SUM (COL1 + COL2) IS NULL THEN 0
ELSE SUM (COL1 + COL2) 이므로 아래와 같다.

NULL + 10   = NULL → 0
12   + NULL = NULL → 0
NULL + NULL = NULL → 0
10   +  12  = 22
```

 



\33. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a33)

 

해설 : 2번은 데이터가 조회되지 않는다. 왜냐하면 ROWNUM은 논리적인 숫자이므로 "ROWNUM = 2" 와 같이 조회하면 찾을 수 없다.

```
[ 1번 RESULT ]
ENAME		  SAL
---------- ----------
조자룡           6000

[ 2번 RESULT ]
no rows selected

[ 3번 RESULT ]
ENAME		  SAL
---------- ----------
조자룡           6000
초선             5000
여포             4000
관우             3000
조조             2000
유비             1000

[ 4번 RESULT ]
ENAME		  SAL
---------- ----------
조자룡           6000
초선             5000
여포             4000
```

 



\34. **정답 : \**4\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a34)

 

해설 :

| **우선순위** | **연산자**                       |
| ------------ | -------------------------------- |
| **1**        | 산술 연산자(*, /, +, -)          |
| **2**        | 연결 연산자 (\|\|)               |
| **3**        | 비교 연산자(<, >, <=, =>, <>, =) |
| **4**        | IS NULL, LIKE, IN                |
| **5**        | BETWEEN                          |
| **6**        | NOT 연산자                       |
| **7**        | AND 연산자                       |
| **8**        | OR 연산자                        |

 



\35. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a35)

 

해설 : SELF JOIN은 동일한 테이블에서 발생하는 조인을 의미하며, FROM절에 동일한 테이블명이 두 번 이상 나타난다. 그리고 SELF JOIN을 하기 위해서 동일한 테이블을 두 번 이상 사용하므로 FROM절에 별칭(Alias)을 사용해야 한다.

```
[SELF JOIN]
SELECT A.칼럼명,
       B.칼럼명
   FROM 테이블1 A, 테이블2 B
   WHERE A.칼럼명2 = B.칼럼명1
```

 



\36. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a36)

 

해설 : SELECT * FROM [테이블명] WHERE LIKE [조건]

```
SQL> SELECT*FROM TEST36_1 A, TEST36_2 B WHERE A.ENAME LIKE B.CONDITION;

     EMPNO ENAME	      NO CONDITION
---------- ---------- ---------- ----------
      1000 조조                1 조%
      3000 조훈                1 조%
      2000 관우                2 %우%

-- 문제에서 COUNT(*) 이므로 

SQL> SELECT COUNT(*) ROWCNT FROM TEST36_1 A, TEST36_2 B WHERE A.ENAME LIKE B.CONDITION;

    ROWCNT
----------
	 3


--'조조'로 시작하는 이름 조회
WHERE B.CONDITION LIKE '조조%'

--'우'가 포함된 이름 조회
WHERE B.CONDITION LIKE '%우%'

--'조조'로 끝나는 사원의 이름 조회
WHERE B.CONDITION LIKE '%조조'
```

 

```
--A로 시작하는 문자를 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE 'A%'

--A로 끝나는 문자 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '%A'

--A를 포함하는 문자 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '%A%'

--A로 시작하는 두글자 문자 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE 'A_'

--첫번째 문자가 'A''가 아닌 모든 문자열 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE'[^A]'

--첫번째 문자가 'A'또는'B'또는'C'인 문자열 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '[ABC]'
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '[A-C]'
```

 



\37. **정답 : \**3\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a37)

 

해설 : COUNT에 컬럼을 주었을때 NULL값은 포함이 되지않으므로 (2,2,3)

```
SQL> SELECT COUNT(*) FROM TEST37;

  COUNT(*)
----------
	 4
→ 전체 행의 갯수를 반환할때는 NULL 포함     

SQL> SELECT COUNT(COL1) FROM TEST37;

COUNT(COL1)
-----------
	  2     
→ (컬럼명을 지정할경우 NULL 미포함)

SQL> SELECT*FROM TEST37 WHERE COL1 IN(12,10,NULL);

      COL1	 COL2
---------- ----------
	12
	10	   12
→ 2건

SQL> SELECT COL1, COUNT(*) FROM TEST37 GROUP BY COL1;

      COL1   COUNT(*)
---------- ----------
		    2
	12	    1
	10	    1
→ 3건
```



 

\38. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a38)

 

해설 : 테이블 B를 생성할때 "ON DELETE CASCADE" 옵션을 사용하고 A테이블의 행을 삭제하면 B 테이블의 행도 같이 삭제된다.

```
SQL> SELECT*FROM B;

	 A	    B
---------- ----------
	 1	    1
	 2	    2

SQL> DELETE FROM A WHERE A=1;

1 row deleted.

SQL> SELECT*FROM B;

	 A	    B
---------- ----------
	 2	    2
```

 



\39. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a39)

 

해설 :  GROUP BY COL1 → 조조(1개),유비(2개),관우(3개),여포(1개),초선(1개)

→ HAVING COUNT(*) > 2  이므로 갯수가 2개 이상인 관우의 갯수 → 3

 



\40. **정답 : \**4\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a40)

 

해설 : DISTINCT (중복제거) 

```
COL1   COL2
-----------
조조     1
조조     2
조조     3


COUNT(COL1)  COUNT(COL2)
------------------------
    3            3
```

 



\41. **정답 : \**2\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a41)

 

해설 : CHAR는 고정길이 문자열을 의미한다.

DOUBLE 이 DECIMAL 에 비해 비교할 수 없이 크지만, 소수점을 표현하는 것에는 DECIMAL 이 더 정밀하다.

숫자의 정밀한 표현과 금융관련 계산과 같은 부분에 사용 된다.

 

**DECIMAL(m, d) : \**M의 최대값은 65, D는 소수 자릿수이며 0이면 소수점 가지지 않음\****

```
mysql> CREATE TABLE T1(NUM DECIMAL(65,30));
Query OK, 0 rows affected (0.00 sec)

mysql> INSERT INTO T1 VALUES(123.123);
Query OK, 1 row affected (0.00 sec)

mysql> SELECT*FROM T1;
+------------------------------------+
| NUM                                |
+------------------------------------+
| 123.123000000000000000000000000000 |
+------------------------------------+
1 row in set (0.00 sec)
```

 

 



\42. **정답 : \**4\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a42)

 

해설 : **ORDER BY 가 항상 마지막에 실행된다.**

 

1️⃣FROM 절에서 테이블의 목록을 가져온다.

2️⃣WHERE 절에서 검색 조건에 일치하지않는 행을 제외한다.

3️⃣GROUP BY 절에 명시된 행의 값을 그룹화 한다.

4️⃣HAVING 절은 GROUP BY 절로 그룹화된 데이터를 대상으로 조건을 정의한다.

5️⃣SELECT 절에서 명시한 칼럼값들을 조회한다.

6️⃣ORDER BY 절에서 명시한 칼럼값을 기준으로 정렬한후 출력

 

 



\43. **정답 : 2**

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a43)

 

해설 : 순수 관계 연산자란, 관계형 데이터베이스에 적용할 수 있도록 개발한 관계 연산자를 의미한다. DELETE는 포함되지 않는다.

**순수 관계 연산자**

| **연산자**         | **특징**                                                     |
| ------------------ | ------------------------------------------------------------ |
| **SELECT ( σ )**   | · 릴레이션에 존재하는 튜플 중에서 선택 조건을 만족하는 튜플의 부분집합을 구하여 새로운 릴레이션을 만듦 · 릴레이션의 행(가로)에 해당하는 튜플을 구하는 것이므로 수평 연산이라고도 함 · 연산자의 기호는 그리스 문자 시그마(σ)를 사용함 |
| **PROJECT ( π )**  | · 주어진 릴레이션에서 속성 List에 제시된 Attribute만을 추출하는 연산 · 릴레이션의 열(세로)에 해당하는 Attribute를 추출하는 것이므로 수직 연산자라고도 함 · 연산자의 기호는 그리스 문자 파이(π)를 사용함 |
| **JOIN ( ⋈ )**     | · 공통 속성을 중심으로 2개의 릴레이션을 하나로 합쳐서 새로운 릴레이션을 만드는 연산 · 연산자의 기호는 ⋈를 사용함 · 조인 조건이 '='일 때 동일한 속성이 두 번 나타나게 되는데, 이 중 중복된 속성을 제거하여 같은 속성을 한 번만 표기하는 방법을 자연(NATURAL) 조인이라고 함 |
| **DIVISION ( ÷ )** | · X ⊃ Y인 2개의 릴레이션에서 R(X)와 S(Y)가 있을 때, R의 속성이 S의 속성값을 모두 가진 튜플에서 S가 가진 속성을 제외한 속성만을 구하는 연산 |



 

***\*- - - - - - - - 주관식 - - - - - - - -\****

 

\44. **정답 : \**ROW_NUMBER()\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a44)

 

해설 : ROW_NUMBER() : 중복값이 있어도 고유 등수 부여(1위, 2위, 3위, 4위)

RANK() : 중복값은 중복등수, **등수 건너뜀**(1위, 1위, 3위, 4위)

DENSE_RANK() : 중복값은 중복등수, 등수 안 건너뜀(1위, 1위, 2위, 2위) ***동일 등수 순위에 영향이 없다.**

 



\45. **정답 : \**INTO TEAM_EMP\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a45)

 

해설 : SELECT * INTO 새로만들테이블명 FROM 복사할테이블명

```
[오라클]
<테이블 복사할 때>
CREATE TABLE 새로만들테이블명 AS
SELECT * FROM 복사할테이블명 [WHERE 절]

<테이블 구조만 복사할 때>
CREATE TABLE 새로만들테이블명 AS
SELECT * FROM 복사할테이블명 WHERE 1=2 [where에다가 참이 아닌 조건을 넣어줌]

<테이블은 이미 생성되어 있고 데이터만 복사할 때>
INSERT INTO 복사할테이블명 SELECT * FROM 복사할테이블명 [WHERE 절]

<테이블 이름 변경>
ALTER TABLE 구테이블명 RENAME TO 신테이블명

[SQL server]
<테이블 복사할 때>
SELECT * INTO 새로만들테이블명 FROM 복사할테이블명
```

 



\46. **정답 : \**(COL1, COL2),(COL1),()\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a46)

 

해설 : ROLLUP은 그룹된 칼럼의 SUBTOTAL을 생성하기 위해서 사용된다.

그룹의 수가 N개 일때 N+1개의 SUBTOTAL이 생성된다. 

GROUPING SETS은 여러 그룹질의를 UNION ALL(합집합)과 같은 결과를 만들어서 소계, 합계를 집계할 수 있다.

 

| **GROUPING SETS 함수**                    | **GROUP BY UNION ALL절**                                     |
| ----------------------------------------- | ------------------------------------------------------------ |
| **group by grouping sets(a,b,c)**         | group by a union all  group by union all  group by c         |
| **group by grouping sets(a,b,(b,c))**     | group by a union all group by b union all group by b,c       |
| **group by grouping sets((a,b,c))**       | group by a,b,c                                               |
| **group by grouping sets(a,rollup(b,c))** | group by a union all group by rollup(b,c)                    |
| **group by rollup(a,b,c)**                | group by (a,b,c) union all group by (a,b)union all group by (a) union all group by () |
| **group by cube(a,b,c)**                  | group by (a,b,c) union all group by (a,b) union all group by (a,c) union all group by (b,c) union all group by (a) union all group by (b) union all group by (c) union all group by () |

 



\47. **정답 : \**1\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a47)

 

해설 : COMMIT 시점으로 ROLLBACK(되돌아가기) 하였으므로 출력값은 1

 



\48. **정답 : \**24\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a48)

 

해설 : NVL(COL2,0) , COL2 이 NULL이면 0으로 대체되고 평균이 계산된다.

 



\49. **정답 : \**16\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a49)

 

해설 : **WHERE 절에 A.COL1 <> B.COL1 이므로 A.COL1 컬럼을 기준으로 다른수의 갯수를 카운트한다.**

```
SQL> SELECT COUNT(*) FROM TEST49 A, TEST49_2 B WHERE A.COL1 <> B.COL1;

  COUNT(*)
----------
	16
```



![img](https://blog.kakaocdn.net/dn/thIWI/btrDaUQfDSC/UMAmoMXGCBfNk1cIGqUbJ0/img.png)



 

 



\50. **정답 : \**CROSS JOIN\****

📖[문제확인](https://yunamom.tistory.com/269?category=1055509#a50)

 

해설 : **CROSS JOIN의 결과 개수는 두 테이블의 행의 개수를 곱한 개수가 된다.**

**CROSS JOIN**은 **상호 조인**이라고도 불리며, **한 쪽 테이블의 모든 행들과 다른 테이블의 모든 행을 조인**시키는 기능을 한다.

이러한 CROSS JOIN을 카테시안 곱 (Cartesian Product)라고도 한다.

```
SQL> SELECT COUNT(*) FROM TEST49 CROSS JOIN TEST49;

  COUNT(*)
----------
	25
```

 