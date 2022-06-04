# Nama      : Muhammad Hilmy Tsany
# NIM       : 24060120140171
# Tanggal   : 14 Desember 2020
# Deskripsi : Latihan UAS (Coba Soal UAS Tahun 2019/2020)
# Nomor 2

# DefSpek
# TotalElmtDaun : PohonBiner --> integer
# TotalElmtDaun(P) menghitung jumlah daun pada pohon biner

def TotalElmtDaun(P):
    if(IsOneElmt(P)):
        return Akar(P)
    else:
        if(IsBiner(P)):
            return TotalElmtDaun(Left(P)) + TotalElmtDaun(Right(P))
        elif(IsUnerRightPB(P)):
            return TotalElmtDaun(Left(P))
        elif(IsUnerRightPB(P)):
            return TotalElmtDaun(Right(P))

# TotalElmtNode: PohonBiner --> integer
# TotalElmtNode(P) menghitung jumlah semua elemen pada pohon biner

def TotalElmtNode(P):
    if(IsOneElmt(P)):
        return Akar(P)
    else:
        if(IsBiner(P)):
            return TotalElmtNode(Left(P))+ Akar(P) + TotalElmtNode(Right(P))
        elif(IsUnerLeftPB(P)):
            return TotalElmtNode(Left(P)) + Akar(P)
        elif(IsUnerRightPB(P)):
            return Akar(P) + TotalElmtNode(Right(P))