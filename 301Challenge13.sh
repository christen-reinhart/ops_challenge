# Set the required information for the new user
$UserName = "Franz Ferdinand"
$SamAccountName = "ferdinand"
$UserPrincipalName = "ferdi@GlobeXpower.com"
$GivenName = "Franz"
$Surname = "Ferdinand"
$DisplayName = "Franz Ferdinand"
$Department = "TPS"
$Title = "TPS Reporting Lead"
$Office = "Springfield, OR"
$EmailAddress = "ferdi@GlobeXpower.com"
$Password = "2wsxcde3@WSXCDE#" # Set a strong password

# Specify the OU path based on the provided details
$OUPath = "OU=Users,DC=GlobeX,DC=COM"

# Create a secure string for the password
$SecurePassword = ConvertTo-SecureString -AsPlainText $Password -Force

# Use New-ADUser to create the new user
New-ADUser -Name $UserName -SamAccountName $SamAccountName -UserPrincipalName $UserPrincipalName -GivenName $GivenName -Surname $Surname -DisplayName $DisplayName -Title $Title -Department $Department -Office $Office -Path $OUPath -AccountPassword $SecurePassword -Enabled $true -EmailAddress $EmailAddress

# Display a message indicating successful user creation
Write-Host "User account for $UserName created successfully."