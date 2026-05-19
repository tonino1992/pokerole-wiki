# fix_charge_links.ps1 - Update [[Charge]] trait references to [[Charge_Trait]]
$movesDir = "c:\Users\acampanale\Desktop\poke-wiki\pokerole-wiki\wiki\04_Moves_e_Abilities\Mosse"

Get-ChildItem -Path $movesDir -Filter "*.md" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -Encoding UTF8
    if ($content -match '\[\[Charge\]\]') {
        $newContent = $content -replace '\[\[Charge\]\]', '[[Charge_Trait]]'
        Set-Content $_.FullName -Value $newContent -Encoding UTF8 -NoNewline
        Write-Host "Updated: $($_.Name)"
    }
}

# Now delete the old Charge.md trait file
$oldFile = "c:\Users\acampanale\Desktop\poke-wiki\pokerole-wiki\wiki\04_Moves_e_Abilities\Tratti\Charge.md"
if (Test-Path $oldFile) {
    Remove-Item $oldFile
    Write-Host "Deleted old Tratti/Charge.md"
}

Write-Host "Done!"
