# add_evo_links.ps1 - Add evolution chain links to Kanto Pokemon
# Also adds a "## Correlati" section linking to each other in the evo chain

$kantoDir = "c:\Users\acampanale\Desktop\poke-wiki\pokerole-wiki\wiki\03_Pokedex\Kanto"

# Define evolution chains
$chains = @(
    @("0001_Bulbasaur", "0002_Ivysaur", "0003_Venusaur"),
    @("0004_Charmander", "0005_Charmeleon", "0006_Charizard"),
    @("0007_Squirtle", "0008_Wartortle", "0009_Blastoise"),
    @("0010_Caterpie", "0011_Metapod", "0012_Butterfree"),
    @("0013_Weedle", "0014_Kakuna", "0015_Beedrill"),
    @("0016_Pidgey", "0017_Pidgeotto", "0018_Pidgeot"),
    @("0019_Rattata", "0020_Raticate"),
    @("0021_Spearow", "0022_Fearow"),
    @("0023_Ekans", "0024_Arbok"),
    @("0025_Pikachu", "0026_Raichu"),
    @("0027_Sandshrew", "0028_Sandslash"),
    @("0029_Nidoran_F", "0030_Nidorina", "0031_Nidoqueen"),
    @("0032_Nidoran_M", "0033_Nidorino", "0034_Nidoking"),
    @("0035_Clefairy", "0036_Clefable"),
    @("0037_Vulpix", "0038_Ninetales"),
    @("0039_Jigglypuff", "0040_Wigglytuff"),
    @("0041_Zubat", "0042_Golbat"),
    @("0043_Oddish", "0044_Gloom", "0045_Vileplume"),
    @("0046_Paras", "0047_Parasect"),
    @("0048_Venonat", "0049_Venomoth"),
    @("0050_Diglett", "0051_Dugtrio"),
    @("0052_Meowth", "0053_Persian"),
    @("0054_Psyduck", "0055_Golduck"),
    @("0056_Mankey", "0057_Primeape"),
    @("0058_Growlithe", "0059_Arcanine"),
    @("0060_Poliwag", "0061_Poliwhirl", "0062_Poliwrath"),
    @("0063_Abra", "0064_Kadabra", "0065_Alakazam"),
    @("0066_Machop", "0067_Machoke", "0068_Machamp"),
    @("0069_Bellsprout", "0070_Weepinbell", "0071_Victreebel"),
    @("0072_Tentacool", "0073_Tentacruel"),
    @("0074_Geodude", "0075_Graveler", "0076_Golem"),
    @("0077_Ponyta", "0078_Rapidash"),
    @("0079_Slowpoke", "0080_Slowbro"),
    @("0081_Magnemite", "0082_Magneton"),
    @("0084_Doduo", "0085_Dodrio"),
    @("0086_Seel", "0087_Dewgong"),
    @("0088_Grimer", "0089_Muk"),
    @("0090_Shellder", "0091_Cloyster"),
    @("0092_Gastly", "0093_Haunter", "0094_Gengar"),
    @("0096_Drowzee", "0097_Hypno"),
    @("0098_Krabby", "0099_Kingler"),
    @("0100_Voltorb", "0101_Electrode"),
    @("0102_Exeggcute", "0103_Exeggutor"),
    @("0104_Cubone", "0105_Marowak"),
    @("0109_Koffing", "0110_Weezing"),
    @("0111_Rhyhorn", "0112_Rhydon"),
    @("0116_Horsea", "0117_Seadra"),
    @("0118_Goldeen", "0119_Seaking"),
    @("0120_Staryu", "0121_Starmie"),
    @("0133_Eevee", "0134_Vaporeon"),
    @("0133_Eevee", "0135_Jolteon"),
    @("0133_Eevee", "0136_Flareon"),
    @("0138_Omanyte", "0139_Omastar"),
    @("0140_Kabuto", "0141_Kabutops"),
    @("0147_Dratini", "0148_Dragonair", "0149_Dragonite")
)

$updated = 0

foreach ($chain in $chains) {
    for ($i = 0; $i -lt $chain.Count; $i++) {
        $pokeName = $chain[$i]
        $filePath = Join-Path $kantoDir "$pokeName.md"
        
        if (-not (Test-Path $filePath)) {
            Write-Host "SKIP (not found): $pokeName"
            continue
        }
        
        $content = Get-Content -Path $filePath -Raw -Encoding UTF8
        
        # Skip if already has Correlati section
        if ($content -match '## Correlati') {
            continue
        }
        
        # Build evolution links
        $evoLinks = @()
        $displayName = $pokeName -replace '^\d{4}_', ''
        
        # Add links to all others in the chain
        foreach ($other in $chain) {
            if ($other -ne $pokeName) {
                $otherDisplay = $other -replace '^\d{4}_', ''
                $otherDisplay = $otherDisplay -replace '_', ' '
                $evoLinks += "- [[$other|$otherDisplay]]"
            }
        }
        
        $correlatiSection = "`n---`n`n## Correlati`n`n### Catena Evolutiva`n$($evoLinks -join "`n")`n"
        
        $newContent = $content.TrimEnd() + "`n" + $correlatiSection
        Set-Content -Path $filePath -Value $newContent -Encoding UTF8 -NoNewline
        $updated++
    }
}

Write-Host "`nUpdated $updated Pokemon files with evolution chain links."
