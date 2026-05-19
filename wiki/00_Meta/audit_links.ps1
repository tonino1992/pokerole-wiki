# audit_links.ps1 - Analisi completa dei wikilink nella wiki Pokerole
# Scansiona tutti i file .md, estrae i [[wikilink]] e verifica che puntino a file esistenti.

$wikiRoot = "c:\Users\acampanale\Desktop\poke-wiki\pokerole-wiki\wiki"

# 1. Build a map of all existing .md files (basename -> full path)
$allMdFiles = Get-ChildItem -Path $wikiRoot -Recurse -Filter "*.md"
$fileMap = @{}
$duplicates = @()

foreach ($f in $allMdFiles) {
    $baseName = $f.BaseName
    if ($fileMap.ContainsKey($baseName)) {
        $duplicates += [PSCustomObject]@{
            Name = $baseName
            Path1 = $fileMap[$baseName]
            Path2 = $f.FullName
        }
    }
    $fileMap[$baseName] = $f.FullName
}

# 2. Extract all [[wikilinks]] from all .md files
$brokenLinks = @()
$validLinks = @()
$orphanCandidates = @{} # files never linked TO

# Initialize orphan tracking - every file starts as "not linked to"
foreach ($f in $allMdFiles) {
    $orphanCandidates[$f.BaseName] = $f.FullName
}
# Remove index.md and log.md from orphan check (they are entry points)
$entryPoints = @("index", "log", "ingest_queue")
foreach ($ep in $entryPoints) {
    $orphanCandidates.Remove($ep)
}

foreach ($f in $allMdFiles) {
    $content = Get-Content -Path $f.FullName -Raw -ErrorAction SilentlyContinue
    if (-not $content) { continue }

    # Match [[Target]] and [[Target|Display]] patterns
    $matches = [regex]::Matches($content, '\[\[([^\]]+)\]\]')
    
    foreach ($m in $matches) {
        $linkText = $m.Groups[1].Value
        # Handle [[Target|Display]] - take the Target part
        $target = $linkText.Split('|')[0].Trim()
        # Handle [[Target#Section]] - take the Target part
        $target = $target.Split('#')[0].Trim()
        
        # Replace spaces with underscores for file lookup
        $targetNormalized = $target -replace ' ', '_'
        
        # Check if target exists in fileMap
        if ($fileMap.ContainsKey($targetNormalized)) {
            $validLinks += [PSCustomObject]@{
                Source = $f.FullName.Replace($wikiRoot + "\", "")
                Target = $target
                Resolved = $fileMap[$targetNormalized].Replace($wikiRoot + "\", "")
            }
            # Mark target as "linked to" (not orphan)
            $orphanCandidates.Remove($targetNormalized)
        }
        elseif ($fileMap.ContainsKey($target)) {
            $validLinks += [PSCustomObject]@{
                Source = $f.FullName.Replace($wikiRoot + "\", "")
                Target = $target
                Resolved = $fileMap[$target].Replace($wikiRoot + "\", "")
            }
            $orphanCandidates.Remove($target)
        }
        else {
            $brokenLinks += [PSCustomObject]@{
                Source = $f.FullName.Replace($wikiRoot + "\", "")
                Target = $target
                TargetNormalized = $targetNormalized
                RawLink = $m.Value
            }
        }
    }
}

# 3. Output Report
Write-Host ""
Write-Host "=========================================="
Write-Host " WIKI LINK AUDIT REPORT"
Write-Host "=========================================="
Write-Host ""
Write-Host "Total .md files: $($allMdFiles.Count)"
Write-Host "Total valid links: $($validLinks.Count)"
Write-Host "Total BROKEN links: $($brokenLinks.Count)"
Write-Host "Total orphan files (no inbound links): $($orphanCandidates.Count)"
Write-Host "Duplicate basenames: $($duplicates.Count)"

if ($duplicates.Count -gt 0) {
    Write-Host ""
    Write-Host "--- DUPLICATE BASENAMES ---"
    foreach ($d in $duplicates) {
        Write-Host "  '$($d.Name)': $($d.Path1) vs $($d.Path2)"
    }
}

if ($brokenLinks.Count -gt 0) {
    Write-Host ""
    Write-Host "--- BROKEN LINKS ---"
    # Group by target
    $grouped = $brokenLinks | Group-Object -Property TargetNormalized | Sort-Object -Property Count -Descending
    foreach ($g in $grouped) {
        Write-Host ""
        Write-Host "  MISSING: '$($g.Name)' (referenced $($g.Count) times)"
        foreach ($link in $g.Group | Select-Object -First 5) {
            Write-Host "    <- $($link.Source) [$($link.RawLink)]"
        }
        if ($g.Count -gt 5) {
            Write-Host "    ... and $($g.Count - 5) more"
        }
    }
}

if ($orphanCandidates.Count -gt 0) {
    Write-Host ""
    Write-Host "--- ORPHAN FILES (no inbound wikilinks) ---"
    # Exclude scripts and meta files
    $realOrphans = $orphanCandidates.GetEnumerator() | Where-Object { 
        $_.Value -notmatch '\\00_Meta\\' -and $_.Value -notmatch '\.ps1$' -and $_.Value -notmatch '\.py$'
    } | Sort-Object -Property Value
    
    foreach ($o in $realOrphans) {
        Write-Host "  $($o.Value.Replace($wikiRoot + '\', ''))"
    }
    Write-Host ""
    Write-Host "  (Total real orphans: $($realOrphans.Count))"
}

# 4. Index.md link check: find entries in index.md that point to non-existent files
Write-Host ""
Write-Host "--- INDEX.MD LINK INTEGRITY ---"
$indexContent = Get-Content -Path "$wikiRoot\index.md" -Raw
$indexLinks = [regex]::Matches($indexContent, '\[\[([^\]]+)\]\]')
$indexBroken = @()
foreach ($il in $indexLinks) {
    $target = $il.Groups[1].Value.Split('|')[0].Split('#')[0].Trim()
    $targetNorm = $target -replace ' ', '_'
    if (-not $fileMap.ContainsKey($targetNorm) -and -not $fileMap.ContainsKey($target)) {
        $indexBroken += $target
    }
}
if ($indexBroken.Count -gt 0) {
    Write-Host "  BROKEN links in index.md:"
    foreach ($ib in $indexBroken) {
        Write-Host "    - [[$ib]]"
    }
} else {
    Write-Host "  All links in index.md are valid (among those that exist as files)."
}

Write-Host ""
Write-Host "=========================================="
Write-Host " END OF AUDIT"
Write-Host "=========================================="
