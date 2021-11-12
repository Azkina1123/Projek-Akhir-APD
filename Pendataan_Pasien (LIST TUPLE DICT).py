"""
PROJEK AKHIR KELOMPOK 16
"""


#========================================== DATA PASIEN =============================================

services = {
    "Medical Check Up" : [],
    "Rawat Jalan" : [],
    "Rawat Inap" : [],
    "Gawat Darurat" : []
}


#--------------------------------- MEDICAL CHECK UP FORM --------------------------------------


formMCU = (
    {"Registrasi" : ("Tanggal Registrasi", 
                    "No. Pasien")},
    {"Identitas Pasien" : ("Nama Lengkap", 
                        "Tempat, Tanggal Lahir",  
                        "Jenis Kelamin", 
                        "Pekerjaan", 
                        "Telepon/Handphone", 
                        "Alamat Lengkap")},
    {"Kebiasaan" : ("Olahraga", 
                    "Merokok", 
                    "Alkohol", 
                    "Minum Kopi")},
    {"Riwayat Penyakit Keluarga" : ("Penyakit Jantung", 
                                    "Penyakit Darah Tinggi", 
                                    "Penyakit Kencing Manis", 
                                    "Penyakit Stroke", 
                                    "Penyakit Paru")}
    )

patientsMCU = services["Medical Check Up"]


#----------------------------------- RAWAT JALAN FORM --------------------------------------


formRawatJalan = (
    {"Registrasi" : ("Tanggal Registrasi", 
                        "No. Pasien")},
    {"Identitas Pasien" : ("Nama Lengkap", 
                            "Tempat, Tanggal Lahir",  
                            "Jenis Kelamin", 
                            "Agama", 
                            "Pendidikan Terakhir", 
                            "Pekerjaan", 
                            "Telepon/Handphone", 
                            "Alamat Lengkap", 
                            "Status Pernikahan", 
                            "Keluhan Pasien")},
    {"Identitas Penanggungjawab" : ("Nama Lengkap", 
                                    "Telepon/Handphone", 
                                    "Alamat Lengkap", 
                                    "Hubungan dengan Pasien")}
    )

patientsRawatJalan = services["Rawat Jalan"]


#------------------------------------ RAWAT INAP FORM --------------------------------------


formRawatInap = (
    {"Registrasi" : ("Tanggal Registrasi", 
                    "No. Pasien")},
    {"Identitas Pasien" : ("Nama Lengkap", 
                        "Tempat, Tanggal Lahir", 
                        "Jenis Kelamin", 
                        "Alamat Lengkap", 
                        "No. KTP/SIM/PASPOR",
                        "Pendidikan Terakhir", 
                        "Pekerjaan",
                        "No. Telepon", 
                        "Alamat Tempat Kerja", 
                        "Warga Negara")},
    {"Anamnesis" : ("Keluhan Utama", 
                    "Riwayat Alergi",
                    "Riwayat Tranfusi Darah",
                    "Riwayat Merokok",
                    "Riwayat Minum Alkohol",
                    "Riwayat Penyakit Keluarga")},
    {"Identitas Penanggungjawab" : ("Nama Lengkap", 
                                "Alamat Lengkap", 
                                "Pekerjaan", 
                                "Alamat Tempat Kerja", 
                                "Hubungan dengan Pasien")},
    {"Kelas Perawatan yang Diminta" : ("Kelas Perawatan", 
                                        "Kamar, Lantai", 
                                        "Tanggal Masuk, Jam", 
                                        "Asal Pasien")}
    )

patientsRawatInap = services["Rawat Inap"]


#----------------------------------- GAWAT DARURAT FORM --------------------------------------


formGawatDarurat = (
    {"Registrasi" : ("Tanggal Registrasi", 
                    "No. Pasien")},
    {"Identitas Pasien" : ("Nama Lengkap", 
                            "Tempat, Tanggal Lahir",
                            "Jenis Kelamin",
                            "Pendidikan",
                            "Alamat Lengkap",
                            "Pekerjaan",
                            "No. Telepon",
                            "Tanggal Masuk IGD")},
    {"Identitas yang Berhubungan" : ("Nama Ayah/Ibu/Suami/Istri",
                                    "No. Telepon",
                                    "Penanggungjawab Pasien",
                                    "No. Telepon")},
    {"Anamnesa" : ("Keluhan Utama",
                    "Riwayat Penyakit Keluarga",
                    "Riwayat Alergi")},
    {"Triage Status" : ("Biru/Merah/Kuning/Hijau",
                        "Keadaan Umum",
                        "Pernapasan",
                        "Sirkulasi")}
    )

patientsGawatDarurat = services["Gawat Darurat"]



#=========================================== PROGRAM ==============================================


import datetime as dt
from os import system
import sys
import getpass as gp

# CLEAR --> untuk membersihkan halaman
def clear(): 
    system("cls")

# TANGGAL 
def date(): 
    tgl_lengkap = dt.datetime.today()
    hari = tgl_lengkap.strftime("%a")
    tanggal = tgl_lengkap.strftime("%d")
    bulan = tgl_lengkap.strftime("%m")
    tahun = tgl_lengkap.strftime("%y")

    tgl = f"{hari}, {tanggal}/{bulan}/{tahun}"
    return tgl



# ------------------------------------ WELCOME -------------------------------------


# PILIH MODE
def welcome(warning): 
    clear()
    print("\n\n\n\n\n\n")
    print("  Selamat datang di Rumah Sakit Sejahtera!  ".center(100))

    print("\n\t ",f"{warning}".center(100), "\n")

    print("Pilih mode berikut.".center(100))
    print("(Ketik '0' untuk keluar dari program)".center(100), "\n")
    print("(1) Staff Rumah Sakit        (2) Daftar sebagai Pasien".center(100))

    mode = input("\n\t\t\t\t>>> ")

    if mode == "1":
        logIn("")

    elif mode == "2":
        patient_MainMenu("")

    elif mode == "0":
        exit("")

    elif mode == "":
        welcome("\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0m      ")

    else:
        welcome("\033[1;31;40m Opsi tidak tersedia! \033[0m      ")


# ----------------------------------- STAFF MODE ---------------------------------------


# LOGIN STAFF
unameCounter = [1]
pwCounter = [1]
def logIn(warning):
    clear()
    print("\n\n\n\n\n")

    print("Log In Staff Rumah Sakit".center(100))

    print("\n\t ", f"{warning}".center(100), "\n")

    # input username
    username = input("\t\t\t\t       Username\t: ")

    # jika username benar
    if username == "staff":
        unameCounter.clear()
        unameCounter.append(1)

        # input password
        password = gp.getpass(prompt="\t\t\t\t       Password\t: ")

        # jika password benar
        if password == "123":
            pwCounter.clear()
            pwCounter.append(1)

            staff_MainMenu("")

        # jika password salah 3 kali
        elif len(pwCounter) == 3:
            kickedOut()

        # jika password salah
        else:
            pwCounter.append(1)
            logIn("\033[1;31;40m Password salah! \033[0m      ")
            
    # jika username salah 3 kali
    elif len(unameCounter) == 3:
        kickedOut()

    # jika username salah
    else:
        unameCounter.append(1)
        logIn("\033[1;31;40m Username salah! \033[0m      ")

# MENU MEMILIH LAYANAN
def staff_MainMenu(warning):
    clear()
    hospital_title()

    # menu layanan yang disediakan
    print (f"{'JENIS PELAYANAN :'.center(100)} \
            \n\n\t\t[1] Medical Check-Up\
            \t\t[4] Gawat Darurat\
            \n\n\t\t[2] Rawat Jalan\
            \t\t\t[5] Statistik Rumah Sakit\
            \n\n\t\t[3] Rawat Inap")

    print("\n\t ", f"{warning}".center(100))

    print(f"\n{'Ketik nomor pada jenis pelayanan yang diinginkan'.center(100)}")
    print("('0' untuk log out)".center(100))

    layanan = input("\n\n\t\t>>> ")

    if layanan == "1":
        MCU_menu()

    elif layanan == "2":
        RawatJalan_menu()

    elif layanan == "3": 
        RawatInap_menu()

    elif layanan == "4": 
        GawatDarurat_menu()

    elif layanan == "5":
        statistics()
    
    elif layanan == "0":
        welcome("")

    elif layanan == "":
        staff_MainMenu('\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0m      ')

    else:
        staff_MainMenu('\033[1;31;40m Layanan tidak tersedia! \033[0m      ')

# MENU MEMILIH FUNGSI
def staff_SubMenu(service, menu_, print_, edit_, warning):
    clear()
    service_title(service)

    # menu opsi yang disediakan
    print(f"{'OPSI :'.center(100)}\
            \n\n\t\t(1) Tampilkan Data Pasien\
            \t    (2) Edit Data Pasien")
    
    # peringatan yang hanya terlihat apabila ada kesalahan input
    print("\n\t ", f"{warning}".center(100))

    print(f"\n{'Ketik nomor pada opsi yang diinginkan'.center(100)}")
    print("('0' untuk kembali ke menu utama)".center(100))

    opsi = input("\n\t\t>>> ") 

    if opsi == "1":
        print_()

    elif opsi == "2": 
        edit_()

    elif opsi == "3": 
        statistics()

    elif opsi == "0":
        staff_MainMenu("")

    elif opsi == "":
        staff_SubMenu(service, print_, edit_, menu_, '\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0m      ')

    else:
        staff_SubMenu(service, print_, edit_, menu_, '\033[1;31;40m Opsi tidak tersedia! \033[0m      ')


# ------------------------------------ PATIENT MODE ----------------------------------------


def patient_MainMenu(warning):
    clear()
    hospital_title()

    # menu layanan yang disediakan
    print (f"{'JENIS PELAYANAN :'.center(100)} \
            \n\n\t\t[1] Medical Check-Up\
            \t\t[3] Rawat Inap\
            \n\n\t\t[2] Rawat Jalan\
            \t\t\t[4] Gawat Darurat")

    print("\n\t ", f"{warning}".center(100))

    print(f"\n{'Ketik nomor pada jenis pelayanan yang diinginkan'.center(100)}")
    print("(Ketik '0' untuk kembali ke lobi)".center(100))

    layanan = input("\n\n\t\t>>> ")

    if layanan == "1":
        MCU_reg()

    elif layanan == "2":
        RawatJalan_reg()

    elif layanan == "3": 
        RawatInap_reg()

    elif layanan == "4": 
        GawatDarurat_reg()

    elif layanan == "5":
        statistics()
    
    elif layanan == "0":
        welcome("")

    elif layanan == "":
        patient_MainMenu('\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0m      ')

    else:
        patient_MainMenu('\033[1;31;40m Layanan tidak tersedia! \033[0m      ')


# ---------------------------------------- FUNGSI --------------------------------------------


# JUDUL RUMAH SAKIT
def hospital_title(): 
    clear()
    print()
    print("- - - - - - - - - - - - - -".center(100))
    print("      RUMAH SAKIT SEJAHTERA      ".center(100, ":"))
    print("- - - - - - - - - - - - - -".center(100), "\n\n")

# JUDUL LAYANAN YG DIPILIH
def service_title(service):
    print()
    print("----------------------------------".center(100))
    print(f"{service}".upper().center(100))
    print("----------------------------------".center(100), "\n\n")

# JUDUL FUNGSI YG DIPILIH
def function_title(service, submenu): 
    print()
    print("----------------------------------".center(100))
    print(f"{service}".upper().center(100))
    print("----------------------------------".center(100), "\n\n")

    print(f"{submenu} {service}".center(100))

# FUNGSI TAMPILKAN DATA
def print_function(service, patientData, patientForm, menu_, warning):
    clear()
    function_title(service, "Tampilkan Data Pasien")
    print("\n")

    # banyak data pasien yg tersimpan dalam list (patientsMCU, patientsRawatJalan, dll)
    jumlah = len(patientData)

    # jika belum ada data yg tersimpan
    if jumlah == 0:
        print("Belum ada data yang dimasukkan pada layanan ini.".center(100))

    # jika sudah ada data yg tersimpan
    else:
        print(f"\t\tTerdapat {jumlah} data pasien yang tersimpan.")
        print("\n\t\tMesin Pencarian")
        print("\t\t(Ketik '0' untuk menampilkan seluruh data pasien pada layanan ini)")
        
        print(f"\n\t\t{warning}")
    
        # mesin pencarian
        try:
           no_pasien = int(input("\t\tNo. Pasien: "))
        # jika inputnya bukan angka    
        except ValueError:
            print_function(service, patientData, patientForm, menu_,"\033[1;31;40m Harap isi dengan angka! \033[0m      ")
        
        # jika inputnya angka
        else:
            # jika mesin pencarian diisi angka no. pasien
            if 0 <= no_pasien <= jumlah :

                # jika mesin pencarian diisi 0 --> tampilkan semua data pasien
                if no_pasien == 0:
                    index = 0
                    # tampilkan seluruh data dari no. pasien terkecil
                    while index < jumlah:
                        print()
                        print(f'{"_"*100}'.center(100))
                        print()
                        
                        # data yg akan ditampilkan
                        print_data = patientData[index]

                        # jika data pasien telah dihapus
                        if len(print_data) == 0:
                            print("\n\n")
                            print("Data telah dihapus.".center(100))
                            print("\n\n")
                        # jika data pasien masih tersimpan
                        else:
                            for i in patientForm:
                                for section, forms in i.items():
                                    index_section = patientForm.index(i)

                                    if patientForm.index(i) == 0:
                                        for form in forms:
                                            index_data = forms.index(form)
                                            print(f"\t\t{form} : {print_data[index_section][index_data]}")
                                    else:
                                        print("\n")
                                        print(f"-- {section.upper()} --".center(100))
                                        print()

                                        index_data = 0
                                        for form in forms:
                                            print(f"\t\t\t\t{form.ljust(23)} : {print_data[index_section][index_data].ljust(20)}")
                                            index_data+= 1
                                    
                        index += 1

                # jika mesin pencarian diisi no. pasien yg datanya sudah dihapus
                elif len(patientData[no_pasien - 1]) == 0:
                    print(f'{"_"*100}'.center(100))
                    print("\n\n")
                    print("Data telah dihapus.".center(100))
                    print("\n\n")
            
                # jika mesin pencarian diisi no. pasien yg datanya masih tersimpan
                else:
                    print()
                    print(f'{"_"*100}'.center(100))
                    print()

                    index = no_pasien - 1
                    print_data = patientData[index]

                    for i in patientForm:
                        for section, forms in i.items():
                            index_section = patientForm.index(i)

                            if patientForm.index(i) == 0:
                                for form in forms:
                                    index_data = forms.index(form)
                                    print(f"\t\t{form} : {print_data[index_section][index_data]}")
                            else:
                                print("\n")
                                print(f"-- {section.upper()} --".center(100))
                                print()

                                index_data = 0
                                for form in forms:
                                    print(f"\t\t\t\t{form.ljust(23)} : {print_data[index_section][index_data].ljust(20)}")
                                    index_data+= 1
            
            # jika mesin pencarian diisi angka bukan no. pasien
            else:
                print_function(service, patientData, patientForm, menu_ ,"\033[1;31;40m No. Pasien tidak terdaftar! \033[0m      ")

    # sesi telah selesai
    back = input("\n\n\t\tKembali ke menu sebelumnya => ")
    menu_()

# FUNGSI EDIT DATA
def edit_function(service, patientData, update_, menu_, warning):
    clear()
    function_title(service, "Edit Data Pasien")
    print("\n")

    # FUNGSI PERBARUI DATA
    def update_function(update_, warning):
        clear()
        function_title(service, "Perbarui Data Pasien")
        print("\n")
        # banyak data pasien yg tersimpan dalam patientData (patientsMCU, patientsRawatJalan, dll)
        jumlah = len(patientData)

        print(f"\t\tTerdapat {jumlah} data pasien yang tersimpan. \n")
        print("\t\tMesin Pencarian")
        print(f"\n\t\t{warning}")

        # mesin pencarian
        try:
            no_pasien = int(input("\t\tNo. Pasien: "))
        # jika inputnya bukan angka    
        except ValueError:
            update_function(update_, "\033[1;31;40m Harap isi dengan angka! \033[0m      ")
        # jika inputnya angka
        else:
            # jika mesin pencarian diisi angka no. pasien
            if 1 <= no_pasien <= jumlah :
                update_data = patientData[no_pasien - 1]
                
                # jika mesin pencarian diisi no. pasien yg datanya sudah dihapus
                if len(update_data) == 0:
                    print(f'{"_"*100}'.center(100))
                    print("\n\n")
                    print("Data telah dihapus.".center(100))
                    print("\n\n")

                # jika mesin pencarian diisi no. pasien yg datanya masih tersimpan
                else:
                    update_(no_pasien)

            # jika mesin pencarian diisi angka bukan no. pasien
            else:
                update_function(update_, "\033[1;31;40m No. Pasien tidak terdaftar! \033[0m      ")

    # FUNGSI HAPUS DATA
    def delete_function(warning):
        clear()
        function_title(service, "Hapus Data Pasien")
        print("\n")

        # banyak data pasien yg tersimpan dalam patientData (patientsMCU, patientsRawatJalan, dll)
        jumlah = len(patientData)

        print(f"\t\tTerdapat {jumlah} data pasien yang tersimpan.\n")
        print("\t\tMesin Pencarian\n")
        
        # peringatan yg hanya muncul ketika terjadi kesalahan input
        print(f"\t\t{warning}")
        try:
            no_pasien = int(input("\t\tNo. Pasien: "))

        # jika inputnya bukan angka    
        except ValueError:
            delete_function("\033[1;31;40m Harap isi dengan angka! \033[0m      ")
        # jika inputnya integer
        else:
            clear()
            # jika mesin pencarian diisi angka no. pasien
            if 1 <= no_pasien <= jumlah :
                print(f"\n\n\n\n\n",f"Apakah Anda yakin ingin menghapus data pasien no. {no_pasien}?".center(100))
                print("(Ketik '1' untuk hapus data pasien)".center(100))
                delete = input("\n\t\t\t\t\t>>> ")

                # jika inputnya 1, data benar-benar dihapus
                if delete == "1":
                    delete_data = patientData[no_pasien - 1]
                    delete_data.clear()

                    clear()
                    print("\n\n\n\n\n\n")
                    print(f"Data pasien no. {no_pasien} telah dihapus.".center(100))

                # jika inputnya sembarang, data tidak jadi dihapus
                else:
                    clear()
                    print("\n\n\n\n\n\n")
                    print(f"Aktivitas dibatalkan.".center(100))
            
            # jika mesin pencarian diisi angka bukan no. pasien
            else:
                delete_function("\033[1;31;40m No. Pasien tidak terdaftar! \033[0m      ")

    # banyak data pasien yg tersimpan dalam list (patientsMCU, patientsRawatJalan, dll)
    jumlah = len(patientData)

    # jika belum ada data yg tersimpan
    if jumlah == 0:
        print("Belum ada data yang dimasukkan pada layanan ini.".center(100))
    
    # jika sudah ada data yg tersimpan
    else:

        # opsi yang disediakan
        print("")
        print("\t", f"{warning}".center(100),)
        print("(1) Perbarui data      (2) Hapus data".center(100))
        pilih = input("\n\n\t\t\t\t\t>>> ")

        if len(pilih) == 0:
            edit_function(service, patientData, update_, menu_, "\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0m      ")

        elif pilih == "1":
            update_function(update_, "")

        elif pilih == "2":
            delete_function("")

        else:
            edit_function(service, patientData, update_, menu_, "\033[1;31;40m Opsi tidak tersedia! \033[0m      ")
    
    # sesi telah selesai
    back = input("\n\n\t\tKembali ke menu sebelumnya => ")
    menu_()


# ---------------------------------- MEDICAL CHECK UP ----------------------------------


# MENU MEDICAL CHECK UP
def MCU_menu():
    staff_SubMenu("Medical Check Up", MCU_menu, MCU_print, MCU_edit, "")

# TAMPILKAN DATA MCU
def MCU_print():
    print_function("Medical Check Up", patientsMCU, formMCU, MCU_menu, "")

# EDIT DATA MCU
def MCU_edit():
    edit_function("Medical Check Up", patientsMCU, MCU_update, MCU_menu, "")

# PERBARUI FORMULIR MCU
def MCU_update(patientNum):
    clear()
    function_title("Medical Check Up", "Perbarui Data Pasien")
    print("(Tekan ENTER untuk data yang tidak ingin diperbarui)".center(100), "\n\n")

    # data yg ingin di-update
    data_pasien = patientsMCU[patientNum-1]

    for i in formMCU:
        for section, forms in i.items():

            index_section = formMCU.index(i)
            if formMCU.index(i) == 0:
                for form in forms:
                    index_data = forms.index(form)
                    print(f"\t\t{form} : {data_pasien[index_section][index_data]}")
            else:
                print("\n")
                print(f"-- {section.upper()} --".center(100))
                if formMCU.index(i) == 2 or formMCU.index(i) == 3:
                    print("(Isi dengan 'Ya' atau 'Tidak')".center(100))
                print()

                index_data = 0
                for form in forms:
                    update_data = input(f"\t\t\t{form.ljust(23)} : {data_pasien[index_section][index_data].ljust(20)} {'|'.rjust(2)} ")
                    
                    if len(update_data) == 0:
                        if len(data_pasien[index_section][index_data]) == 0:
                            print("\t\t\t\033[1;31;40m Harap masukkan data dengan benar! \033[0m      ")
                        else:
                            pass
                    else:
                        data_pasien[index_section][index_data] = update_data
                        if section == "Kebiasaan" or section == "Riwayat Penyakit Keluarga":
                            if update_data.casefold() == "ya" or update_data.casefold() == "tidak" or update_data.casefold() == "yes" or update_data.casefold() == "no":
                                pass
                            else:
                                print("\t\t\t\033[1;31;40m Harap isi dengan 'Ya' atau 'Tidak'! \033[0m      ")
                        else:
                            pass

                    index_data+= 1

    print("\n\n\t\tData telah berhasil diperbarui.")

    ubah = input("\n\t\tApabila masih ingin mengubah data ketik '1'\n\t\t>>> ")
    if ubah == "1":
        MCU_update(patientNum)
    else:
        pass
    
# REGISTRASI MCU
def MCU_reg():       
    clear()
    function_title("Medical Check Up", "Registrasi Pasien Baru")
    print("\n")

    # menyimpan tanggal dan no. pasien
    print(f"\t\tTanggal Registrasi : {date()}")
    no_pasien = len(patientsMCU) + 1
    print(f"\t\tNo. Pasien : {no_pasien}")

    data_pasien = []

    registrasi = []
    registrasi.append(date())
    registrasi.append(no_pasien)
    data_pasien.append(registrasi)

    # menyimpan identitas pasien
    for i in formMCU:
        for section, forms in i.items():

            if formMCU.index(i) == 0:
                continue

            print("\n")
            print(f"-- {section.upper()} --".center(100))

            if section == "Kebiasaan" or section == "Riwayat Penyakit Keluarga":
                print("(Isi dengan 'Ya' atau 'Tidak')".center(100))
            
            print()

            data = []
            for form in forms:
                input_data = input(f"\t\t\t\t{form.ljust(22)} : ")
                data.append(input_data)

                if input_data == "":
                    print("\t\t\t\t\033[1;31;40m Harap masukkan data dengan benar! \033[0m      ")
                elif section == "Kebiasaan" or section == "Riwayat Penyakit Keluarga":
                    if input_data.casefold() == "ya" or input_data.casefold() == "tidak" or input_data.casefold() == "yes" or input_data.casefold() == "no":
                        pass
                    else:
                        print("\t\t\t\t\033[1;31;40m Harap isi dengan 'Ya' atau 'Tidak'! \033[0m      ")
                else:
                    pass
            data_pasien.append(data)

    patientsMCU.append(data_pasien)

    print("\n\n\t\tData pasien telah berhasil disimpan.")

    ubah = input("\n\t\tJika ingin mengubah data ketik '1' \n\t\t>>> ")
    if ubah == "1":
        MCU_update(no_pasien)
    else:
        pass

    # selesai
    input("\n\n\t\tSelanjutnya => ")
    finish()
    

# ---------------------------------- RAWAT JALAN ----------------------------------


# MENU RAWAT JALAN
def RawatJalan_menu():
    staff_SubMenu("Rawat Jalan", RawatJalan_menu, RawatJalan_print, RawatJalan_edit, "")

# TAMPILKAN DATA RAWAT JALAN
def RawatJalan_print():
    print_function("Rawat Jalan", patientsRawatJalan, formRawatJalan, RawatJalan_menu, "")

# EDIT DATA RAWAT JALAN
def RawatJalan_edit():
    edit_function("Rawat Jalan", patientsRawatJalan, RawatJalan_update, RawatJalan_menu, "")

# PERBARUI FORMULIR RAWAT JALAN
def RawatJalan_update(patientNum):
    clear()
    function_title("Rawat Jalan", "Perbarui Data Pasien")
    print("(Tekan ENTER untuk data yang tidak ingin diperbarui)".center(100), "\n\n")

    # data yg ingin di-update
    data_pasien = patientsRawatJalan[patientNum-1]

    for i in formRawatJalan:
        for section, forms in i.items():

            index_section = formRawatJalan.index(i)
            if formRawatJalan.index(i) == 0:
                for form in forms:
                    index_data = forms.index(form)
                    print(f"\t\t{form} : {data_pasien[index_section][index_data]}")
            else:
                print("\n")
                print(f"-- {section.upper()} --".center(100))
                print()

                index_data = 0
                for form in forms:
                    update_data = input(f"\t\t\t{form.ljust(23)} : {data_pasien[index_section][index_data].ljust(20)} {'|'.rjust(2)} ")
                    
                    if len(update_data) == 0:
                        if len(data_pasien[index_section][index_data]) == 0:
                            print("\t\t\t\033[1;31;40m Harap masukkan data dengan benar! \033[0m      ")
                        else:
                            pass
                    else:
                        data_pasien[index_section][index_data] = update_data

                    index_data+= 1

    print("\n\n\t\tData telah berhasil diperbarui.")

    ubah = input("\n\t\tApabila masih ingin mengubah data ketik '1'\n\t\t>>> ")
    if ubah == "1":
        RawatJalan_update(patientNum)
    else:
        pass
  
# REGISTRASI RAWAT JALAN
def RawatJalan_reg():
    clear()
    function_title("Rawat Jalan", "Registrasi Pasien Baru")
    print("\n")

    # menyimpan tanggal dan no. pasien
    print(f"\t\tTanggal Registrasi : {date()}")
    no_pasien = len(patientsRawatJalan) + 1
    print(f"\t\tNo. Pasien : {no_pasien}")

    data_pasien = []

    registrasi = []
    registrasi.append(date())
    registrasi.append(no_pasien)
    data_pasien.append(registrasi)

    # menyimpan identitas pasien
    for i in formRawatJalan:
        for section, forms in i.items():

            if formRawatJalan.index(i) == 0:
                continue

            print("\n")
            print(f"-- {section.upper()} --".center(100))   
            print()

            data = []
            for form in forms:
                input_data = input(f"\t\t\t\t{form.ljust(22)} : ")
                data.append(input_data)

                if input_data == "":
                    print("\t\t\t\t\033[1;31;40m Harap masukkan data dengan benar! \033[0m      ")
                else:
                    pass
            data_pasien.append(data)

    patientsRawatJalan.append(data_pasien)

    print("\n\n\t\tData pasien telah berhasil disimpan.")

    ubah = input("\n\t\tJika ingin mengubah data ketik '1' \n\t\t>>> ")
    if ubah == "1":
        RawatJalan_update(no_pasien)
    else:
        pass

    # selesai
    input("\n\n\t\tSelanjutnya => ")
    finish()


# ---------------------------------- RAWAT INAP ----------------------------------


# MENU MEDICAL CHECK UP
def RawatInap_menu():
    staff_SubMenu("Rawat Inap", RawatInap_menu, RawatInap_print, RawatInap_edit, "")

# TAMPILKAN DATA RAWAT INAP
def RawatInap_print():
    print_function("Rawat Inap", patientsRawatInap, formRawatInap, RawatInap_menu, "")

# EDIT DATA RAWAT INAP
def RawatInap_edit():
    edit_function("Rawat Inap", patientsRawatInap, RawatInap_update, RawatInap_menu, "")

# PERBARUI DATA RAWAT INAP
def RawatInap_update(patientNum):
    clear()
    function_title("Rawat Inap", "Perbarui Data Pasien")
    print("(Tekan ENTER untuk data yang tidak ingin diperbarui)".center(100), "\n\n")

    # data yg ingin di-update
    data_pasien = patientsRawatInap[patientNum-1]

    for i in formRawatInap:
        for section, forms in i.items():

            index_section = formRawatInap.index(i)
            if formRawatInap.index(i) == 0:
                for form in forms:
                    index_data = forms.index(form)
                    print(f"\t\t{form} : {data_pasien[index_section][index_data]}")
            else:
                print("\n")
                print(f"-- {section.upper()} --".center(100))
                print()

                index_data = 0
                for form in forms:
                    update_data = input(f"\t\t\t{form.ljust(23)} : {data_pasien[index_section][index_data].ljust(20)} {'|'.rjust(2)} ")
                    
                    if len(update_data) == 0:
                        if len(data_pasien[index_section][index_data]) == 0:
                            print("\t\t\t\033[1;31;40m Harap masukkan data dengan benar! \033[0m      ")
                        else:
                            pass
                    else:
                        data_pasien[index_section][index_data] = update_data

                    index_data+= 1

    print("\n\n\t\tData telah berhasil diperbarui.")

    ubah = input("\n\t\tApabila masih ingin mengubah data ketik '1'\n\t\t>>> ")
    if ubah == "1":
        RawatInap_update(patientNum)
    else:
        pass

# REGISTRASI RAWAT INAP
def RawatInap_reg():
    clear()
    function_title("Rawat Inap", "Registrasi Pasien Baru")
    print("\n")

    # menyimpan tanggal dan no. pasien
    print(f"\t\tTanggal Registrasi : {date()}")
    no_pasien = len(patientsRawatInap) + 1
    print(f"\t\tNo. Pasien : {no_pasien}")

    data_pasien = []

    registrasi = []
    registrasi.append(date())
    registrasi.append(no_pasien)
    data_pasien.append(registrasi)

    # menyimpan identitas pasien
    for i in formRawatInap:
        for section, forms in i.items():

            if formRawatInap.index(i) == 0:
                continue

            print("\n")
            print(f"-- {section.upper()} --".center(100))   
            print()

            data = []
            for form in forms:
                input_data = input(f"\t\t\t\t{form.ljust(22)} : ")
                data.append(input_data)

                if input_data == "":
                    print("\t\t\t\t\033[1;31;40m Harap masukkan data dengan benar! \033[0m      ")
                else:
                    pass
            data_pasien.append(data)

    patientsRawatInap.append(data_pasien)

    print("\n\n\t\tData pasien telah berhasil disimpan.")

    ubah = input("\n\t\tJika ingin mengubah data ketik '1' \n\t\t>>> ")
    if ubah == "1":
        RawatInap_update(no_pasien)
    else:
        pass

    # kembali ke menu medical check up
    input("\n\n\t\tKembali ke menu sebelumnya => ")
    finish()



# ---------------------------------- GAWAT DARURAT ----------------------------------


# MENU GAWAT DARURAT
def GawatDarurat_menu():
    staff_SubMenu("Gawat Darurat", GawatDarurat_menu, GawatDarurat_print, GawatDarurat_edit, "")

# TAMPILKAN DATA GAWAT DARURAT
def GawatDarurat_print():
    print_function("Gawat Darurat", patientsGawatDarurat, formGawatDarurat, GawatDarurat_menu, "")

# EDIT DATA GAWAT DARURAT
def GawatDarurat_edit():
    edit_function("Gawat Darurat", patientsGawatDarurat, GawatDarurat_update, GawatDarurat_menu, "")

# PERBARUI DATA GAWAT DARURAT
def GawatDarurat_update(patientNum):
    clear()
    function_title("Gawat Darurat", "Perbarui Data Pasien")
    print("(Tekan ENTER untuk data yang tidak ingin diperbarui)".center(100), "\n\n")

    # data yg ingin di-update
    data_pasien = patientsGawatDarurat[patientNum-1]

    for i in formGawatDarurat:
        for section, forms in i.items():

            index_section = formGawatDarurat.index(i)
            if formGawatDarurat.index(i) == 0:
                for form in forms:
                    index_data = forms.index(form)
                    print(f"\t\t{form} : {data_pasien[index_section][index_data]}")
            else:
                print("\n")
                print(f"-- {section.upper()} --".center(100))
                print()

                index_data = 0
                for form in forms:
                    update_data = input(f"\t\t\t{form.ljust(23)} : {data_pasien[index_section][index_data].ljust(20)} {'|'.rjust(2)} ")
                    
                    if len(update_data) == 0:
                        if len(data_pasien[index_section][index_data]) == 0:
                            print("\t\t\t\033[1;31;40m Harap masukkan data dengan benar! \033[0m      ")
                        else:
                            pass
                    else:
                        data_pasien[index_section][index_data] = update_data

                    index_data+= 1

    print("\n\n\t\tData telah berhasil diperbarui.")

    ubah = input("\n\t\tApabila masih ingin mengubah data ketik '1'\n\t\t>>> ")
    if ubah == "1":
        GawatDarurat_update(patientNum)
    else:
        pass

# REGISTRASI GAWAT DARURAT
def GawatDarurat_reg():
    clear()
    function_title("Rawat Inap", "Registrasi Pasien Baru")
    print("\n")

    # menyimpan tanggal dan no. pasien
    print(f"\t\tTanggal Registrasi : {date()}")
    no_pasien = len(patientsGawatDarurat) + 1
    print(f"\t\tNo. Pasien : {no_pasien}")

    data_pasien = []

    registrasi = []
    registrasi.append(date())
    registrasi.append(no_pasien)
    data_pasien.append(registrasi)

    # menyimpan identitas pasien
    for i in formGawatDarurat:
        for section, forms in i.items():

            if formGawatDarurat.index(i) == 0:
                continue

            print("\n")
            print(f"-- {section.upper()} --".center(100))

            if formGawatDarurat.index(i) == 4:
                print("(Bagian berikut diisi oleh perawat/dokter)".center(100))
                
            print()

            data = []
            for form in forms:
                input_data = input(f"\t\t\t\t{form.ljust(22)} : ")
                data.append(input_data)

                if input_data == "":
                    if formGawatDarurat.index(i) == 4:
                        pass
                    else:
                        print("\t\t\t\t\033[1;31;40m Harap masukkan data dengan benar! \033[0m      ")
                else:
                    pass

            data_pasien.append(data)

    patientsGawatDarurat.append(data_pasien)

    print("\n\n\t\tData pasien telah berhasil disimpan.")

    ubah = input("\n\t\tJika ingin mengubah data ketik '1' \n\t\t>>> ")
    if ubah == "1":
        GawatDarurat_update(no_pasien)
    else:
        pass

    # kembali ke menu medical check up
    input("\n\n\t\tKembali ke menu sebelumnya => ")
    finish()


# -------------------------------- STATISTIK RUMAH SAKIT --------------------------------


# STATISTIK RUMAH SAKIT
def statistics():
    clear()

    # judul halaman
    hospital_title()
    print("Statistik Rumah Sakit".center(100))

    # tanggal hari ini
    print(f"\n\t\t{date()}")

    # diagram batang per layanan
    for service, patients in services.items():
        n = len(patients)
        print(f"\n\t\t{service.ljust(17)}", '\033[1;37;47m|\033[0m'*n, n)

    print(f"\t\t{'_'*75}")
    print(f"\n\t\t\t\t\t\t\t\t\tTotal pasien : {len(patientsMCU) + len(patientsRawatJalan) + len(patientsRawatInap) + len(patientsGawatDarurat)}")
    
    # sesi telah selesai
    back = input("\n\n\t\tKembali ke menu sebelumnya => ")
    staff_MainMenu("")


# ---------------------------------- TAMBAHAN --------------------------------------


def exit(warning): 
    clear()

    # menanyakan apakah ingin keluar
    print("\n\n\n\n\n","Apakah Anda yakin ingin keluar?".center(100))
    print("(Ketik '1' untuk 'Ya', '0' untuk 'Tidak')".center(100))

    print("\n\t", f"{warning}".center(100))

    # input jawaban
    keluar = input("\n\t\t\t\t\t   >>> ")

    # jika input 1
    if keluar == "1":
        clear()

        print("\n\n\n\n\n\n", "Selamat tinggal ~".center(100))
        input("\n\t\t\t\t\t    Keluar => ")

        sys.exit()

    # jika input 0
    elif keluar == "0":
        clear()

        print("\n\n\n\n\n\n", "Selamat datang kembali ~".center(100))
        input("\n\t\t\t\t\t Kembali ke lobi => ")

        welcome("")

    # jika input yang lain
    else:
        exit("\033[1;31;40m Harap ketik '1' atau '0'! \033[0m      ")

def kickedOut():
    clear()
    print("\n\n\n\n\n\n\n")
    print("\t ","\033[1;31;40m Anda telah dikeluarkan dari rumah sakit! \033[0m      ".center(100))
    input("\n\t\t\t\t\tKeluar => ")
    sys.exit()

def finish():
    clear()
    print("\n\n\n\n\n\n\n")
    print("\t", "\033[0;32;40m Terima kasih telah mendaftar sebagai pasien di rumah sakit kami \033[0m       ".center(100))
    input("\n\t\t\t\t\tKeluar => ")
    welcome("")


#==================================== JALANKAN PROGRAM =====================================

# PROGRAM DIMULAI ~
welcome("")

