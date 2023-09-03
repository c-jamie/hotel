create materialized view mv_virt_price as 
with virt_price as (
	select 
				'virt' as source
				, slugify(concat(v1."Title", '-', v1."CityStateCountry" ->>'City', '-',  v1."CityStateCountry" ->>'Country')) as source_id
				, v2."Description" as room
				, null as rate_name
				, null as board_info
				, date(v2.start_date) as date_from
				, date(v2.end_date) as date_to
				, date(v2.date) as snap_date
				, 'USD' as currency
				, v2."TotalAmountUsd" as price
				, slugify(concat(v1."Title", '-', 
					v1."CityStateCountry" ->>'City', '-',  
					v1."CityStateCountry" ->>'Country', 
					v2."Description", date(v2.end_date), date(v2.date))) as price_id
				, slugify(concat(v1."Title", '-', 
					v1."CityStateCountry" ->>'City', '-',  
					v1."CityStateCountry" ->>'Country', 
					v2."Description")) as room_id
	
	from 		virtuoso_l2 as v2
	inner join 	virtuoso_l1 as v1
	on 			v2.supplier_id  = v1."Id" 
), dedup as (
	select 	*
			, row_number() over(partition by room_id order by snap_date) as rn
	from 	virt_price
) select * from dedup where rn=1