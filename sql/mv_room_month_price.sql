create materialized view mv_room_month_price as 

with final_price as (
	
	select 
				source
				, source_id
				, room
				, rate_name
				, board_info
				, date_from
				, date_to
				, snap_date
				, currency
				, price
				, price_id
				, room_id
	from 		mv_mms_price
	where 		date_to  > now() 
	
	union 
	
	select 
				source
				, source_id
				, room
				, rate_name
				, board_info
				, date_from
				, date_to
				, snap_date
				, currency
				, price
				, price_id
				, room_id
	from 		mv_kiwi_price
	where 		date_to  > now() 
	
	
	union 
	
	select 
				source
				, source_id
				, room
				, rate_name
				, board_info
				, date_from
				, date_to
				, snap_date
				, currency
				, price
				, price_id
				, room_id
	from 		mv_virt_price
		where 		date_to  > now() 
	


), analytics_1_room_month as (
	select
				source
				, source_id
				, room
				, currency
				, date_trunc('month', date_to) as month_date
				, percentile_cont(0.8) within group (order by price) as room_month_percentile_80
				, percentile_cont(0.2) within group (order by price) as room_month_percentile_20
				, min(price) as room_month_min_price
				, max(price) as room_month_max_price
				, percentile_cont(0.5) within group (order by price) as room_month_median_price
	from 		final_price
	group by	source
				, source_id
				, room
				, currency
				, date_trunc('month', date_to) 
	
), analytics_1_hotel_month as (
	select
				source
				, source_id
				, currency
				, date_trunc('month', date_to) as month_date
				, percentile_cont(0.8) within group (order by price) as hotel_month_percentile_80
				, percentile_cont(0.2) within group (order by price) as hotel_month_percentile_20
				, min(price) as hotel_month_min_price
				, max(price) as hotel_month_max_price
				, percentile_cont(0.5) within group (order by price) as hotel_month_median_price
	from 		final_price
	group by	source
				, source_id
				, currency
				, date_trunc('month', date_to) 
	
), analytics_1_hotel as (
	select
				source
				, source_id
				, currency
				, percentile_cont(0.8) within group (order by price) as hotel_percentile_80
				, percentile_cont(0.2) within group (order by price) as hotel_percentile_20
				, min(price) as hotel_min_price
				, max(price) as hotel_max_price
				, percentile_cont(0.5) within group (order by price) as hotel_median_price
	from 		final_price
	group by	source
				, source_id
				, currency
	
), final as (

	select
				a1rm.source
				, a1rm.source_id
				, a1rm.room
				, a1rm.currency
				, a1rm.month_date
				, a1rm.room_month_percentile_80
				, a1rm.room_month_percentile_20
				, a1rm.room_month_min_price
				, a1rm.room_month_max_price
				, a1rm.room_month_median_price
				
				, a1hm.hotel_month_percentile_80
				, a1hm.hotel_month_percentile_20
				, a1hm.hotel_month_min_price
				, a1hm.hotel_month_max_price
				, a1hm.hotel_month_median_price
				
				, a1h.hotel_percentile_80
				, a1h.hotel_percentile_20
				, a1h.hotel_min_price
				, a1h.hotel_max_price
				, a1h.hotel_median_price
							
				
	from 		analytics_1_room_month as a1rm
	left join 	analytics_1_hotel_month as a1hm
	on 			a1rm.source = a1hm.source
	and 		a1rm.source_id = a1hm.source_id
	and 		a1rm.currency = a1hm.currency
	and 		a1rm.month_date = a1hm.month_date
	
	left join 	analytics_1_hotel as a1h
	on 			a1rm.source = a1h.source
	and 		a1rm.source_id = a1h.source_id
	and 		a1rm.currency = a1h.currency
	

) select * from final;