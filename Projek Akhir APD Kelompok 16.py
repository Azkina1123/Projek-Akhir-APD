"""
PROJEK AKHIR KELOMPOK 16

Anggota :
1. Aziizah Oki Shofrina (2109106004)
2. M. Arvin Saskoro (2109106048)
3. Wanda Nurhaliza (2109106055)

Tema    : Pendataan Pasien
Judul   : Pendataan Pasien di Rumah Sakit
Tujuan  : Menyimpan data pasien di rumah sakit
          Mengetahui statistik rumah sakit terkait banyaknya pasien yang mendaftar

"""

import datetime as dt
from os import system
import getpass as gp
from colorama import Fore, Back

accounts = [{"Username" : "admin", "Password" : "000"},
        {"Username" : "staff", "Password" : "123"}]


#========================================== DATA PASIEN =============================================


services = {
    "Medical Check Up" : [],
    "Rawat Jalan" : [],
    "Rawat Inap" : [],
    "Gawat Darurat" : []}

# MEDICAL CHECK UP FORM --------------------------------------
MCU_form = (
    {"Registrasi" : ("Tanggal Registrasi", "No. Pasien")},
    {"Identitas Pasien" : ("Nama Lengkap", "Tempat, Tanggal Lahir",  "Jenis Kelamin", "Pekerjaan", "Telepon/Handphone", "Alamat Lengkap")},
    {"Kebiasaan" : ("Olahraga", "Merokok", "Alkohol", "Minum Kopi")},
    {"Riwayat Penyakit Keluarga" : ("Penyakit Jantung", "Penyakit Darah Tinggi", "Penyakit Kencing Manis", "Penyakit Stroke", "Penyakit Paru")}
    )
MCU_patients = services["Medical Check Up"]
# RAWAT JALAN FORM -------------------------------------------
RawatJalan_form = (
    {"Registrasi" : ("Tanggal Registrasi", "No. Pasien")},
    {"Identitas Pasien" : ("Nama Lengkap", "Tempat, Tanggal Lahir",  "Jenis Kelamin", "Agama", "Pendidikan Terakhir", "Pekerjaan", "Telepon/Handphone", "Alamat Lengkap", "Status Pernikahan")},
    {"Sebab Perawatan" : ("Keluhan Pasien",)},
    {"Identitas Penanggungjawab" : ("Nama Lengkap", "Telepon/Handphone", "Alamat Lengkap", "Hubungan dengan Pasien")}
    )
RawatJalan_patients = services["Rawat Jalan"]
# RAWAT INAP FORM --------------------------------------------
RawatInap_form = (
    {"Registrasi" : ("Tanggal Registrasi", "No. Pasien")},
    {"Identitas Pasien" : ("Nama Lengkap", "Tempat, Tanggal Lahir", "Jenis Kelamin", "Alamat Lengkap", "No. KTP/SIM/PASPOR","Pendidikan Terakhir", "Pekerjaan", "Telepon/Handphone", "Alamat Tempat Kerja", "Warga Negara")},
    {"Anamnesis" : ("Keluhan Utama", "Riwayat Alergi", "Riwayat Transfusi Darah", "Riwayat Merokok", "Riwayat Minum Alkohol", "Riwayat Penyakit Keluarga")},
    {"Identitas Penanggungjawab" : ("Nama Lengkap", "Telepon/Handphone", "Alamat Lengkap", "Pekerjaan", "Alamat Tempat Kerja", "Hubungan dengan Pasien")},
    {"Kelas Perawatan yang Diminta" : ("Kelas Perawatan", "Kamar, Lantai", "Tanggal Masuk, Jam", "Asal Pasien (IGD/IRJ)")}
    )
RawatInap_patients = services["Rawat Inap"]
# GAWAT DARURAT FORM -----------------------------------------
GawatDarurat_form = (
    {"Registrasi" : ("Tanggal Registrasi", "No. Pasien")},
    {"Identitas Pasien" : ("Nama Lengkap", "Tempat, Tanggal Lahir", "Jenis Kelamin", "Pendidikan", "Alamat Lengkap", "Pekerjaan", "Telepon/Handphone", "Tanggal Masuk IGD")},
    {"Identitas yang Berhubungan" : ("Nama Ayah/Ibu/Suami/Istri", "Telepon/Handphone", "Penanggungjawab Pasien", "Telepon/Handphone")},
    {"Anamnesis" : ("Keluhan Utama", "Riwayat Penyakit Keluarga", "Riwayat Alergi")},
    {"Triage Status" : ("Biru/Merah/Kuning/Hijau", "Keadaan Umum", "Pernapasan", "Sirkulasi")}
    )
GawatDarurat_patients = services["Gawat Darurat"]


#=========================================== PROGRAM ==============================================


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
    while True:
        clear()
        print("\n\n\n\n\n\n\n\n")
        
        print("\033[01m  Selamat datang di Rumah Sakit Sejahtera!  \033[0m ".center(110), "\n")

        print(Fore.RED + f"{warning}".center(100) + Fore.RESET, "\n")

        print("Pilih mode berikut.".center(100))
        guide_color("(Ketik '0' untuk keluar dari program)")
        print()
        print("(1) Staff Rumah Sakit        (2) Daftar sebagai Pasien".center(100))

        mode = input("\n\t\t\t\t>>> ")

        if mode == "1":
            logIn()

        elif mode == "2":
            close_staff_mode()
            patient_MainMenu("")

        elif mode == "0":
            end("")

        elif mode == "":
            welcome("Harap pilih opsi terlebih dahulu!")

        else:
            welcome("Opsi tidak tersedia!")


# ----------------------------------- STAFF MODE ---------------------------------------


# LOGIN STAFF
def logIn():
    def logging_in(unameCounter, pwCounter, warning):
        clear()
        print("\n\n\n\n\n\n")

        print("Log In Staff Rumah Sakit".center(100))
        guide_color("(Ketik '*' untuk membatalkan log in)")

        if on_the_new_page() is True:
            global user
            user = []

        print("\n", Fore.RED + f"{warning}".center(100) + Fore.RESET, "\n")

        try:
            print(f"\t\t\t\t       Username\t: {user[0]}")
        except IndexError:
        # input username
            username = input("\t\t\t\t       Username\t: ")

            # jika username benar
            if username_exists(username) is True:
                user.append(username)
                pass

            elif username == "*":
                close_the_page()
                welcome("Proses log in dibatalkan.")

             # jika username salah
            else:
                unameCounter  += 1
                # jika username salah 3 kali
                if unameCounter == 3:
                    close_the_page()
                    welcome("Proses log in gagal!")
                else:
                    on_the_same_page()
                    logging_in(unameCounter, pwCounter, "Username salah!")

            # input password
        password = gp.getpass("\t\t\t\t       Password\t: ")

        # jika password benar
        if password_is_correct(user[0], password) is True:
            close_the_page()
            staff_MainMenu("")

        elif password == "*":
            close_the_page()
            welcome("Proses log in dibatalkan.")

        # jika password salah
        else:
            pwCounter += 1
            # jika password salah 3 kali
            if pwCounter == 3:
                close_the_page()
                welcome("Proses log in gagal!")
            else:
                on_the_same_page()
                logging_in(unameCounter, pwCounter, "Password salah!")

       
    unameCounter = 0
    pwCounter = 0
    while True:
        logging_in(unameCounter, pwCounter, "")

# MENU MEMILIH LAYANAN
def staff_MainMenu(warning):
    while True:
        open_staff_mode()
        clear()
        hospital_title()
        
        # menu layanan yang disediakan
        print (f"{'JENIS PELAYANAN :'.center(100)} \
                \n\n\t\t[1] Medical Check-Up\
                \t\t[4] Gawat Darurat\
                \n\n\t\t[2] Rawat Jalan\
                \t\t\t[5] Statistik Rumah Sakit\
                \n\n\t\t[3] Rawat Inap")

        print("\n", Fore.RED + f"{warning}".center(100) + Fore.RESET, "\n")

        print("Ketik nomor pada jenis pelayanan yang diinginkan".center(100))
        guide_color("(Ketik '0' untuk log out)")

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
            staff_MainMenu('Harap pilih opsi terlebih dahulu!')

        else:
            staff_MainMenu('Layanan tidak tersedia!')


# ------------------------------------ PATIENT MODE ----------------------------------------


# MENU MEMILIH LAYANAN (ISI FORMULIR)
def patient_MainMenu(warning):
    while True:
        clear()
        hospital_title()
        
        # menu layanan yang disediakan
        print (f"{'JENIS PELAYANAN :'.center(100)} \
                \n\n\t\t[1] Medical Check-Up\
                \t\t[3] Rawat Inap\
                \n\n\t\t[2] Rawat Jalan\
                \t\t\t[4] Gawat Darurat")

        print("\n", Fore.RED + f"{warning}".center(100) + Fore.RESET, "\n")

        print("Ketik nomor pada jenis pelayanan yang diinginkan".center(100))
        guide_color("(Ketik '0' untuk kembali ke lobi)")

        layanan = input("\n\n\t\t>>> ")

        if layanan == "1":
            MCU_reg()

        elif layanan == "2":
            RawatJalan_reg()

        elif layanan == "3": 
            RawatInap_reg()

        elif layanan == "4": 
            GawatDarurat_reg()
        
        elif layanan == "0":
            welcome("")

        elif layanan == "":
            patient_MainMenu('Harap pilih opsi terlebih dahulu!')

        else:
            patient_MainMenu('Layanan tidak tersedia!')


# ---------------------------------------- FUNGSI --------------------------------------------


# FUNGSI PENANDA MODE YANG DIJALANKAN
in_staff_mode_list = []
def open_staff_mode():
    in_staff_mode_list.append(1)
def close_staff_mode():
    in_staff_mode_list.clear()
def in_staff_mode():
    if len(in_staff_mode_list) == 0:
        return False
    else:
        return True


# JUDUL RUMAH SAKIT
def hospital_title(): 
    clear()
    print()
    print("- - - - - - - - - - - - - -".center(100))
    print(":|:|:     \033[07m\033[01m  RUMAH SAKIT SEJAHTERA  \033[0m     :|:|:".center(114))
    print("- - - - - - - - - - - - - -".center(100), "\n\n")

# JUDUL LAYANAN YG DIPILIH
def service_title(service):
    print()
    print("----------------------------------".center(100))
    title = f"-■-  {service}  -■-".upper()
    print("\033[01m"+ title.center(100) + "\033[0m ")
    print("----------------------------------".center(100), "\n\n")

# JUDUL FUNGSI YG DIPILIH
def function_title(service, submenu): 
    service_title(service)

    print(f"{submenu} {service}".center(100))

# FUNGSI MENGECEK HANYA HURUF DAN SPASI
def string_checker(string):
    true = []
    for x in string:
        try:
            to_int = int(x)
        except ValueError:
            true.append(x)

    if len(string) == len(true):
        if space_checker(string) is True:
            return False
        else:
            return True

# FUNGSI CEK ALFABET
def alpha_checker(string):
    return string.isalpha()

# FUNGSI CEK INTEGER  
def integer_checker(integer):
    try :
        check = int(integer)
    except ValueError:
        return False
    else:
        if decimal_checker(integer) is True:
            return True
        else:
            return False

# FUNGSI CEK ANGKA ASLI
def decimal_checker(integer):
    if integer.isdecimal() is True:
        return True
    else:
        return False

# FUNGSI CEK 0 DI AWAL
def zero_checker(string):
    test = []
    for x in str(string):
        test.append(x)

    if test[0] == "0" and len(test) > 1:
        return True
    else:
        return False

# FUNGSI MENGECEK HANYA SPASI
def space_checker(string):
    return string.isspace()

# FUNGSI MENGECEK JAWABAN FORMULIR
def form_checker(section, question, answer):
    if question == "Nama Lengkap" or question == "Pekerjaan" or question == "Agama" or question == "Status Pernikahan" or question == "Keluhan Pasien" or question == "Hubungan dengan Pasien" or question == "Warga Negara" or question == "Nama Ayah/Ibu/Suami/Istri" or question == "Penanggungjawab Pasien" or question == "Keluhan Utama":
        if string_checker(answer) is True:
            return True
        else:
            warning = f"Isi {question} dengan abjad!"
            return warning
    elif question == "Jenis Kelamin":
        if answer.casefold() == "p" or answer.casefold() == "l" or answer.casefold() == "perempuan" or answer.casefold() == "laki-laki" or answer.casefold() == "wanita" or answer.casefold() == "pria" or answer.casefold() =="girl" or answer.casefold() =="boy" or answer.casefold() =="woman" or answer.casefold() == "man" or answer.casefold() == "female" or answer.casefold() == "male" or answer.casefold() == "cewe" or answer.casefold() == "cowo" or answer.casefold() == "laki":
            return True
        else:
            warning = f"{question} tidak ada!"
            return warning
    elif question == "Telepon/Handphone" or question == "Kontak Ayah/Ibu/Suami/Istri" or question == "Kontak Penanggungjawab":
        if integer_checker(answer) is False:
            warning = f"Isi {question} dengan angka saja!"
            return warning
        else:
            return True
    elif question == "Asal Pasien (IGD/IRJ)":
        if answer.casefold() == "igd" or answer.casefold() == "irj":
            warning = f"Isi {question} dengan IGD atau IRJ!"
            return warning
        else:
            return True
    elif section == "Kebiasaan" or section == "Riwayat Penyakit Keluarga" or question == "Riwayat Alergi" or question == "Riwayat Transfusi Darah" or question == "Riwayat Merokok" or question == "Riwayat Minum Alkohol" or question == "Riwayat Penyakit Keluarga":
        if answer.casefold() == "ya" or answer.casefold() == "tidak" or answer.casefold() == "yes" or answer.casefold() == "no" or answer.casefold() == "y" or answer.casefold() == "n":
            return True
        else:
            warning = f"Isi bagian {section} dengan 'Ya' atau 'Tidak'!"
            return warning
    elif question == "Biru/Merah/Kuning/Hijau":
        if answer.casefold() == "biru" or answer.casefold() == "merah" or answer.casefold() == "kuning" or answer.casefold() == "hijau":
            return True
        else:
            warning = f"Pilihan tidak tersedia"
            return warning
    else:
        return True

# FUNGSI LOGIN
def username_exists(input_username):
    users = []
    for account in accounts:
        for user in account.values():
            users.append(user)

    if input_username in users[0::2]:
        return True
    else:
        return False
def password_is_correct(input_username, input_password):
    users = []
    for account in accounts:
        for user in account.values():
            users.append(user)

    if input_password in users:
        input_pasword_index = users.index(input_username) + 1
        if  users[input_pasword_index] == input_password:
            return True
        else:
            return False
    else:
        return False

# FUNGSI PENANDA HALAMAN
on_the_page_list = []
def on_the_new_page():
    if len(on_the_page_list) == 0:
        return True
    else:
        return False
def on_the_same_page():
    on_the_page_list.append(1)
def close_the_page():
    on_the_page_list.clear()

# FUNGSI WARNA GUIDE
def guide_color(guide):
    print(Fore.LIGHTBLACK_EX + guide.center(100) + Fore.RESET)

# FUNGSI BATAL ISI FORMULIR
def cancel_the_form():
    clear()
    print("\n\n\n\n\n")
    print("Apakah Anda ingin menghentikan kegiatan Anda?".center(100))

    print()
    print(Fore.LIGHTRED_EX + "Harap diperhatikan!".center(100))
    print("Pergi sekarang tidak akan menyimpan seluruh aktivitas Anda saat ini.".center(100) + Fore.RESET)
    guide_color("(Ketik '1' untuk pergi)")

    cancel = input("\n\t\t\t\t\t>>> ")
    if cancel == "1":
        return True
    else:
        return False


# -------------------------------------------- PAGE --------------------------------------------------


# HALAMAN MENU
def staff_SubMenu(service, menu_, print_, edit_, warning):
    while True:
        clear()
        service_title(service)
        
        # menu opsi yang disediakan
        print(f"{'OPSI :'.center(100)}\
                \n\n\t\t(1) Tampilkan Data Pasien\
                \t    (2) Edit Data Pasien")
        
        # peringatan yang hanya terlihat apabila ada kesalahan input
        print("\n", Fore.RED + f"{warning}".center(100) + Fore.RESET, "\n")

        print("Ketik nomor pada opsi yang diinginkan".center(100))
        guide_color("('0' untuk kembali ke menu utama)")

        opsi = input("\n\t\t>>> ") 

        if opsi == "1":
            print_()

        elif opsi == "2": 
            edit_()

        elif opsi == "0":
            staff_MainMenu("")

        elif opsi == "":
            staff_SubMenu(service, print_, edit_, menu_, 'Harap pilih opsi terlebih dahulu!')

        else:
            staff_SubMenu(service, print_, edit_, menu_, 'Opsi tidak tersedia!')

# HALAMAN REGISTRASI FORMULIR
def reg_page(service, patientData, patientForm, update_, warning):
    clear()
    function_title(service, "Registrasi Pasien Baru")
    guide_color("(Ketik '*' untuk membatalkan proses registrasi)")
    print("\n")

    # ketika pertama kali membuka halaman ini
    if on_the_new_page() is True:
        global new_patient
        new_list = []
        patientData.append(new_list)

        no_pasien = len(patientData)
        new_patient = patientData[no_pasien - 1]
        
        while len(new_patient) < len(patientForm):
            data = []
            new_patient.append(data)

        new_patient[0].append(date())
        new_patient[0].append(no_pasien)

    # menyimpan identitas pasien
    for i in patientForm:
        for section, forms in i.items():
            section_index = patientForm.index(i)

            # data default
            if section == "Registrasi":
                print(f"\t\tTanggal Registrasi : {new_patient[0][0]}")
                print(f"\t\tNo. Pasien : {new_patient[0][1]} \n")
                    
                print(Fore.RED + f"{warning}".center(100) + Fore.RESET)
                continue
            
            # data diisi pasien
            else:
                # judul tiap bagian
                if section == "Kelas Perawatan yang Diminta" or section == "Triage Status":
                    break
                else:
                    print("\n")
                    print(f"-- {section.upper()} --".center(100))

                    if section == "Kebiasaan" or section == "Riwayat Penyakit Keluarga":
                        guide_color("(Isi 'Ya' atau 'Tidak')")
                    print()

            # formulir yang ditampilkan
            for question_index in range(len(forms)):
                question = forms[question_index]

                # aturan mengisi pada bagian anamnesis
                if section == "Anamnesis" and question_index == 1:
                    print()
                    guide_color("(Isi 'Ya' atau 'Tidak')")
                    print()

                # pertanyaan yang harus diisi
                print(f"\t\t\t\t{question.ljust(27)} : ", end="")

                # jawaban pasien
                try :
                    print(new_patient[section_index][question_index])
                except IndexError:
                    input_question = input("")

                    # aturan dalam pengisian
                    if input_question == "" or space_checker(input_question) is True:
                        on_the_same_page()
                        reg_page(service, patientData, patientForm, update_, "Harap untuk tidak mengosongkan formulir!")

                    elif input_question == "*":
                        if cancel_the_form() is True :
                            close_the_page()
                            del patientData[len(patientData)-1]
                            patient_MainMenu(f"Proses registrasi {service} dibatalkan.")
                        else:
                            on_the_same_page()
                            reg_page(service, patientData, patientForm, update_, "")

                    else:
                        if form_checker(section, question, input_question) is True:
                            pass
                        else:
                            on_the_same_page()
                            reg_page(service, patientData, patientForm, update_, form_checker(section, question, input_question))
                        
                        # khusus bagian anamnesis diperlukan keterangan
                        if section == "Anamnesis" and question_index > 0:
                            if input_question.casefold() == "ya" or input_question.casefold() == "y" or input_question.casefold() == "yes":
                                keterangan = input("\t\t\t\t- Keterangan : ")
                                if keterangan == "" or space_checker(keterangan) is True:
                                    on_the_same_page()
                                    reg_page(service, patientData, patientForm, update_, "Harap untuk tidak mengosongkan formulir!")
                                elif keterangan == "*":
                                    if cancel_the_form() is True :
                                        close_the_page()
                                        del patientData[len(patientData)-1]
                                        patient_MainMenu(f"Proses registrasi {service} dibatalkan.")
                                    else:
                                        on_the_same_page()
                                        reg_page(service, patientData, patientForm, update_, "")
                                else:
                                    input_question = f"{input_question}, {keterangan}"
                    new_patient[section_index].append(input_question)
                else:
                    pass

    print("\n\n\t\tData pasien telah berhasil disimpan.")

    ubah = input("\n\t\tJika ingin mengubah data ketik '1' \n\t\t>>> ")
    if ubah == "1":
        close_the_page()
        update_(new_patient[0][1])
    else:
        input("\n\n\t\tKembali ke menu sebelumnya => ")
        close_the_page()
        finish()

# FORMULIR DIISI PETUGAS
def staff_form_page(service, patientNum, patientData, patientForm, update_, menu_, warning):
    clear()
    function_title(service, "Pengisian Formulir oleh Petugas")
    guide_color("(Ketik '*' untuk membatalkan pengisian formulir)")
    print("\n")

    add_data = patientData[patientNum -1]
    prev_data = add_data.copy()

    # ketika pertama kali membuka halaman
    if on_the_new_page() is True:
        global add_list
        add_list = []

    for i in patientForm:
        for section, forms in i.items():
            section_index = patientForm.index(i)

            # hanya bagian ini yang diisi
            if section == "Kelas Perawatan yang Diminta" or section == "Triage Status":
                print(f"\t\t\t Tanggal Registrasi : {add_data[0][0]}")
                print(f"\t\t\t No. Pasien : {patientNum}")
                print(f"\t\t\t Nama Pasien : {add_data[1][0]} \n")

                # judul bagian
                print(f"-- {section.upper()} --".center(100))
                print()
                print(Fore.RED + f"{warning}".center(100) + Fore.RESET)
                print()

                # formulir yang ditampilkan 
                for question_index in range(len(forms)):
                    form = forms[question_index]
                    
                    # selama formulir belum terisi semua
                    if len(add_list) < len(forms):
                        # pertanyaa yang harus diisi
                        print(f"\t\t\t\t{form.ljust(27)} : ", end="")

                        # jawaban petugas
                        try:
                            print(add_list[question_index])
                        except IndexError:
                            input_data = input("")
                            
                            # aturan dalam pengisian
                            if input_data == "" or space_checker(input_data) is True:
                                on_the_same_page()
                                staff_form_page(service, patientNum, patientData, patientForm, update_, menu_, "Harap tidak mengosongkan formulir")
                            elif input_data == "*":
                                if cancel_the_form() is True :
                                    close_the_page()
                                    del add_data
                                    patientData.insert(patientNum-1, prev_data)
                                    update_page(service, patientNum, patientData, patientForm, update_, menu_, "Pengisian formulir oleh petugas dibatalkan.")
                                else:
                                    on_the_same_page()
                                    staff_form_page(service, patientNum, patientData, patientForm, update_, menu_, "")
                            else:
                                if form_checker(section, form, input_data) is True:
                                    pass
                                else:
                                    on_the_same_page()
                                    staff_form_page(service, patientNum, patientData, patientForm, update_, menu_, form_checker(section, form, input_data))

                            add_list.append(input_data)

                add_data[section_index] = add_list
                close_the_page()
                break
                                        
# HALAMAN PERBARUI FORMULIR
def update_page(service, patientNum, patientData, patientForm, update_, menu_, warning):
    clear()
    function_title(service, "Perbarui Data Pasien")
    guide_color("(Tekan ENTER untuk data yang tidak ingin diperbarui)")
    print("\n")

    # data yg ingin di-update
    update_patient = patientData[patientNum-1]

    # ketika pertama kali membuka halaman
    if on_the_new_page() is True:
        global sign
        sign = []
        while len(sign) < len(patientForm):
            data = []
            sign.append(data)

    # edit data pasien
    for i in patientForm:
        for section, forms in i.items():
            index_section = patientForm.index(i)

            # data default
            if section == "Registrasi":
                for form in forms:
                    index_data = forms.index(form)
                    print(f"\t\t{form} : {update_patient[index_section][index_data]}")
            
                print("\n", Fore.RED + f"{warning}".center(100) + Fore.RESET)
                

            else:
                # bagian yang hanya bisa diedit petugas
                if section == "Kelas Perawatan yang Diminta" or section == "Triage Status":
                    if in_staff_mode() is True:
                        pass
                    else:
                        break

                # judul tiap bagian
                print("\n")
                print(f"-- {section.upper()} --".center(100))
                if section == "Kebiasaan" or section == "Riwayat Penyakit Keluarga":
                    guide_color("(Isi dengan 'Ya' atau 'Tidak')")
                elif section == "Kelas Perawatan yang Diminta" or section == "Triage Status":
                    guide_color("(Bagian berikut diisi oleh petugas yang bersangkutan)")
                else:
                    pass
                print()

                # formulir yang ditampilkan
                for index_question in range(len(forms)):
                    question = forms[index_question]

                    # jika data telah dikonfirmasi petugas (rawat inap dan gawat darurat)
                    completed = len(update_patient[index_section]) != 0
                    if section == "Kelas Perawatan yang Diminta" or section == "Triage Status":
                        if completed is False:
                            print(Fore.YELLOW + "Data belum diisi oleh petugas.".center(100) + Fore.RESET)
                            guide_color("(Ketik '1' untuk mengisi)")
                            YESorNO = input("\n\t\t\t\t\t\t>>> ")
                            if YESorNO == "1":
                                close_the_page()
                                staff_form_page(service, patientNum, patientData, patientForm, update_, menu_, "")
                                
                                break
                            else:
                                break
     
                    # aturan mengisi pada bagian anamnesis
                    if section == "Anamnesis" and index_question == 1:
                        print()
                        guide_color("(Isi 'Ya' atau 'Tidak')")
                        print()
                    else:
                        pass
                    
                    # pertanyaan yang akan diedit
                    print(f"\t\t\t{question.ljust(27)} : {update_patient[index_section][index_question].ljust(20)} {'|'.rjust(2)}", end="")

                    # jawaban
                    try :
                        print(sign[index_section][index_question])
                    except IndexError:
                        update_data = input(" ")

                        # aturan dalam pengisian
                        if update_data == "" or space_checker(update_data) is True:
                            pass
                        else:
                            if form_checker(section, question, update_data) is True:
                                pass
                            else:
                                on_the_same_page()
                                update_page(service, patientNum, patientData, patientForm, update_, menu_,form_checker(section, question, update_data))

                            # khusus bagian anamnesis diperlukan keterangan
                            if section == "Anamnesis" and index_question > 0:
                                if update_data.casefold() == "ya" or update_data.casefold() == "y" or update_data.casefold() == "yes":
                                    keterangan = input("\t\t\t- Keterangan : ")
                                    if keterangan == "" or space_checker(keterangan) is True:
                                        
                                        keterangan = update_patient[index_section][index_question].split(", ")
                                        try: 
                                            update_data = f"{update_data}, {keterangan[1]}"
                                        except IndexError:
                                            on_the_same_page()
                                            update_page(service, patientNum, patientData, patientForm, update_, menu_, "Harap untuk tidak mengosongkan formulir!")
                    
                                    else:
                                        update_data = f"{update_data}, {keterangan}"

                            update_patient[index_section][index_question] = update_data
                        sign[index_section].append("")

    print("\n\n\t\tData telah berhasil diperbarui.")
        
    close_the_page()
    ubah = input("\n\t\tApabila masih ingin mengubah data ketik '1'\n\t\t>>> ")
    if ubah == "1":
        update_(patientNum)
    else:
        input("\n\n\t\tKembali ke menu sebelumnya => ")
        if in_staff_mode() is True:
            menu_()
        else:
            finish()

# HALAMAN TAMPILKAN DATA
def show_page(service, patientData, patientForm, menu_, warning):
    clear()
    function_title(service, "Tampilkan Data Pasien")
    guide_color("(Ketik '*' untuk kembali ke menu sebelumnya)")
    print("\n")

    # fungsi menampilkan 1 data pasien
    def show_data(data):
        for i in patientForm:
            for section, forms in i.items():
                section_index = patientForm.index(i)

                if section_index == 0:
                    for form in forms:
                        index_data = forms.index(form)
                        print(f"\t\t{form} : {data[section_index][index_data]}")
                else:
                    print("\n")
                    print(f"-- {section.upper()} --".center(100))
                    print()

                    index_data = 0
                    for form in forms:
                        try :
                            print(f"\t\t\t\t{form.ljust(27)} : {data[section_index][index_data].ljust(20)}")
                        except IndexError:
                            print(Fore.YELLOW + "Data belum diisi oleh petugas.".center(100) + Fore.RESET)
                            print()
                            break

                        index_data += 1
        
    # banyak data pasien yg tersimpan dalam list (MCU_patients, RawatJalan_patients, dll)
    jumlah = len(patientData)

    # jika belum ada data yg tersimpan
    if jumlah == 0:
        print(Fore.YELLOW + "Belum ada data yang dimasukkan pada layanan ini.".center(100) + Fore.RESET)

    # jika sudah ada data yg tersimpan
    else:
        print(f"\t\tTerdapat {jumlah} data pasien yang tersimpan.")
        print("\n\t\tMesin Pencarian")
        print(Fore.LIGHTBLACK_EX + "\t\t(Ketik '0' untuk menampilkan seluruh data pasien pada layanan ini)" + Fore.RESET)
        
        print(Fore.RED + f"\n\t\t{warning}" + Fore.RESET)
    
        # mesin pencarian
        no_pasien = input("\t\tNo. Pasien: ")
        # jika inputnya bukan angka 
        if no_pasien == "*":
            menu_()

        if integer_checker(no_pasien) is False:
            show_page(service, patientData, patientForm, menu_, "Harap isi dengan angka!")
        # jika inputnya angka
        else:
            # jika mesin pencarian diisi angka no. pasien
            if int(no_pasien) <= jumlah :
                
                # jika no. pasien gak jelas (0000, 0001, dll)
                if zero_checker(no_pasien) is True:
                     show_page(service, patientData, patientForm, menu_ ,"No. Pasien tidak terdaftar!")
    
                # jika mesin pencarian diisi 0 --> tampilkan semua data pasien
                elif no_pasien == "0":
                    index = 0

                    # tampilkan seluruh data dari no. pasien terkecil
                    while index < jumlah:
                        print()
                        print(f'{"_"*100}'.center(100))
                        print()

                        # data yg akan ditampilkan
                        print_data = patientData[index]

                        # datanya sudah terhapus
                        if len(print_data) == 0:
                            print("\n\n\n")
                            print(Fore.YELLOW + "Data pasien ini telah dihapus sebelumnya.".center(100) + Fore.RESET)
                            print("\n\n")
                            
                        # datanya masih tersimpan
                        else:
                            show_data(print_data)
                                    
                        index += 1
                
                # datanya sudah dihapus
                elif len(patientData[int(no_pasien) - 1]) == 0:
                    print(f'{"_"*100}'.center(100))
                    print("\n\n")
                    print(Fore.YELLOW + "Data pasien ini telah dihapus sebelumnya.".center(100) + Fore.RESET)
                    print("\n\n")
            
                # datanya masih tersimpan
                else:
                    print()
                    print(f'{"_"*100}'.center(100))
                    print()

                    index = int(no_pasien) - 1
                    print_data = patientData[index]

                    show_data(print_data)


            # jika mesin pencarian diisi angka bukan no. pasien
            else:
                show_page(service, patientData, patientForm, menu_ ,"No. Pasien tidak terdaftar!")

    # sesi telah selesai
    input("\n\n\t\tKembali ke menu sebelumnya => ")
    menu_()

# HALAMAN EDIT DATA
def edit_page(service, patientData, patientForm, update_, menu_, warning):
    while True:
        clear()
        function_title(service, "Edit Data Pasien")
        print("")

        # FUNGSI PERBARUI DATA
        def update_menu(warning):
            clear()
            function_title(service, "Perbarui Data Pasien")
            guide_color("(Ketik '*' untuk kembali ke menu sebelumnya)")
            print("\n")
            # banyak data pasien yg tersimpan dalam patientData (MCU_patients, RawatJalan_patients, dll)
            jumlah = len(patientData)

            if patientData == RawatInap_patients or patientData == GawatDarurat_patients:
                def not_checked():
                    confirmed = 0
                    data_index_ke = 0
                    list_data = []

                    while data_index_ke < len(patientData):
                        for i in patientForm:
                            for section in i.keys():
                                if section == "Kelas Perawatan yang Diminta" or section == "Triage Status":
                                    section_index = patientForm.index(i)
                                    data = patientData[data_index_ke][section_index]
                                    list_data.append(data)
                        data_index_ke += 1

                    list_isi = []
                    for data in list_data:
                        isi = len(data)
                        list_isi.append(isi)
                    
                    if 0 in list_isi:
                        return list_isi.count(0)
                    else:
                        return 0

                print(f"\t\tTerdapat {jumlah} data pasien yang tersimpan. ")
                if not_checked() > 0:
                    print(Fore.YELLOW + f"\t\t• {not_checked()} data belum dikonfirmasi" + Fore.RESET, "\n")
                else:
                    pass

            else:
                print(f"\t\tTerdapat {jumlah} data pasien yang tersimpan. \n")

            print("\t\tMesin Pencarian")
            print(Fore.RED + f"\n\t\t{warning}" + Fore.RESET)

            # mesin pencarian
            no_pasien = input("\t\tNo. Pasien: ")

            # jika ingin kembali
            if no_pasien == "*":
                edit_page(service, patientData, patientForm, update_, menu_, warning)
            # jika inputnya bukan angka    
            elif integer_checker(no_pasien) is False:
                update_menu("Harap isi dengan angka!")
            # jika inputnya angka
            else:
                # jika mesin pencarian diisi angka no. pasien
                if 1 <= int(no_pasien) <= jumlah:
                    update_data = patientData[int(no_pasien) - 1]

                    # jika no. pasien gak jelas (0000, 0001, dll)
                    if zero_checker(no_pasien) is True:
                        update_menu("No. Pasien tidak terdaftar!")

                    # jika mesin pencarian diisi no. pasien yg datanya sudah dihapus
                    elif len(update_data) == 0:
                        print("\n\n\n")
                        print(Fore.YELLOW + "Data pasien ini telah dihapus sebelumnya.".center(100) + Fore.RESET)
                        print("\n\n")

                    # jika mesin pencarian diisi no. pasien yg datanya masih tersimpan
                    else:
                        update_(int(no_pasien))

                # jika mesin pencarian diisi angka bukan no. pasien
                else:
                    update_menu("No. Pasien tidak terdaftar!")

        # FUNGSI HAPUS DATA
        def delete_menu(warning):
            clear()
            function_title(service, "Hapus Data Pasien")
            guide_color("(Ketik '*' untuk kembali ke menu sebelumnya)")
            print("\n")

            # banyak data pasien yg tersimpan dalam patientData (MCU_patients, RawatJalan_patients, dll)
            jumlah = len(patientData)

            print(f"\t\tTerdapat {jumlah} data pasien yang tersimpan.\n")
            print("\t\tMesin Pencarian\n")
            
            # peringatan yg hanya muncul ketika terjadi kesalahan input
            print(Fore.RED + f"\t\t{warning}" + Fore.RESET)

            no_pasien = input("\t\tNo. Pasien: ")

            if no_pasien == "*":
                edit_page(service, patientData, patientForm, update_, menu_, warning)

            # jika inputnya bukan angka    
            elif integer_checker(no_pasien) is False:
                delete_menu("Harap isi dengan angka!")

            # jika inputnya integer
            else:
                clear()
                
                # jika no. pasien gak jelas (0000, 0001, dll)
                if zero_checker(no_pasien) is True:
                    delete_menu("No. Pasien tidak terdaftar!")
            
                # jika mesin pencarian diisi angka no. pasien
                elif 1 <= int(no_pasien) <= jumlah :
                    delete_data = patientData[int(no_pasien) - 1]

                    # jika data sudah dihapus sebelumnya
                    if len(delete_data) == 0:

                        print("\n\n\n\n\n\n\n\n\n")
                        print(Fore.YELLOW + "Data pasien ini telah dihapus sebelumnya.".center(100) + Fore.RESET)
                        print("\n\n")

                    else:
                        print(f"\n\n\n\n\n\n\n\n",f"Apakah Anda yakin ingin menghapus data pasien no. {no_pasien}".center(100))
                        print(f"atas nama {delete_data[1][0]}?".center(100))
                        guide_color("(Ketik '1' untuk hapus data pasien)")
                        delete = input("\n\t\t\t\t\t>>> ")

                        # jika inputnya 1, data benar-benar dihapus
                        if delete == "1":
                            delete_data.clear()

                            clear()
                            print("\n\n\n\n\n\n\n\n")
                            print(Fore.LIGHTGREEN_EX + f"Data pasien no. {no_pasien} berhasil dihapus.".center(100) + Fore.RESET)
                        
                        # jika inputnya sembarang, data tidak jadi dihapus
                        else:
                            clear()
                            print("\n\n\n\n\n\n")
                            print(Fore.RED + "Aktivitas dibatalkan.".center(100) + Fore.RESET)
                            print()

                    # jika mesin pencarian diisi angka bukan no. pasien
                else:
                    delete_menu("No. Pasien tidak terdaftar!")

        # banyak data pasien yg tersimpan dalam list (MCU_patients, RawatJalan_patients, dll)
        jumlah = len(patientData)

        # jika belum ada data yg tersimpan
        if jumlah == 0:
            print(Fore.YELLOW + "Belum ada data yang dimasukkan pada layanan ini.".center(100) + Fore.RESET)
            
        # jika sudah ada data yg tersimpan
        else:
            # opsi yang disediakan
            print(Fore.RED + f"{warning}".center(100) + Fore.RESET, "\n")
            print("(1) Perbarui data      (2) Hapus data".center(100))
            guide_color("(Ketik '0' untuk kembali ke menu sebelumnya)")
            pilih = input("\n\n\t\t\t\t\t>>> ")

            if len(pilih) == 0:
                edit_page(service, patientData, patientForm, update_, menu_, "Harap pilih opsi terlebih dahulu!")

            elif pilih == "1":
                update_menu("")

            elif pilih == "2":
                delete_menu("")

            elif pilih == "0":
                menu_()

            else:
                edit_page(service, patientData, patientForm, update_, menu_, "Opsi tidak tersedia!")
        
        input("\n\n\t\tKembali ke menu sebelumnya => ")
        menu_()


# ---------------------------------- MEDICAL CHECK UP ----------------------------------


# MENU MEDICAL CHECK UP
def MCU_menu():
    staff_SubMenu("Medical Check Up", MCU_menu, MCU_print, MCU_edit, "")

# TAMPILKAN DATA MCU
def MCU_print():
    show_page("Medical Check Up", MCU_patients, MCU_form, MCU_menu, "")

# EDIT DATA MCU
def MCU_edit():
    edit_page("Medical Check Up", MCU_patients, MCU_form, MCU_update, MCU_menu, "")

# PERBARUI FORMULIR MCU
def MCU_update(patientNum):
    update_page("Medical Check Up", patientNum, MCU_patients, MCU_form, MCU_update, MCU_menu, "")
    
# REGISTRASI MCU
def MCU_reg():       
    reg_page("Medical Check Up", MCU_patients, MCU_form, MCU_update, "")
    

# ---------------------------------- RAWAT JALAN ----------------------------------


# MENU RAWAT JALAN
def RawatJalan_menu():
    staff_SubMenu("Rawat Jalan", RawatJalan_menu, RawatJalan_print, RawatJalan_edit, "")

# TAMPILKAN DATA RAWAT JALAN
def RawatJalan_print():
    show_page("Rawat Jalan", RawatJalan_patients, RawatJalan_form, RawatJalan_menu, "")

# EDIT DATA RAWAT JALAN
def RawatJalan_edit():
    edit_page("Rawat Jalan", RawatJalan_patients, RawatJalan_form, RawatJalan_update, RawatJalan_menu, "")

# PERBARUI FORMULIR RAWAT JALAN
def RawatJalan_update(patientNum):
    update_page("Rawat Jalan", patientNum, RawatJalan_patients, RawatJalan_form, RawatJalan_update, RawatJalan_menu,"")
  
# REGISTRASI RAWAT JALAN
def RawatJalan_reg():
    reg_page("Rawat Jalan", RawatJalan_patients, RawatJalan_form, RawatJalan_update, "")


# ---------------------------------- RAWAT INAP ----------------------------------


# MENU MEDICAL CHECK UP
def RawatInap_menu():
    staff_SubMenu("Rawat Inap", RawatInap_menu, RawatInap_print, RawatInap_edit, "")

# TAMPILKAN DATA RAWAT INAP
def RawatInap_print():
    show_page("Rawat Inap", RawatInap_patients, RawatInap_form, RawatInap_menu, "")

# EDIT DATA RAWAT INAP
def RawatInap_edit():
    edit_page("Rawat Inap", RawatInap_patients, RawatInap_form, RawatInap_update, RawatInap_menu,"")

# PERBARUI DATA RAWAT INAP
def RawatInap_update(patientNum):
    update_page("Rawat Inap", patientNum, RawatInap_patients, RawatInap_form, RawatInap_update, RawatInap_menu,"")

# REGISTRASI RAWAT INAP
def RawatInap_reg():
    reg_page("Rawat Inap", RawatInap_patients, RawatInap_form, RawatInap_update, "")


# ---------------------------------- GAWAT DARURAT ----------------------------------


# MENU GAWAT DARURAT
def GawatDarurat_menu():
    staff_SubMenu("Gawat Darurat", GawatDarurat_menu, GawatDarurat_print, GawatDarurat_edit, "")

# TAMPILKAN DATA GAWAT DARURAT
def GawatDarurat_print():
    show_page("Gawat Darurat", GawatDarurat_patients, GawatDarurat_form, GawatDarurat_menu, "")

# EDIT DATA GAWAT DARURAT
def GawatDarurat_edit():
    edit_page("Gawat Darurat", GawatDarurat_patients, GawatDarurat_form, GawatDarurat_update, GawatDarurat_menu, "")

# PERBARUI DATA GAWAT DARURAT
def GawatDarurat_update(patientNum):
    update_page("Gawat Darurat", patientNum, GawatDarurat_patients, GawatDarurat_form, GawatDarurat_update, GawatDarurat_menu,"")

# REGISTRASI GAWAT DARURAT
def GawatDarurat_reg():
    reg_page("Gawat Darurat", GawatDarurat_patients, GawatDarurat_form, GawatDarurat_update, "")


# -------------------------------- STATISTIK RUMAH SAKIT --------------------------------


# STATISTIK RUMAH SAKIT
def statistics():
    while True:
        clear()

        # judul halaman
        hospital_title()
        print("Statistik Rumah Sakit".center(100))

        # tanggal hari ini
        print(f"\n\t\t{date()}")

        # diagram batang per layanan
        for service, patients in services.items():
            n = len(patients)
            print(f"\n\t\t{service.ljust(17)}", Back.LIGHTWHITE_EX + '  '*n + Back.RESET, n)

        print(f"\t\t{'_'*75}")
        print(f"\n\t\t\t\t\t\t\t\t\tTotal pasien : {len(MCU_patients) + len(RawatJalan_patients) + len(RawatInap_patients) + len(GawatDarurat_patients)}")
        
        # sesi telah selesai
        input("\n\n\t\tKembali ke menu sebelumnya => ")
        staff_MainMenu("")


# ---------------------------------- KELUAR --------------------------------------


def end(warning): 
    clear()

    # menanyakan apakah ingin keluar
    print("\n\n\n\n\n\n\n\n", "Apakah Anda yakin ingin keluar?".center(100))
    guide_color("(Ketik '1' untuk 'Ya', '0' untuk 'Tidak')")

    print("\n", Fore.RED + f"{warning}".center(100) + Fore.RESET, "\n")

    # input jawaban
    keluar = input("\t\t\t\t\t   >>> ")

    # jika input 1
    if keluar == "1":
        clear()

        print("\n\n\n\n\n\n\n\n", "Selamat tinggal ~".center(100))
        input("\n\t\t\t\t\t    Keluar => ")

        exit()

    # jika input 0
    elif keluar == "0":
        clear()

        print("\n\n\n\n\n\n\n\n", "Selamat datang kembali ~".center(100))
        input("\n\t\t\t\t\t Kembali ke lobi => ")

        welcome("")

    # jika input yang lain
    else:
        end("Harap ketik '1' atau '0'!")

def finish():
    clear()
    print("\n\n\n\n\n\n\n\n\n")
    print(Fore.GREEN + "Terima kasih telah mendaftar sebagai pasien di rumah sakit kami ".center(100) + Fore.RESET)
    input("\n\t\t\t\t\tKeluar => ")
    welcome("")


#==================================== JALANKAN PROGRAM =====================================

# PROGRAM DIMULAI ~
if __name__ == "__main__":
    while True:
        welcome("")
