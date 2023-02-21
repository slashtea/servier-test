-- Premiere question

-- Utilisation de CTE pour reprendre la table de base avec un total et ensuite faire une somme
-- et groupe
WITH TOTAL_VENTES AS (
  SELECT
    date,
    prod_price * prod_qty AS total
  FROM `project-id.dataset.transactions`
  WHERE date >= "2020-01-01" AND date <= "2020-12-31"
)

SELECT
  date,
  SUM(total) AS ventes
FROM TOTAL_VENTES
GROUP BY date;


-- Deuxieme question
-- Utilisation du pivot pour afficher les totaux de vente par client et par type de produits sur des colonnes

WITH TOTAL_VENTES AS (
  SELECT
    transac.client_id,
    produit.product_type,
    transac.prop_price * transac.prod_qty AS total
  FROM `project-id.dataset.transactions` AS transac
  INNER JOIN `project-id.dataset.products` AS produit
  ON transac.prop_id = produit.product_id
  WHERE transac.date >= "2020-01-01" AND transac.date <= "2020-12-31"
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