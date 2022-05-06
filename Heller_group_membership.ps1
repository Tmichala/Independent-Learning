# Copy Active Directory group membership from user A to user B
$logfile="c:\LOG\CopyAdGroup.log"
$userSource= “jsanti"
$userTarget=”a.adams”
$Time = Get-Date
Add-content $logfile -value $Time -Encoding UTF8
Add-content $logfile -value "_______________"
Add-content $logfile -value "Copying AD groups from $userSource to $userTarget" -Encoding UTF8
$sourceGroups = (Get-ADPrincipalGroupMembership -Identity $userSource).SamAccountName
foreach ($group in $sourceGroups)
{
Add-content $logfile -value "Adding $userTarget to $group" -Encoding UTF8
try
{
$log=Add-ADPrincipalGroupMembership -Identity $userTarget -MemberOf $group
Add-content $logfile -value $log -Encoding UTF8
}
catch
{
Add-content $logfile $($Error[0].Exception.Message) -Encoding UTF8
Continue
}
}
Add-content $logfile -value "_______________"