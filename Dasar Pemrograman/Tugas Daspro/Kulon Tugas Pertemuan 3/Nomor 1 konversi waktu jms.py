# Hitung detik                       countsec(j,m,s)

# definisi dan spesifikasi
#countsec: 3 integer --> integer
# {countsec(j,m,s) adalah jam, menit, dan detik pada suatu tanggal tertentu}

# Realisasi
def countsec(j,m,s):
    return(j*3600 + m*60+s)

# Aplikasi
print(countsec(12,12,12))
