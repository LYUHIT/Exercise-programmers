# -- 코드를 입력하세요
# SELECT CAR_ID, MAX(IF (CAR_ID IN (
#     SELECT CAR_ID
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE), '대여중', '대여가능'))AS AVAILABILITY
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# GROUP BY CAR_ID
# ORDER BY CAR_ID DESC

-- 코드를 입력하세요
SELECT distinct CAR_ID, if(CAR_ID in 
    (select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where "2022-10-16" between START_DATE and END_DATE
    ), "대여중", "대여 가능") AVAILABILITY
# SELECT *
from CAR_RENTAL_COMPANY_RENTAL_HISTORY

order by CAR_ID desc