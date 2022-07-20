# SQL 풀이
> 출처: [프로그래머스 - SQL 고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=sql_practice_kit)

[1. SELCT](#select)

[2. SUM, MAX, MIN](#sum-max-min)

[3. GROUP BY](#group-by)

[4. IS NULL](#is-null)

[5. JOIN](#join)

[6. String, Date](#string-date)

[7. 그외](#그외)

## SELECT
1. 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요. 
    ```sql
      SELECT * 
      FROM ANIMAL_INS 
      ORDER BY ANIMAL_ID;
    ```
2. 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.
     ```sql
        SELECT NAME, DATETIME 
        FROM ANIMAL_INS 
        ORDER BY ANIMAL_ID DESC;
     ```
3. 동물 보호소에 들어온 동물 중 아픈 동물1의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
     ```sql
        SELECT ANIMAL_ID, NAME 
        FROM ANIMAL_INS 
        WHERE INTAKE_CONDITION = 'Sick'
        ORDER BY ANIMAL_ID;
     ```
4. 동물 보호소에 들어온 동물 중 젊은 동물1의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
     ```sql
        SELECT ANIMAL_ID, NAME 
        FROM ANIMAL_INS 
        WHERE INTAKE_CONDITION != 'Aged' 
        ORDER BY ANIMAL_ID;
     ```
5. 동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요. 
     ```sql
        SELECT ANIMAL_ID, NAME 
        FROM ANIMAL_INS 
        ORDER BY ANIMAL_ID;
     ```
6. 동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.
     ```sql
        SELECT ANIMAL_ID, NAME, DATETIME 
        FROM ANIMAL_INS 
        ORDER BY NAME, DATETIME DESC;
     ```
7. 동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.
     ```sql
        SELECT NAME 
        FROM ANIMAL_INS 
        ORDER BY DATETIME 
        LIMIT 1;
     ```
## SUM, MAX, MIN
1. 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
     ```sql
        SELECT DATETIME 
        FROM ANIMAL_INS 
        ORDER BY DATETIME DESC 
        LIMIT 1;
     ```
2. 동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
     ```sql
        SELECT DATETIME 
        FROM ANIMAL_INS 
        ORDER BY DATETIME 
        LIMIT 1;
     ```
3. 동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.
     ```sql
        SELECT COUNT(*) 
        FROM ANIMAL_INS;
     ```
4. 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.
     ```sql
        SELECT COUNT(DISTINCT(NAME)) 
        FROM ANIMAL_INS 
        WHERE NAME IS NOT NULL;
     ```
## GROUP BY
1. 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.
     ```SQL
      SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) 
      FROM ANIMAL_INS 
      GROUP BY ANIMAL_TYPE 
      ORDER BY ANIMAL_TYPE;
     ```
2. 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
- `HAVING` : 함수 결과 값으로 조건을 걸 때 사용하며, 일반적으로 `GROUP BY` 절 뒤에 위치한다.
    1. COUNT(*) + WHERE
     ```sql
        SELECT NAME, COUNT(*) AS COUNT
        FROM ANIMAL_INS 
        WHERE NAME IS NOT NULL
        GROUP BY NAME 
        HAVING COUNT > 1
        ORDER BY NAME;
     ```
    2. COUNT(NAME)
     ```sql
        SELECT NAME, COUNT(NAME) AS COUNT
        FROM ANIMAL_INS 
        GROUP BY NAME 
        HAVING COUNT > 1
        ORDER BY NAME;
     ```
    - `COUNT()`는 NULL값을 제외하고 계산하기 때문에 `WHERE ~ IS NOT NULL`을 쓰지않고도 구할 수 있다.

3. 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
     ```sql
        SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT
        FROM ANIMAL_OUTS
        WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) < 20
        GROUP BY HOUR
        ORDER BY HOUR;
     ```
4. 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
    1. 변수 설정 후, 조건에 맞게 COUNT 세기
        ```sql
            SET @time := -1;
            SELECT (@time := @time + 1) AS HOUR,
            (
                SELECT COUNT(DATETIME)
                FROM ANIMAL_OUTS
                WHERE HOUR(DATETIME) = @time
            ) AS COUNT
            FROM ANIMAL_OUTS
            WHERE @time < 23;
        ```
        > `SET @변수` : 변수 선언
        > 
        > `:=` : 변수 선언시 특정 값 할당하기

    2. WITH RECURSIVE + IFNULL + LEFT OUTER JOIN(USING)
        ```sql
            -- 첫번째 테이블
            WITH RECURSIVE TIME AS (
                SELECT 0 AS HOUR
                UNION ALL
                SELECT HOUR + 1
                FROM TIME
                WHERE HOUR < 23
            )

            -- 첫번째 테이블 + 두번째 테이블
            SELECT HOUR, IFNULL(SCD_TABLE.COUNT, 0) AS COUNT
            FROM TIME
            LEFT OUTER JOIN (
                SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
                FROM ANIMAL_OUTS
                GROUP BY HOUR
            ) SCD_TABLE
            USING (HOUR);
        ```
        > `IFNULL` : 2번째 테이블의 COUNT가 NULL값이면 0으로 채워 넣는다.
        > 
        > `LEFT OUTER JOIN` : 공통된 기준을 중심으로 2번째 테이블에서 겹치는 데이터를 수용
        > 
        > `USING` : 두 테이블을 연결할 조건(기준: 두 테이블이 동일하게 가지고 있는 컬럼명)

## IS NULL
1. 동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
     ```sql
        SELECT ANIMAL_ID
        FROM ANIMAL_INS
        WHERE NAME IS NULL
        ORDER BY ANIMAL_ID;
     ```
2. 동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
     ```sql
        SELECT ANIMAL_ID
        FROM ANIMAL_INS
        WHERE NAME IS NOT NULL
        ORDER BY ANIMAL_ID;
     ```
3. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.
     ```sql
        SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE
        FROM ANIMAL_INS
        ORDER BY ANIMAL_ID;
     ```
## JOIN
1. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
    1. `NOT IN` 사용
        ```sql
            SELECT ANIMAL_ID, NAME
            FROM ANIMAL_OUTS
            WHERE ANIMAL_ID NOT IN
                (
                    SELECT ANIMAL_ID
                    FROM ANIMAL_INS
                )
            ORDER BY ANIMAL_ID;
        ```
     2. `LEFT JOIN` ~ `ON` 사용
        ```sql
            SELECT TMP1.ANIMAL_ID, TMP1.NAME
            FROM ANIMAL_OUTS TMP1
            LEFT JOIN ANIMAL_INS TMP2
            ON (
                TMP1.ANIMAL_ID = TMP2.ANIMAL_ID
            )
            WHERE TMP2.ANIMAL_ID IS NULL
            ORDER BY TMP1.ANIMAL_ID;
        ```
     3. `LEFT JOIN` ~ `USING` 사용
        ```sql
            SELECT TMP1.ANIMAL_ID, TMP1.NAME
            FROM ANIMAL_OUTS TMP1
            LEFT JOIN ANIMAL_INS TMP2
            USING (ANIMAL_ID)
            WHERE TMP2.ANIMAL_ID IS NULL
            ORDER BY TMP1.ANIMAL_ID;
        ```
2.  보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
     ```sql
        SELECT TMP1.ANIMAL_ID, TMP1.NAME
        FROM ANIMAL_INS AS TMP1
        LEFT JOIN ANIMAL_OUTS AS TMP2
        USING (ANIMAL_ID)
        WHERE TMP1.DATETIME > TMP2.DATETIME
        ORDER BY TMP1.DATETIME;
     ```
3. 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.
     ```sql
        SELECT TMP1.NAME, TMP1.DATETIME
        FROM ANIMAL_INS AS TMP1
        LEFT JOIN ANIMAL_OUTS AS TMP2
        USING (ANIMAL_ID)
        WHERE TMP2.DATETIME IS NULL
        ORDER BY TMP1.DATETIME
        LIMIT 3;
     ```
4. 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
     ```sql
        SELECT TMP1.ANIMAL_ID, TMP1.ANIMAL_TYPE, TMP1.NAME
        FROM ANIMAL_OUTS AS TMP1
        RIGHT JOIN (
            SELECT ANIMAL_ID, ANIMAL_TYPE
            FROM ANIMAL_INS
            WHERE SEX_UPON_INTAKE LIKE 'Intact%'
        ) AS TMP2
        USING (ANIMAL_ID)
        WHERE TMP1.SEX_UPON_OUTCOME NOT LIKE 'Intact%'
        ORDER BY TMP1.ANIMAL_ID;
     ```
## String, Date
1. 동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.
    1. `OR` 사용하기
     ```sql
        SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
        FROM ANIMAL_INS
        WHERE NAME = 'Lucy'
        OR NAME = 'Ella'
        OR NAME = 'Pickle'
        OR NAME = 'Rogan'
        OR NAME = 'Sabrina'
        OR NAME = 'Mitty'
        ORDER BY ANIMAL_ID;
     ```
     2. `IN` 사용하기
    ```sql
        SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
        FROM ANIMAL_INS
        WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
        ORDER BY ANIMAL_ID;
    ```
2. 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.
     ```sql
        SELECT ANIMAL_ID, NAME
        FROM ANIMAL_INS
        WHERE NAME LIKE '%EL%'
        AND ANIMAL_TYPE = 'Dog'
        ORDER BY NAME;
     ```
3. 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.
     ```sql
        SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE 'Intact%', 'X', 'O') AS '중성화'
        FROM ANIMAL_INS;
     ```
4. 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.
     ```sql
        SELECT TMP1.ANIMAL_ID, TMP1.NAME
        FROM ANIMAL_OUTS AS TMP1
        LEFT JOIN ANIMAL_INS AS TMP2
        USING (ANIMAL_ID)
        ORDER BY TMP1.DATETIME - TMP2.DATETIME DESC
        LIMIT 2;
     ```
5.  동물의 아이디와 이름, 들어온 날짜1를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다.
    1. `DATE_FORMAT` 활용하기
     ```sql
        SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d')
        FROM ANIMAL_INS
        ORDER BY ANIMAL_ID;
     ```
     2. `LEFT` 함수 활용하기
     ```sql
        SELECT ANIMAL_ID, NAME, LEFT(DATETIME, 10)
        FROM ANIMAL_INS
        ORDER BY ANIMAL_ID;
    ```
## 그외
1. 이 서비스에서는 공간을 둘 이상 등록한 사람을 "헤비 유저"라고 부릅니다. 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회하는 SQL문을 작성해주세요.
     ```sql
         SELECT TMP1.ID, TMP1.NAME, TMP1.HOST_ID
         FROM PLACES AS TMP1
         JOIN (
            SELECT HOST_ID
            FROM PLACES
            GROUP BY HOST_ID
            HAVING COUNT(HOST_ID) > 1
         ) AS TMP2
         ON TMP1.HOST_ID = TMP2.HOST_ID
         ORDER BY TMP1.ID;
     ```
2. 데이터 분석 팀에서는 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니가 있는지 알아보려 합니다. 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.
      1. `(INNER) JOIN` + `WHERE` 2번 사용하기
         ```sql
            SELECT DISTINCT TMP1.CART_ID
            FROM CART_PRODUCTS AS TMP1
            JOIN (
               SELECT CART_ID
               FROM CART_PRODUCTS
               WHERE NAME = 'Yogurt'
            ) AS TMP2
            USING (CART_ID)
            WHERE TMP1.NAME = 'Milk'
            ORDER BY CART_ID;
         ```
      2. `(INNER) JOIN` + `WHERE` 1번 사용하기
         ```sql
            SELECT DISTINCT TMP1.CART_ID
            FROM CART_PRODUCTS AS TMP1
            JOIN CART_PRODUCTS AS TMP2
            ON TMP1.CART_ID = TMP2.CART_ID
            WHERE TMP1.NAME = 'Milk' AND TMP2.NAME='Yogurt'
            ORDER BY CART_ID;
         ```
      3. `IN` 연산자 + `COUNT(DISTINCT 필드명)` 활용하기
         ```sql
               SELECT CART_ID
               FROM CART_PRODUCTS
               WHERE NAME IN ('Yogurt', 'Milk')
               GROUP BY CART_ID 
               HAVING COUNT(DISTINCT NAME) > 1;
         ```