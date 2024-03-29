SELECT B.AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(BS.BTS*B.PRICE) AS TOTAL_SALES
FROM BOOK AS B
LEFT JOIN (
    SELECT BOOK_ID, SUM(SALES) AS BTS
    FROM BOOK_SALES
    WHERE SALES_DATE LIKE '2022-01-%'
    GROUP BY BOOK_ID
) AS BS ON B.BOOK_ID = BS.BOOK_ID
JOIN AUTHOR AS A ON B.AUTHOR_ID = A.AUTHOR_ID
GROUP BY AUTHOR_NAME, CATEGORY
ORDER BY AUTHOR_ID ASC, CATEGORY DESC