import mysql.connector as conn

db = conn.connect(

	host="localhost",
	user="kone",
	password="Klol4365!",
	database="music_company"
)

pointer=db.cursor()

#for audio
query_1="select distributor.*, candidate.* from distributor, candidate, sells_album, creates_album where distributor.d_incoming_url = (select d_incoming_url from sells_album where m_id in (select m_id from for_sale_album where m_id in (select m_id from approved_album where m_id in (select m_id from music_album where m_type = 'audio'))) and d_incoming_url in (select d_incoming_url from downloads where do_request_date >= '2021-01-01' and do_request_date <= '2021-12-31' and do_status='pass') group by d_incoming_url order by count(*) desc limit 0,1) and sells_album.d_incoming_url=distributor.d_incoming_url and sells_album.m_id=creates_album.m_id and candidate.c_id=creates_album.c_id"
pointer.execute(query_1)
result1=pointer.fetchall()
print("query_1 executed successfully")
for x in result1:
	print(x)

#for video
query_2="select distributor.*, candidate.* from distributor, candidate, sells_album, creates_album where distributor.d_incoming_url = (select d_incoming_url from sells_album where m_id in (select m_id from for_sale_album where m_id in (select m_id from approved_album where m_id in (select m_id from music_album where m_type = 'video'))) and d_incoming_url in (select d_incoming_url from downloads where do_request_date >= '2021-01-01' and do_request_date <= '2021-12-31' and do_status='pass') group by d_incoming_url order by count(*) desc limit 0,1) and sells_album.d_incoming_url=distributor.d_incoming_url and sells_album.m_id=creates_album.m_id and candidate.c_id=creates_album.c_id"
pointer.execute(query_2)
result2=pointer.fetchall()
print("query_2 executed successfully")
for x in result2:
	print(x)

db.close()
