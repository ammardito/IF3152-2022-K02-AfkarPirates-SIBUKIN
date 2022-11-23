import sqlite3
from kegiatan import Kegiatan
from kategori import Kategori

class Model():
    def __init__(self):
        pass

    def create_table(self):
        self.conn = sqlite3.connect('sibukin.db')
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("""CREATE TABLE IF NOT EXISTS kegiatan (
                        id_kegiatan integer,
                        nama_kegiatan text,
                        batas_waktu text,
                        status text,
                        id_kategori integer,
                        PRIMARY KEY (id_kegiatan),
                        FOREIGN KEY (id_kategori) REFERENCES kategori(id_kategori)
                        )"""
                    )
            self.c.execute("""CREATE TABLE IF NOT EXISTS kategori (
                        id_kategori integer,
                        nama_kategori text,
                        PRIMARY KEY (id_kategori)
                        )"""
                    )
        self.conn.close()

    def insert_kegiatan(self, kegiatan):
        pass  

    def insert_kategori(self, kategori):
        pass

    def get_all_kegiatan(self):
        self.conn = sqlite3.connect('sibukin.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM kegiatan")
        return self.c.fetchall()

    def get_all_kegiatan_with_nama_kategori(self):
        self.conn = sqlite3.connect('sibukin.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM kegiatan INNER JOIN kategori USING(id_kategori)")
        return self.c.fetchall()
    
    def get_kegiatan_filtered_today(self):
        pass
    
    def get_kegiatan_filtered_status(self, status):
        pass
    
    def get_kegiatan_filtered_kategori(self, kategori):
        pass
    
    def get_kegiatan_filtered_status_kategori(self, status, kategori):
        pass

    def get_kegiatan_filtered_status_today(self, status):
        pass

    def get_kegiatan_filtered_kategori_today(self, kategori):
        pass
    
    def get_kegiatan_filtered_status_kategori_today(self, status, kategori):
        pass

    def get_all_kategori(self):
        pass

    def get_kegiatan_by_id(self, id):
        pass

    def get_kategori_by_id(self, id):
        pass

    def update_status(self, id, new_status):
        self.conn = sqlite3.connect('sibukin.db')
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("""UPDATE kegiatan SET status = :status
                        WHERE id_kegiatan = :id_kegiatan""",
                    {'id_kegiatan': id, 'status': new_status})
        self.conn.close()

    def remove_kegiatan(self, kegiatan):
        pass
    
    def remove_kegiatan_by_id(self, id):
        pass
