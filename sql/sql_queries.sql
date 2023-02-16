-- Premiere question

-- Utilisation de CTE pour reprendre la table de base avec un total et ensuite faire une somme
-- et groupe
WITH TOTAL_VENTES AS (
  SELECT
    *,
    prod_price * prod_qty AS total
  FROM `project-id.dataset.transactions`
)

SELECT
  date,
  SUM(total) AS ventes
FROM TOTAL_VENTES
WHERE date >= "2019-01-01" AND date <= "2019-12-31"
GROUP BY date


-- Deuxieme question
-- Utilisation du pivot pour afficher les totaux de vente par client et par type de produits sur des colonnes

WITH TOTAL_VENTES AS (
  SELECT
    client_id,
    product_type,
    prop_price * prod_qty AS total
  FROM `project-id.dataset.transactions` AS transac
  INNER JOIN `project-id.dataset.products` AS produit
  ON transac.prop_id = produit.product_id
  WHERE date >= "2019-01-01" AND date <= "2019-12-31"
)

SELECT * FROM
(
  SELECT 
    product_type,
    client_id,
    total
  FROM TOTAL_VENTES
)

PIVOT
(
  SUM(total) AS ventes
  FOR product_type in ('MEUBLE', 'DECO')
)