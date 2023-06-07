# daftar penyakit (master)
penyakit = {
    'P01': {'nama': 'a', 'gejala': ['G01', 'G03']},
    'P02': {'nama': 'b', 'gejala': ['G02', 'G03', 'G06']},
    'P03': {'nama': 'c', 'gejala': ['G02', 'G04', 'G01', 'G05']},
    'P04': {'nama': 'd', 'gejala': ['G06', 'G05']}
}

# daftar gejala (master)
gejala = {
    'G01': {'nama': 'pusing', 'nilai_pakar': 0.8},
    'G02': {'nama': 'Keringat Dingin', 'nilai_pakar': 0.6},
    'G03': {'nama': 'Menggigil', 'nilai_pakar': 0.5},
    'G04': {'nama': 'Dehidrasi', 'nilai_pakar': 0.2},
    'G05': {'nama': 'Batuk', 'nilai_pakar': 0.5},
    'G06': {'nama': 'Nyeri Tenggorokan', 'nilai_pakar': 0.5}
}

# rumus perhitungan nilai dari cf
def hitung_cf(nilai_dari_gejala, nilai_dari_pakar):
    return nilai_dari_gejala * nilai_dari_pakar

# pasien 1 (pasien)
gejala_pasien = {
    'G01': 0.5,  # pusing
    'G05': 0.8,  # batuk
    'G04': 0.4,  # dehidrasi
    'G02': 0.3,  # keringat dingin
    'G03': 0.2  # menggigil
}

# perhitungan cf
hasil_penyakit = {}

for kode_penyakit, data_penyakit in penyakit.items():
    # rumus untuk Cf[H,E]1 = Cf[H]1 x Cf[E]1 (proses awal)
    gejala_penyakit = data_penyakit['gejala']
    cf_penyakit = [hitung_cf(gejala_pasien[kode_gejala], gejala[kode_gejala]['nilai_pakar']) for kode_gejala in gejala_penyakit if kode_gejala in gejala_pasien and gejala_pasien[kode_gejala] is not None]

    if cf_penyakit:
        cf_hasil = cf_penyakit[0]
        for cf_gejala in cf_penyakit[1:]:
            # rumus untuk Cf[Cf1,Cf2] = Cf[H,E]1 + Cf[H,E]2 * [1-Cf[H,E]1] (proses lanjut)
            cf_hasil = cf_hasil + cf_gejala * (1 - cf_hasil)

        hasil_penyakit[kode_penyakit] = cf_hasil

# hasil cf (kesimpulan)
print("Kesimpulan dari sistem pakar")
hasil_penyakit = sorted(hasil_penyakit.items(), key=lambda x: x[1], reverse=True)
for kode_penyakit, cf in hasil_penyakit:
    nama_penyakit = penyakit[kode_penyakit]['nama']
    print(f'{nama_penyakit}\t = {cf * 100:.2f}%')
print("Pasien menderita penyakit P03")
