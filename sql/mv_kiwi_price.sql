create materialized view mv_kiwi_price as
with kiwi_price as (
	
	select 	
				'kiwi' as source
				, l2."propertyId" as source_id
				, l3.title as room
				, l4.title as rate_name
				, regexp_replace(l4.description, '/<[^>]*>/g','') as board_info
				, date(l2."inDate") as date_from
				, date(l2."outDate") as date_to
				, l4.date as snap_date
				, l2.currency
				, l4."totalRate" as price
				, slugify(concat(l2."propertyId", '-', l3.title, '-', l4.title, l4.description, '-', date(l2."outDate"), '-', l4.date)) as price_id
				, slugify(concat(l2."propertyId", '-', l3.title, '-', l4.title, l4.description)) as room_id
				
	from 		kiwi_l2 as l2
	inner join 	kiwi_l3 as l3
	on 			l2.id  = l3.kiwi_l2_id 
	inner join 	kiwi_l4 as l4
	on 			l3.id  = l4.kiwi_l3_id 	

), dedup as (
	select 	*
			, row_number() over(partition by room_id order by snap_date) as rn
	from 	kiwi_price
) select * from dedup where rn=1