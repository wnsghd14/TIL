**1. 데이터 모델링 시 유의점으로 적절하지 않은 것은? (자격 검정 3번과 유사)**

정답→ 성능을 위한 반정규화를 고려한다. (유의점으로 적절하지 않습니다.)

| **구분**     | **설명**                                                     |
| ------------ | ------------------------------------------------------------ |
| **중복**     | 데이터 모델은 같은 데이터를 사용하는 사람, 시간 그리고 장소를 파악하는데 도움을 준다 이러한 지식응용은 데이터베이스가 여러 장소에 같은 정보를 저장하는 잘못을 하지 않도록 한다. |
| **비유연성** | 데이터 모델을 어떻게 설계했느냐에 따라 사소한 업무변화에도 데이터 모델이 수시로 변경됨으로써 유지보수의 어려움을 가중시킬 수 있다. |
| **비일관성** | 데이터의 중복이 없더라도 비일관성은 발생한다. 데이터 모델링을 할 때 데이터와 데이터간 상호 연관 관계에 대한 명확한 정의는 이러한 위험을 사전에 예방할 수 있도록 해준다. |

 

 

**2. 아래의 설명 중 속성에 대한 설명이 가장 적절하지 않은 것은? (자격 검정 문제 16번)**

```
[설명]
우리은행은 예금분류(일반예금, 특별예금 등)의 원금, 예치기간, 이자율을 관리할 필요가 있다.
또한 원금에 대한 이자율을 적용하여 계산된 이자에 대해서도 속성으로 관리하고자 한다.
예를 들어 원금이 1000원이고 예치기간이 5개월이며 이자율이 5.0%라는 속성을 관리하고 계산된 이자도 관리한다.
일반예금이나 특별예금 등에 대해서는 코드를 부여(예: 01-일반예금, 02-특별예금 등)하여 관리한다.
```

1) 일반예금은 코드 엔터티를 별도로 구분하고 값에는 코드값만 포함한다.  2) 원금, 예치기간은 기본(BASIC) 속성이다.  3) 이자와 이자율은 파생(DERIVED) 속성이다.  4) 예금분류는 설계(DESIGNED) 속성이다.

정답→ 3️⃣이자, 이자율은 파생 속성이다.(**이자율은 정의되는 값으로 파생속성이 아니다**.)

| **문제 해설**                                                |
| ------------------------------------------------------------ |
| 파생속성은 다른 속성에 영향을 받아 발생하는 속성으로, 보통 계산된 값들이 이에 해당된다. |
| 이자는 이자율과 원금등에 의해 계산이 되는 파생속성, 이자율은 계산이 되는 속성이 아닌 정의되는 값으로 파생속성이 아니다. |

 

**3. 인스턴스에 대한 설명 중 가장 적절하지 않은 것은?**

 

정답→ 인스턴스는 속성이 없을 수도 있다.

해설 : 인스턴스는 속성이 없으면 존재할수 없다. (아래 표 참고)

![img](https://blog.kakaocdn.net/dn/cW9hNz/btrDnp9C7V5/GioJssEzHfdsJFHumOuuLk/img.png)by yunamom

 

**4. 아래의 ERD에 대한 설명 중 적절하지 않은 것은? (자격 검정 문제 7번과 유사)**

![img](https://blog.kakaocdn.net/dn/GZdCv/btrDj1al2Bf/YdjB86u4Px9uSHhvTboUJ1/img.png)문제 예시

 

정답→ 주문은 고객이 없을 수도 있다. 

해설 : 주문은 반드시 고객이 있어야 한다. (아래 관계차수표 참고)

![img](https://blog.kakaocdn.net/dn/rQJRG/btrDrQrmtaX/289iritX1vkdNC8UkKNpKk/img.png)

 

**5. 부모엔터티로부터 속성을 받았지만 자식엔터티의 주식별자로 사용하지 않고 일반적인 속성으로만 사용하는 경우로 가장 적절하지 않은 것은?**

 

정답→ Data Life Cycle이 같을 때.

해설 : 

| **문제 해설**                                                |
| ------------------------------------------------------------ |
| 자식 엔터티에서 받은 속성이 반드시 필수가 아니어도 무방하기 때문에 부모 없는 자식이 생성될 수 있는 경우이다. |
| 엔터티별로 **데이터의 생명주기(Data Life Cycle)를 다르게 관리할 경우**이다. |
| 여러 개의 엔터티가 하나의 엔터티로 통합되어 표현되었는데, 각각의 엔터티가 별도의 관계를 가질 때 이에 해당된다. |
| 자식엔터티에 주식별자로 사용하여도 되지만 자식엔터티에서 별도의 주식별자를 생성하는 것이 더 유리하다고 판단될 때 |

 

**6. 모델링의 단계 중 가장 재사용성이 높은 모델링은?**

 

정답→ 논리적 데이터 모델링

 

해설 : 논리적 시스템으로 구축하고자 하는 업무에 대해 Key, 속성, 관계 등을 정확하게 표현, 재사용성이 높음

 

**7. 아래의 내용 중 파생 속성으로만 선택된 것으로 적절한 것은?**

정답→ 4️⃣ 최초주문일자, 주문금액, 총주문금액 

 

해설 : 파생속성은 타 속성에 의해 영향을받아 자신의 값이 변한다.(주문수량, 총주문금액 등)

 

**8. 다음 중 엔터티간의 관계에서 1:1, 1:M과 같이 관계의 기수성을 나타내는것으로 가장 적절한 것은?**

 

1) 관계명(Relationship Membership)  2) 관계차수(Relationship Degree/Cardinality)  3) 관계선택사양(Relationship Optionality)  4) 관계정의(Relationship Definition)

정답→ 관계차수 (Cardinality)

 

**단답형 1. 업무에서 필요로 하는 인스턴스로 관리하고자 하는 의미상 더 이상 분리 되지 않는 최소의 데이터 단위는?(자격 검정 14번)**

 

정답→ 속성

 

**단답형 2. 기본키가 아닌 모든 속성이 기본키에 완전 함수 종속된 상태를 무엇이라 하는가?**

 

정답→ 제2정규형



**9. 테이블에 값을 입력하는 명령어**

정답→Insert

해설 :

 

**10. 다음중 결과값이 다른 하나를 고르시오.**

1) CEIL(22.14)    2) FLOOR(22.14)  3) TRUNC(22.14)  4) ROUND(22.14)

정답→1번 Ceil

해설 : Ceil (정수올림), Floor(정수내림), Trunc(소수점버리기), Round(반올림) ←5이상을 올림 

```
SQL> SELECT CEIL(22.14), FLOOR(22.14), TRUNC(22.14), ROUND(22.14) FROM DUAL;

CEIL(22.14) FLOOR(22.14) TRUNC(22.14) ROUND(22.14)
----------- ------------ ------------ ------------
	 23	      22	   22		22
```

 

**11. \**손흥민이 포함된 팀의 포지션을 'FW' 로 변경하는 SQL문으로 올바른것은?\****

정답→4️⃣

해설 :

 

 

**12. SNS 별 추천점수 추출하는 함수**

정답→3️⃣

해설 :

 

**13. \**데이터 무결성을 지키기 위한 것과 관계 없는 것을 고르시오.\****

1) 애플리케이션의 로직  2) Trigger  3) Lock  4) Constraints

정답→3️⃣

해설 : Lock/Unlock은 병행성 제어(동시성) 기법이다.

무결성 : 데이터 임의 갱신으로부터 보호해야 하는 것.

제약조건을 넣어서 무결성을 보장하거나, Triger 로직 안에 검사 기능을 넣을 수도 있고, 개발자의 코딩에서 로직을 넣을 수도 있다.

 

 

**14. 다음 중 아래와 같은 집합이 존재 할 때, 집합 A와 B에 대하여 집합연산을 수행한 결과 집합 C가 되는 경우 이용되는 데이터베이스 집합연산은?**

```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {3, 4}
```

1) Union  2) Difference  3) Intersection  4) Product

정답→3️⃣ Intersection(교집합)

해설 :

 

**15. CTAS 특징에 맞지 않는것을 고르시오. ( 테이블 복사 )**

정답→2️⃣ 모든 제약조건을 다 가져올수있다.

해설 : NOT NULL조건만 가져올수 있다.

 

**16. 가장 첫번째값을 반환하는 함수**

정답→1️⃣ First value

해설 :

 

**17. 9명 이상이 있는 직급 중에 나이가 제일 많은사람 고르기**

정답→ count 9 >= group by 직급

해설 :

 

**18. 다음중 수행이 되는 보기만을 고른것은 ?**

```
INSERT 1 ...
SAVEPOINT A
INSERT 2 ...
DELETE 3 ...
ROLLBACK SAVEPOINT A
INSERT 4 ...
INSERT 5 ...
COMMIT;
```

정답→4️⃣ (1, 4, 5)

해설 : 롤백 전값은 다 회수된다.

 

**19. ROLLUP, CUBE, GROUPING SETS 함수를 칭하는것은?**

정답→3️⃣ Grouping

해설 : 

 

**20. SUBSTR 결과가 다른것을 고르시오**

1) SELECT SUBSTR('DATABASE',7)FROM DUAL;  2) SELECT SUBSTR('DATABASE',-2)FROM DUAL;  3) SELECT SUBSTR('DATABASE',8,-2)FROM DUAL;  4) SELECT SUBSTR('DATABASE',INSTR('DATABASE','S'),2)FROM DUAL;

정답→3️⃣

해설 : 3번은 음수를 반환하게 되므로 X

```
SQL> SELECT SUBSTR('DATABASE',7)FROM DUAL;

SU
--
SE

SQL> SELECT SUBSTR('DATABASE',-2)FROM DUAL;

SU
--
SE

SQL> SELECT SUBSTR('DATABASE',8,-2)FROM DUAL;

S
-

SQL> SELECT SUBSTR('DATABASE',INSTR('DATABASE','S'),2)FROM DUAL;

SU
--
SE
```

 

**21. 아래 테이블 및 결과가 있을 때 SQL수행으로 올바른 것은? (WHERE 절의 NOT EXISTS 안의 서브쿼리 조건의 NULL 처리 문제)**

```
[table1]
COL1   COL2
-----------
1      10
2      20
3      30

[table2]
COL1   COL2
------------
1       10
2       20

[RESULT]
COL1
----
3
```

정답→ WHERE **NOT EXISTS** (SELECT 1 FROM T2 B WHERE **B.COL1 = A.COL1**)

해설 :

```
SELECT COL1 FROM T1 A WHERE NOT EXISTS(SELECT 1 FROM T2 B WHERE B.COL1 = A.COL1);

COL1
----
3
```

 

**22. 테이블의 개수가 5개일 때 최소 조인 개수는 몇개인가?**

정답→ 4개

해설 : 최소 조인 개수 (N-1)

 

**23. 아래의 결과를 출력하는 SQL을 완성하는 GROUP BY(   )로 적절하지 않은 것은?**

```
A 집계, A+B 집계 의 결과
```

정답→ ROLLUP(A,B) = GROUP BY(A,B) UNION ALL GROUP BY (A) UNION ALL GROUP BY ()

해설 : 나머지는 전체 집계가 포함되어 있지 않음

 

 

**24. 아래의 SQL결과가 다른 것을 고르시오.(FULL OUTER JOIN의 변환 형태에 대한 문제)**

```
1) SELECT * FROM A FULL OUTER JOIN B
2) FULL JOIN
3) LEFT OUTER JOIN UNION RIGHT OUTER JOIN
4) LEFT OUTER JOIN UNION ALL RIGHT OUTER JOIN
```

정답→4️⃣

해설 : FULL OUTER JOIN 은 LEFT UNION RIGHT , UNION ALL 은 중복제거 없이 전체출력되므로 다르다.

 

**25. 주문 테이블의 특정 기간 고객의 주문금액을 현재 고객테이블에 있는 고객 데이터만으로 추려내어 전체기간의 주문금액 합인지, 동일 기간의 주문 금액 합인지를 구하는 문제 (어려웠던 문제...SQL문이 엄청길었음)**

정답→4️⃣

해설 : 정답은 4번이라고 함

 

**26. 아래의 테이블에 대한 INSERT 구문 수행시 에러가 발생하지 않는 것을 고르시오.**

```
CREATE TABLE T1(
C1 PRIMARY KEY,
C2 NOT NULL,
C3 UNIQUE,
C4 CHECK (NOT NULL));

1)INSERT INTO T1 VALUES(NULL, 1, 2, 3);
2)INSERT INTO T1 VALUES(1, NULL, 2, 3);
3)INSERT INTO T1 VALUES(1, 2, NULL, 3);
4)INSERT INTO T1 VALUES(1, 2, 3, NULL);
```

정답→3️⃣

해설 : UNIQUE 에는 NULL이 허용된다.

 

**27. 아래의 테이블에 대한 SQL 결과는? (AVG 함수에서 NULL 개수 포함 여부 문제)**

```
[table]
C1
----
10
20
NULL

SELECT AVG(NVL(C1,0)) FROM table;
```

정답→ 10

해설 : NULL이 0으로 변경되어 AVG 의 모수로 포함된다.

 

**28. TABLE1, TABLE2, TABLE3 테이블에 대한 아래의 INSERT 결과 개수로 알맞은 것은?**

**(다중 TABLE INSERT FIRST)**

```
[TABLE0]
N1
---
1
2
5

INSERT FIRST
       WHEN N1 >= 2 THEN INTO TABLE1(N1) VALUES(N1)
       WHEN N1 >= 3 THEN INTO TABLE2(N1) VALUES(N1)
       ELSE INTO TABLE3 VALUES(N1)
SELECT N1 FROM TABLE0;
```

정답→(2,0,1) 

해설 : 가장 위의 WHEN 조건을 만족하면 밑의 조건을 체크하지 않으므로 2,0,1

```
SQL> INSERT FIRST WHEN N1 >= 2 THEN INTO TABLE1(N1) VALUES(N1) WHEN N1 >= 3 THEN INTO TABLE2(N1) VALUES(N1) ELSE INTO TABLE3 VALUES(N1) SELECT N1 FROM TABLE0;

3 rows created.

SQL> SELECT COUNT(*) FROM TABLE1;

  COUNT(*)
----------
	 2

SQL> SELECT COUNT(*) FROM TABLE2;

  COUNT(*)
----------
	 0

SQL> SELECT COUNt(*) FROM TABLE3;

  COUNT(*)
----------
	 1
```

 

**29. 아래와 같은 SQL 결과로 올바른 것은?**

**(OUTER JOIN과 INNER JOIN이 사용될 경우 연결된 조인에서 INNER JOIN 이 마지막에 사용 될 때)**

```
SELECT * FROM
       T1, T2, T3, T4
       WHERE T2.COL1(+) = T1.COL1
       AND T3.COL1(+) = T2.COL1
       AND T4.COL1 = T3.COL1;
```

정답→ 1 

해설 : LEFT - LEFT - INNER JOIN으로 연결되는 경우 결국 INNER JOIN의 결과만이 남는다. 공통으로 가진 값이 1이므로 1건만 남음

 

**30. 아래의 SQL에서 1건만 출력되는 SQL이 아닌것을 고르시오.**

1) ROWNUM = 1  2) ROWNUM < 2  3) ROWNUM <= 2  4) ROWNUM <= 2-1

정답→ ROWNUM <= 2

해설 : ROWNUM <= 2 (2건 출력)

 

**31. 아래 SQL 수행 결과로 올바른 것은? (WHERE 절 NOT IN 안의 서브쿼리 값이 NULL을 포함할 때의 결과)**

```
SELECT ... FROM table1 A 
      WHERE A.N1 
      NOT IN(SELECT B.N1 FROM table3 B);
      
-- select 뒤 불확실
```

정답→결과없음 (0 ROWS) or 0

해설 : NOT IN (SUBQUERY) 에서 NULL이 포함된 경우 NULL의 참 거짓 판정이 되지 않아 0건 처리

```
table3 에 null 값을 넣고 아래와 같이 실행해보았는데 문제에 count(*) 였는지 정확히 기억안남 ㅠㅠ

SQL> select count(*) from table1 A where A.N1 NOT IN(select B.N1 from table3 b);

  COUNT(*)
----------
	 0

SQL> select count(N1) from table1 A where A.N1 NOT IN(select B.N1 from table3 b);

 COUNT(N1)
----------
	 0

SQL> select N1 from table1 A where A.N1 NOT IN(select B.N1 from table3 b);

no rows selected
```

 

**32. 아래의 보기중 수정 전후가 다른 하나를 고르시오. (SUM내부의 NVL과 외부의 NVL의 차이 문제)**

정답→SUM (NVL(COL1) + NVL(COL2)) > NVL(SUM(COL1 + COL2))

해설 : COL1 + COL2 에서 둘중 하나의 값이 NULL 이면 NULL이 되어 값이 달라진다.

 

**33. 아래의 SQL결과 중 다른 것을 고르시오.**

**(OR 조건과 UNION ALL 변환에서 OR 조건에서 사용된 컬럼이 다를 경우의 결과 문제)**

```
[TABLE1]
COL1   COL2
-----------
A      a
B      b
C      c


1) SELECT COL1 FROM TABLE1 WHERE COL1 IN ('A','B') OR COL2 <> 'c';
2) SELECT COL1 FROM TABLE1 WHERE COL1 IN ('A','B')
   UNION ALL
   SELECT COL1 FROM TABLE1 WHERE COL2 <> 'c';
3) SELECT COL1 FROM TABLE1 WHERE COL1 IN ('A','B')
   UNION
   SELECT COL1 FROM TABLE1 WHERE COL2 <> 'c';
4) SELECT COL1 FROM TABLE1 WHERE COL1 = 'A' OR COL1 = 'B' OR COL2 <> 'c';
```

정답→2️⃣ 

해설 : UNION ALL 로 인해 ABAB로 값이 출력됨

 

 

***\*34. 아래의 SQL중 결과가 다른 것은? ( OR, IN, AND 의 변형에 대한 문제)\****

```
1)SELECT*FROM SQLD49 WHERE V1 = 'A' AND V2 IN ('T1','T2','T3');

2)SELECT*FROM SQLD49 WHERE V1 = 'A' AND V2='T1' OR V2='T2' OR V2='T3';

3)SELECT*FROM SQLD49 WHERE (V1,V2) IN (('A','T1'),('A','T2'),('A','T3'));

4)SELECT*FROM SQLD49 WHERE V1 = 'A' AND (V2 = 'T1' OR V2 = 'T2' OR V2 = 'T3');
```

정답→2️⃣

해설 : OR 을 기준으로 모두 출력된다. ( 4번같은경우는 괄호로 묶어져있어서 다름)

```
SELECT*FROM SQLD49 WHERE V1 = 'A' AND V2 IN ('T1','T2','T3');

N1  V1   V2
-----------
1   A    T1


SQL> SELECT*FROM SQLD49 WHERE V1 = 'A' AND V2='T1' OR V2='T2' OR V2='T3';

N1  V1   V2
-----------
1   A    T1
2   B    T2
3        T3


SQL> SELECT*FROM SQLD49 WHERE (V1,V2) IN (('A','T1'),('A','T2'),('A','T3'));

N1  V1   V2
-----------
1   A    T1

SQL> SELECT*FROM SQLD49 WHERE V1 = 'A' AND (V2 = 'T1' OR V2 = 'T2' OR V2 = 'T3');

N1  V1   V2
-----------
1   A    T1
```

 

**35. 특정 과목의 학점이 4.0 이상인 학생의 이름을 구하는 SQL로 올바른것을고르시오**

**(집계 쿼리에서 SELECT 절에 사용되는 컬럼은 GROUP BY 에 사용되어야 함을 묻는 문제)**

```
수강 정보
-------
학번
과목
학점

학생
----
이름
학번

과목
----
과목명
...
```

정답→ SELECT 이름 FROM .... GROUP BY 학번, 이름 HAVING MAX(학점) > 4 

해설 : SELECT 에 이름이 나오므로 GROUP BY 에 이름이 나와야 함

(그룹의 기준을 이름으로 할 경우 유일값이 아니므로 학번-이름으로 묶어야만 유일값의 학점을 구할 수 있다.)

 

**36. 아래의 SQL의 결과로 알맞은 것은? (WHERE 1=2 문제)**

```
SELECT .... FROM SQLD WHERE 1 = 2;

-- SELECT 뒤의 값이 정확하지 않음
```

정답→결과값이 없음 (커뮤니티에서 이게 답이라고 함)

해설 : 문제 보기가 정확히 기억나지 않음 

```
SQL> SELECT N1 FROM SQLD WHERE 1=2;

no rows selected

SQL> SELECT COUNT(N1) FROM SQLD WHERE 1=2;

 COUNT(N1)
----------
	 0
```

 

**37. WHERE 절에 사용된 서브쿼리에 대한 설명으로 적절하지 않은 것은?**

**( 메인쿼리와 서브쿼리중 WHERE 절에 사용된 서브쿼리에대한 내용을 묻는 문제)**

정답→ 메인쿼리 ... 서브쿼리가 있을때 결과는 항상 서브쿼리를 따른다.

해설 : FROM 절에 사용된 서브쿼리(INLINE VIEW) 가 아니라면 메인 쿼리의 결과에 영향을 주지 못한다.

 

**38. 아래의 SQL 결과로 올바른 것은?**

**(LEFT OUTER JOIN에서 ON절에 사용된 조건절과 WHERE 절에 사용된 조건절의 FILTERING에 관한 문제)**

정답→ 1건

해설 : ON 절의 조건절을 우선적으로 FILTERING 하고 그 결과를 조인함





**단답형 3. 아래 SQL1 과 같은 결과가 나오도록 SQL2 빈칸을 작성하시오.**

```
[SQL1]
SELECT*FROM A, B;

[SQL2]
SELECT*FROM A (     ) B;
```

정답→CROSS JOIN

해설 :

 

**단답형 4. 아래의 계층형 쿼리 결과에서 C3의 2번째 값을 작성하시오.**

```
[SQLD44]

C1  C2   C3
------------
 1 NULL  A
 2  1    B
 3  1    C
 4  2    D

[SQL]

SELECT C1, C2, C3
FROM SQLD44
     CONNECT BY PRIOR C1 = C2
           START WITH C1 = 1
     ORDER SIBLINGS BY C1 DESC;
```

정답→C

해설 : C1 이 같은 레벨에서 DESC 로 정렬됨 

```
[RESULT]
 C1  C2   C3
-------------
 1        A
 3   1    C
 2   1    B
 4   2    D
```

 

**단답형 5. 아래의 계층형 쿼리 결과를 작성하시오.**

```
[SQLD45]

 C1  C2  C3
-------------- 
 1       KING
 2   1   JOHN
 3   2   SCOTT

[SQL]
SELECT C3 FROM SQLD45
   WHERE C1 <> 2
   CONNECT BY C1 = PRIOR C2
   START WITH C1 = 2;
```

정답→KING

해설 : C1 = PRIOR C2  역방향

```
SQL> SELECT C3 FROM SQLD45 WHERE C1 <> 2 CONNECT BY C1 = PRIOR C2 START WITH C1 = 2;

C3
-----
KING
```

 

**단답형 6. GRANT, REVOKE 등의 SQL 을 무엇이라 하는가?**

정답→DCL

해설 :

 

**단답형 7. 아래의 SQL결과의 빈칸을 작성하시오. (NTILE 문제)**

```
[SQL]

[RESULT]

COL1    COL2
------------
A      (   )
B        3
C      (   )
```

정답→3, 2

해설 :

```
총 8개의 로우에서 NTILE(3) 으로 개수는 3, 3, 2
```

 

**단답형 8. 아래 SQL의 빈칸을 작성하시오.**

```
[SQLD48]

V1	    N1
----------------
A	    100
B	    150
C	   1400
D	    450
E	     50

[SQL]

SELECT V1, N1,
  COUNT(N1) OVER 
            (ORDER BY N1 RANGE 
            BETWEEN 0 PRECEDING 
            AND
            50 FOLLOWING) AS CNT 
FROM SQLD48;
```

정답→RANGE

해설 : 값의 +0 ~ +50 사이의 COUNT 결과로 나타남

```
SQL> SELECT V1, N1, COUNT(N1) OVER (ORDER BY N1 RANGE BETWEEN 0 PRECEDING AND 50 FOLLOWING) AS CNT FROM SQLD48;

V1    N1    CNT
-----------------
E     50     2
A     100    2
B     150    1
D     450    1
C    1400    1
```

ROW : 데이터의 값을 더함

RANGE : 데이터의 범위를 나타냄

 

**단답형 9. 아래의 SQL 결과를 적으시오. (AND, OR, AND 조건이 있는 SQL) 갯수세기**

```
[SQLD49]

N1  V1  V2
--------------
 1 A	T1
 2 B	T2
 3 NULL	T3
```

정답→3

해설 :

 

**단답형 10. 아래의 SQL결과를 적으시오.(LIKE '_L%' 문제)**

```
[SQLD50]

N1   V1
--------
 1  SMITH
 2  JOHN
 3  ALX
 4  CLARE
 5  BLX
 
 [SQL]
 SELECT COUNT(*) 
 FROM SQLD50 
 WHERE V1 LIKE '_L%';
```

정답→3

해설 : _L% (두번째 자리의 문자가 L인 모든 행 출력)

```
SQL> SELECT COUNT(*) FROM SQLD50 WHERE V1 LIKE '_L%';

  COUNT(*)
----------
	 3
```