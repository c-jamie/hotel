create materialized view mv_mms_price as 

with mms_price as (
	select 
				'mms' as source
				, li.source_id
				, trim(md.name) as room
				, md.room_info_raw as rate_name
				, md.board_raw as board_info
				, date(md."from") as date_from
				, date(md."to") as date_to
				, date(md.time_stamp) as snap_date
				, coalesce(md.data_rate_currency_total_price_offer, md.data_rate_currency_total_price_original) as currency
				, coalesce(CAST(md.data_rate_inc_total_price_offer as REAL), CAST(md.data_rate_inc_total_price_original as REAL)) as price
				, slugify(concat(li.source_id, '-', md.room_info_raw, '-', md.board_raw, '-', md."to", '-', md.time_stamp)) as price_id
				, slugify(concat(li.source_id, '-', md.room_info_raw, '-', md.board_raw)) as room_id
	from 		mms_deep as md
	join 		mv_hotel_info as li
	on 			slugify(md.hotel_name) = slugify(li.hotel_name)
	and 		li.source='mms'

), dedup as (
	select 	*
			, row_number() over(partition by room_id order by snap_date) as rn
	from 	mms_price
	where 	price is not null
) select * from dedup where rn=1
