-- 코드를 입력하세요
-- 통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차
-- 자동차 종류 별로 몇 대인지 출력

SELECT CAR_TYPE, COUNT(*) AS CARS
FROM (
    SELECT CAR_TYPE
    FROM CAR_RENTAL_COMPANY_CAR 
    WHERE OPTIONS LIKE '%통풍시트%' 
        OR OPTIONS LIKE '%열선시트%' 
        OR OPTIONS LIKE '%가죽시트%'
    ) AS OP
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE

