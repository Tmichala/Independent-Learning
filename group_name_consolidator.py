import pyperclip
import os
import subprocess

print("Usage:\nRun following powershell command on HUSPD10, replacing user's identity with their AD username:\n\n" +
"get-adprincipalgroupmembership -Identity HUSAAA | select name | clip\n")
print("This will copy the group membership of the specified user to your clipboard.\n" + 
"Next, paste it into a file called groups.txt and manually copy the output, and paste " + 
"it into the user's active directory group membership then hit enter or check names." +
"\n\nHit Enter if confronted with multiple group names.\n")

from_user = input("Enter the username of the user you would like to copy group membership FROM (example: x-husmit): ")
to_user = input("Enter the username of the user you would like to copy group mmebership TO: ")

skips = ("", "----", "name", "Domain Users")
# get groups FROM user
input_file = 'test'

output = [f"{name.strip()};" for name in input_file if name.strip() not in skips]
for out in output:
    print(out)