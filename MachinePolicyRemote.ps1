# Collect hostname from user
$Hostname = Read-Host -Prompt 'Enter Hostname of machine you want to run Machine Policy Retrieval and Evaluation Cycle on: '

# Run Machine Policy Retrieval Cycle
Invoke-WMIMethod -ComputerName $Hostname -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000021}"

# Run Machine Policy Evaluation Cycle
Invoke-WMIMethod -ComputerName $Hostname -Namespace root\ccm -Class SMS_CLIENT -Name TriggerSchedule "{00000000-0000-0000-0000-000000000022}"