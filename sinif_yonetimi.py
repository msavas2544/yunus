
from db_utils import get_db, init_db

def sinif_ekle(ad, kapasite, aciklama):
	conn = get_db()
	c = conn.cursor()
	c.execute('INSERT INTO siniflar (ad, kapasite, aciklama) VALUES (?, ?, ?)', (ad, kapasite, aciklama))
	conn.commit()
	conn.close()

def siniflari_listele():
	conn = get_db()
	c = conn.cursor()
	c.execute('SELECT id, ad, kapasite, aciklama FROM siniflar')
	rows = c.fetchall()
	conn.close()
	return rows

def sinif_sil(sinif_id):
	conn = get_db()
	c = conn.cursor()
	c.execute('DELETE FROM siniflar WHERE id=?', (sinif_id,))
	conn.commit()
	conn.close()
