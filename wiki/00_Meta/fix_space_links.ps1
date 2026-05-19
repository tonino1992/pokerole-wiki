# fix_space_links.ps1 - Normalizza i wikilink: sostituisci spazi con underscore dove esiste il file corrispondente
# Es: [[Leech Seed]] -> [[Leech_Seed]] (perché il file si chiama Leech_Seed.md)

$wikiRoot = "c:\Users\acampanale\Desktop\poke-wiki\pokerole-wiki\wiki"

# 1. Build map of all .md basenames (with underscores)
$allMdFiles = Get-ChildItem -Path $wikiRoot -Recurse -Filter "*.md"
$fileBasenames = @{}
foreach ($f in $allMdFiles) {
    $fileBasenames[$f.BaseName] = $true
}

Write-Host "Loaded $($fileBasenames.Count) file basenames"

# 2. Process all .md files
$totalFixed = 0
$filesModified = 0

foreach ($f in $allMdFiles) {
    $content = Get-Content -Path $f.FullName -Raw -Encoding UTF8
    if (-not $content) { continue }
    
    $originalContent = $content
    
    # Match all [[...]] wikilinks that contain spaces
    $content = [regex]::Replace($content, '\[\[([^\]\|#]+)\]\]', {
        param($match)
        $linkTarget = $match.Groups[1].Value
        
        # If link contains spaces, try underscore version
        if ($linkTarget -match ' ') {
            $underscored = $linkTarget -replace ' ', '_'
            if ($fileBasenames.ContainsKey($underscored)) {
                $script:totalFixed++
                return "[[$underscored]]"
            }
        }
        
        # Return original if no match
        return $match.Value
    })
    
    # Also handle [[Target|Display]] format with spaces in target
    $content = [regex]::Replace($content, '\[\[([^\]\|#]+)\|([^\]]+)\]\]', {
        param($match)
        $linkTarget = $match.Groups[1].Value
        $displayText = $match.Groups[2].Value
        
        # If target contains spaces, try underscore version
        if ($linkTarget -match ' ') {
            $underscored = $linkTarget -replace ' ', '_'
            if ($fileBasenames.ContainsKey($underscored)) {
                $script:totalFixed++
                return "[[$underscored|$displayText]]"
            }
        }
        
        return $match.Value
    })
    
    # Also handle [[Target#Section]] format with spaces in target
    $content = [regex]::Replace($content, '\[\[([^\]\|#]+)#([^\]\|]+)\]\]', {
        param($match)
        $linkTarget = $match.Groups[1].Value
        $section = $match.Groups[2].Value
        
        if ($linkTarget -match ' ') {
            $underscored = $linkTarget -replace ' ', '_'
            if ($fileBasenames.ContainsKey($underscored)) {
                $script:totalFixed++
                return "[[$underscored#$section]]"
            }
        }
        
        return $match.Value
    })
    
    if ($content -ne $originalContent) {
        Set-Content -Path $f.FullName -Value $content -Encoding UTF8 -NoNewline
        $filesModified++
        $relativePath = $f.FullName.Replace($wikiRoot + "\", "")
        Write-Host "  Modified: $relativePath"
    }
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  RESULTS"
Write-Host "=========================================="
Write-Host "  Files modified: $filesModified"
Write-Host "  Links fixed: $totalFixed"
Write-Host "=========================================="
