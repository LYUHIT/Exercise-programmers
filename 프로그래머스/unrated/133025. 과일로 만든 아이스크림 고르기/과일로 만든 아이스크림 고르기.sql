-- 코드를 입력하세요
-- 총 주문량 > 3000
-- 주 성분 == 과일
-- 정렬 : 총주문량 큰 순서

SELECT FLAVOR
FROM FIRST_HALF
WHERE FLAVOR IN (
    SELECT FLAVOR
    FROM ICECREAM_INFO
    WHERE INGREDIENT_TYPE = 'fruit_based'
) AND TOTAL_ORDER > 3000
