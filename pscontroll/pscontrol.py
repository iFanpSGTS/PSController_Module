import re, psutil, os, math
from error import *

class Command:
    def __init__(self):
        pass
        
    def status(self, enet):
        try:
            for proc in psutil.process_iter():
                if enet in proc.name():
                    return 'Up'
            else: 
                if enet not in proc.name():
                    return 'Down'
        except:
            raise EnetErrorPS
        
    def online(self, online_file):
        try:
            player_online = open(f"{online_file}").readlines()
            return f'{player_online[0]} is Online!!'
        except:
            raise FileNotFoundPS
    
    def player_account(self, player_folder):
        try:
            listplayer = len(os.listdir(f'{player_folder}'))
            return f'{listplayer} account created!'
        except:
            raise FileNotFoundPS
        
    def start_enet(self, enet_path):
        try:
            os.system(r'"{enet_path}"'.format(enet_path))
            return 'The server is running!!'
        except:
            raise FileNotFoundPS
    
    def stop_enet(self, enet_path):
        try:
            os.system(f"taskkill /f /im {enet_path}")
        except:
            EnetErrorPS
            
    def world_created(self, world_folder):
        try:
            listworld = len(os.listdir(f'{world_folder}'))
            return '{listworld} is created for now!'.format(listworld)
        except:
            raise FileNotFoundPS
        
    def givepgems(self, amount, pnickname, player_folder):
        try:
            task1 = open(f'C:\\{player_folder}\\{pnickname}', 'r').read();
            oldgems = re.findall(f"{pnickname}: (.+?)",str(task1))[0]

            givegems = task1.replace(oldgems, amount);

            task2 = open(f'C:\\{player_folder}\\{pnickname}.json', 'w')
            task2.write(givegems)
            task2.close()
            return 'Succesfully give {amount} gems to {pnickname}'.format(amount, pnickname)
        except:
            raise FileNotFoundPS
        
    def giveplevel(self, amount, pnickname, player_folder):
        try:
            task1 = open(f'C:\\{player_folder}\\{pnickname}.json', 'r').read();
            oldlevel = re.findall('"level":(.+?)',str(task1))[0]

            newlevel = task1.replace(oldlevel, amount);

            task2 = open(f'C:\\yourfolderplayer\\{pnickname}.json', 'w')
            task2.write(newlevel)
            task2.close()
            return 'Succesfully give level to {}'.format(pnickname)
        except:
            raise FileNotFoundPS
    
    def giveproles(self, newrank_code, pnickname, player_folder):
        try:
            task1 = open(f'C:\\{player_folder}\\{pnickname}.json', 'r').read();
            oldrole = re.findall('"adminLevel":(.+?)',str(task1))[0]

            newrole = task1.replace(oldrole, newrank_code);

            task2 = open(f'C:\\{player_folder}\\{pnickname}.json', 'w')
            task2.write(newrole)
            task2.close()
            return 'Succes add rank to {pnickname}, now hes rank is {newrank}'.format(pnickname, newrank_code)
        except:
            raise FileNotFoundPS
        
    def countsize_pwfolder(self, player_folder, world_folder):
        try:
            def decsize(size_bytes):
                if size_bytes == 0:
                    return "0B"
                size_name = ("KB", "MB", "GB", "TB", "PB", "ZB")
                hitungan = int(math.floor(math.log(size_bytes, 1024)))
                prediksi = math.pow(1024, hitungan)
                sindikat = round(size_bytes / prediksi,2)
                return "%s %s" % (sindikat, size_name[hitungan])
            file1 = open(f'{player_folder}', 'rb').read()
            htng = len(file1)
            ukuran = (decsize(htng))
            file1y = len(os.listdir(f'{player_folder}'))
            file2 = open(f'{world_folder}', 'rb').read()
            htng1 = len(file2)
            ukuran2 = (decsize(htng1))
            file2y = len(os.listdir(f'{world_folder}'))
            return f'Player account: {file1y}, PlayerFolder size: {ukuran}\nWorld created: {file2y}, WorldFolder size: {ukuran2}'
        except:
            raise FileNotFoundPS
        
    def maintenance_activator_deactivator(self, on_off, server_data_path):
        try:
            if on_off == "on":
                file = open(f'{server_data_path}', 'r').read()
                olfmt = re.findall('(.*?)maint|Mainetrance', str(file))[0]
                chgmt = file.replace(olfmt, "");
                file2 = open('{server_data_path}', 'w')
                file2.write(chgmt)
                file2.close()
                return 'Server now is Maintenance | active!'
            elif on_off == "off":
                file1 = open('{server_data_path}', 'r').read()
                chgmt1 = file1.replace("maint", "#maint");
                file3 = open('{server_data_path}', 'w')
                file3.write(chgmt1)
                file3.close()
                return 'Server now is UnMaintenance | deactive!'
        except:
            raise FileNotFoundPS
        
    def pdel(self, pnickname, playerfolder_path, enet_path):
        try:
            namafile1 = f"{pnickname}.json"
            filepath = f"{playerfolder_path}"
            path = os.path.join(filepath, namafile1)
            os.remove(path)
            os.system(f"taskkill /f /im {enet_path}")
            os.system(r'"Server.exe"')
            return f'Server has been restarting & {namafile1} has been deleted!!'
        except:
            raise FileNotFoundPS
    
    def wdel(self, wname, worldfolder_path, enet_path):
        try:
            namafile1 = f"{wname}.json"
            filepath = f"{worldfolder_path}"
            path = os.path.join(filepath, namafile1)
            os.remove(path)
            os.system(f"taskkill /f /im {enet_path}")
            os.system(r'"Server.exe"')
            return f'Server has been restarting & {namafile1} has been deleted!!'
        except:
            raise FileNotFoundPS