-- import

with source as (
    select
        "Date",
        "Close",
        "Symbol"
    from
        {{ source('dbsales', 'commodities')  }}
),

-- rename

    renamed as (
        select
            cast("Date" as date) as data,
            "Close" as closing_value,
            "Symbol" as symbol
        from
            source

)

select * from renamed