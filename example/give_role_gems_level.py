from pscontroll import Command

cmd = Command()

print(cmd.givepgems("gems amount", "playernickname", "player_folder_path"))
print(cmd.giveplevel("level amount", "playernickname", "player_folder_path"))
print(cmd.giveproles("role_code", "playernickname", "player_folder_path"))