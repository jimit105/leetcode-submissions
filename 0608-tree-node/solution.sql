SELECT id, 'Root' as Type
FROM tree
WHERE p_id IS NULL

UNION

SELECT id, 'Leaf' as Type
FROM tree
WHERE id NOT IN (
    SELECT DISTINCT p_id
    FROM tree
    WHERE p_id IS NOT NULL
) AND p_id IS NOT NULL

UNION

SELECT id, 'Inner' as Type
FROM tree
WHERE id IN (
    SELECT DISTINCT p_id
    FROM tree
    WHERE p_id IS NOT NULL
) AND p_id IS NOT NULL

ORDER BY id;
