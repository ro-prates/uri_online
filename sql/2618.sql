SELECT products.name, providers.name, products.price 
    FROM products, providers, categories
WHERE products.price > 1000 
    AND categories.name = 'Super Luxury' 
    AND categories.id = products.id_categories
    AND products.id_providers = providers.id