-- models/datamart/dm_commodities.sql

with commodities as (
    select
        data,
        symbol,
        closing_value
    from
        {{ ref('stg_commodity') }}
),

handling as (
    select
        data,
        symbol,
        action,
        quantity
    from
        {{ ref('stg_commodity_trading') }}
),

joined as (
    select
        c.data,
        c.symbol,
        c.closing_value,
        m.action,
        m.quantity,
        (m.quantity * c.closing_value) as value,
        case
            when m.action = 'sell' then (m.quantity * c.closing_value)
            else -(m.quantity * c.closing_value)
        end as earning
    from
        commodities c
    inner join
        handling m
    on
        c.data = m.data
        and c.symbol = m.symbol
),

last_day as (
    select
        max(data) as max_date
    from
        joined
),

filtered as (
    select
        *
    from
        joined
    where
        data = (select max_date from last_day)
)

select
    data,
    symbol,
    closing_value,
    action,
    quantity,
    value,
    earning
from
    filtered