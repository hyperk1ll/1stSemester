# konversi waktu                        countsec2(j,m,s,k)

# definisi dan spesifikasi
#countsec2: 3 integer 1 string --> integer
# {countsec2(j,m,s,k) adalah jumlah detik dari jam, menit, dan detik pada suatu tanggal tertentu dengan k menyatakan am atau pm pada jam tersebut}

# Realisasi
def countsec2(j,m,s,k):
    if(k == "am"):
        return(j*3600 + m*60+ s)
    elif(k == "pm"):
        return(3600*12 + j*3600 + m*60+ s)

# Aplikasi
print(countsec2(1,2,5,"am"))
