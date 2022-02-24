SELECT products.name, providers.name 
    FROM providers, products
WHERE products.id_providers = providers.ID AND providers.name = 'Ajax SA'