with source as (
    select
        date,
        symbol,
        action,
        quantity
    from
        {{ source('dbsales', 'commodity_trading')  }}
),

-- rename

renamed as (
    select
        cast(date as date) as data,
        action,
        symbol,
        quantity
    from
        source
)

select * from renamed