# Make sure to run this script as an administrator. 
# Additionally, it will not work if the desired user is currently signed in.

# Get users
$Users = Get-ChildItem -Path "C:\Users\" -Force
Foreach ($User in $Users)
{
    # Clear errors
    $error.clear()
    
    # Declare hive location
    $hive = "C:\Users\" + $user.name + "\ntuser.dat"

    # Load hive into a temp location in registry
    echo "Loading $hive"
    reg load "HKLM\Temp" "$hive"

    # If hive opened successfully, attempt to delete registry values
    if (!$error) {
        # Define desired reg values to delete here
        remove-itemproperty -path "hklm:\temp\Software\Microsoft\Office\16.0\Common\Internet\" -name "UseOnlineContent" -erroraction 'silentlycontinue'
        remove-itemproperty -path "hklm:\temp\Software\Policies\Microsoft\Office\16.0\Common\Internet\" -name "UseOnlineContent" -erroraction 'silentlycontinue'
        remove-itemproperty -path "hklm:\temp\Software\Microsoft\Office\16.0\Common\SignIn\" -name "SignInOptions" -erroraction 'silentlycontinue'
        remove-itemproperty -path "hklm:\temp\Software\Policies\Microsoft\Office\16.0\Common\SignIn\" -name "SignInOptions" -erroraction 'silentlycontinue'
    }

    # Unload hive
    echo "Unloading $hive"
    reg unload "HKLM\temp"
}  
