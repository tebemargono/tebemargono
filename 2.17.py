himpunan ={"senin", 'selasa', 'rabu', 'kamis','jumat'}

tanya_hari = input("hari apa sekarang? ").lower()

if tanya_hari in himpunan:
    print("Sekarang hari kerja")
else:
    print("Sekarang hari libur!")
