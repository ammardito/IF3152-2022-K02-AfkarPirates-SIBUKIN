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
        self.conn = sqlite3.connect('sibukin.db')
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("""INSERT INTO kegiatan VALUES
                        (:id_kegiatan, :nama_kegiatan, :batas_waktu, :status, :id_kategori)""",
                        {'id_kegiatan': kegiatan.id, 'nama_kegiatan': kegiatan.nama, 'batas_waktu': kegiatan.waktu, 'status': kegiatan.status, 'id_kategori': kegiatan.kategori}
                    )
        self.conn.close()    

    def insert_kategori(self, kategori):
        self.conn = sqlite3.connect('sibukin.db')
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("""INSERT INTO kategori VALUES
                        (:id_kategori, :nama_kategori)""",
                        {'id_kategori': kategori.id, 'nama_kategori': kategori.nama}
                    )
        self.conn.close()

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
        self.conn = sqlite3.connect('sibukin.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM kategori")
        return self.c.fetchall()

    def get_kegiatan_by_id(self, id):
        self.conn = sqlite3.connect('sibukin.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM kegiatan WHERE id_kegiatan=:id_kegiatan", {'id_kegiatan': id})
        return self.c.fetchone()

    def get_kategori_by_id(self, id):
        self.conn = sqlite3.connect('sibukin.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT nama_kategori FROM kategori WHERE id_kategori=:id_kategori", {'id_kategori': id})
        return self.c.fetchone()

    def update_status(self, id, new_status):
        pass

    def remove_kegiatan(self, kegiatan):
        pass
    
    def remove_kegiatan_by_id(self, id):
        pass
