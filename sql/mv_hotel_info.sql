CREATE MATERIALIZED VIEW mv_hotel_info
AS

with mms as (
	select  distinct
			'mms' as source
			, slugify(concat(data_name, '-', "location", '-', country)) as source_id
			, data_name as hotel_name
			, location as city
			, country
			, style
			, setting
	from 	mms_lite ml
), _kiwi as (
	select
			distinct
			'kiwi' as source
			, object ->> 'propertyId' as source_id
			, object ->> 'title' as hotel_name
			, region_info ->> 'nearest_city' as city
			, region_info ->> 'country' as country
			, jsonb_array_elements_text(description::jsonb -> 'style')::text as style
			, jsonb_array_elements_text(description::jsonb -> 'setting')::text as setting
	from 	kiwi_l1
), kiwi as (
	select
			source
			, source_id
			, hotel_name
			, city
			, country
			, string_agg(style, ', ') as style
			, string_agg(setting, ', ') as setting
	from 	_kiwi

	group by
			source
			, source_id
			, hotel_name
			, city
			, country

), _virt as (
	 select distinct
	 		'virt' as source
	 		, slugify(concat(vt."Title", '-', vt."CityStateCountry" ->>'City', '-',  vt."CityStateCountry" ->>'Country')) as source_id
	 		, vt."Title" as hotel_name
	 		, vt."CityStateCountry" ->>'City' as city
	 		, vt."CityStateCountry" ->>'Country' as country
	 		, jsonb_array_elements_text(vt."Experiences"::jsonb -> 'data')::text as style
			, vt."Vibe" as setting
	from 	virtuoso_l1 vt
), virt as (
	select
			source
			, source_id
			, hotel_name
			, city
			, country
			, string_agg(style, ', ') as style
			, setting
	from 	_virt

	group by
			source
			, source_id
			, hotel_name
			, city
			, country
			, setting
), combined as (

	select * from mms
	union
	select * from kiwi
	union
	select * from virt
), fin as (
	select
			source
			, slugify(source_id) as source_id
			, hotel_name
			, city
			, country
			, style
			, setting
	from 	combined
) select * from fin