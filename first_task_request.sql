SELECT 
    c.login,
    COUNT(o.track) AS in_delivery_count
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = TRUE
GROUP BY c.login;