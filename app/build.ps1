$exclude = @("venv", "boleto_mei.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "boleto_mei.zip" -Force