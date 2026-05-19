# create_type_pages.ps1 - Genera pagine individuali per ogni Tipo Pokemon in italiano

$typesDir = "c:\Users\acampanale\Desktop\poke-wiki\pokerole-wiki\wiki\03_Pokedex\Tipi"
if (-not (Test-Path $typesDir)) { New-Item -ItemType Directory -Path $typesDir -Force | Out-Null }

$types = @{
    "Normale" = @{ en = "Normal"; desc = "Il tipo Normale è il tipo più comune e versatile. Non ha vantaggi né svantaggi offensivi significativi, ma è immune al tipo Spettro." }
    "Fuoco" = @{ en = "Fire"; desc = "Il tipo Fuoco eccelle nell'attacco offensivo. Le mosse di Fuoco sono potenziate dal Sunny Weather e indebolite dalla Rain. Può infliggere lo status *Burn*." }
    "Acqua" = @{ en = "Water"; desc = "Il tipo Acqua è uno dei più diffusi. Le mosse di Acqua sono potenziate dalla Rain e indebolite dal Sunny Weather. Molti Pokémon di questo tipo possono nuotare e combattere sott'acqua." }
    "Erba" = @{ en = "Grass"; desc = "Il tipo Erba è forte contro Acqua, Terra e Roccia. I Pokémon di tipo Erba sono immuni a *Leech Seed* e ai movimenti basati su polveri (*Powder*)." }
    "Elettro" = @{ en = "Electric"; desc = "Il tipo Elettro è forte contro Acqua e Volante. Può infliggere *Paralysis*. I Pokémon di tipo Elettro sono immuni alla *Paralysis*." }
    "Ghiaccio" = @{ en = "Ice"; desc = "Il tipo Ghiaccio è offensivamente potente (super efficace contro Drago, Volante, Terra, Erba) ma difensivamente fragile. I Pokémon Ghiaccio sono immuni allo status *Frozen* e al danno da Hail." }
    "Lotta" = @{ en = "Fighting"; desc = "Il tipo Lotta è super efficace contro Normale, Roccia, Acciaio, Ghiaccio e Buio. Rappresenta la forza fisica e l'abilità marziale." }
    "Veleno" = @{ en = "Poison"; desc = "Il tipo Veleno può infliggere lo status *Poison* e *Badly Poisoned*. È super efficace contro Erba e Folletto." }
    "Terra" = @{ en = "Ground"; desc = "Il tipo Terra è immune alle mosse di tipo Elettro. È offensivamente forte contro Fuoco, Elettro, Veleno, Roccia e Acciaio." }
    "Volante" = @{ en = "Flying"; desc = "Il tipo Volante è immune alle mosse di tipo Terra. Le mosse Volanti sono potenziate dallo Strong Winds Weather. I Pokémon Volanti possono evitare molte mosse a terra." }
    "Psico" = @{ en = "Psychic"; desc = "Il tipo Psico è forte contro Lotta e Veleno. Rappresenta i poteri mentali e telecinetici. È debole contro Coleottero, Spettro e Buio." }
    "Coleottero" = @{ en = "Bug"; desc = "Il tipo Coleottero è forte contro Erba, Psico e Buio. I Pokémon di questo tipo tendono ad evolversi rapidamente." }
    "Roccia" = @{ en = "Rock"; desc = "Il tipo Roccia ha alta difesa. I Pokémon Roccia ottengono +1 alla Special Defense durante il Sandstorm e sono immuni al danno da Sandstorm." }
    "Spettro" = @{ en = "Ghost"; desc = "Il tipo Spettro è immune al tipo Normale e Lotta. È super efficace contro Psico e altri Spettro." }
    "Drago" = @{ en = "Dragon"; desc = "Il tipo Drago è uno dei più potenti offensivamente, ma ha poche resistenze. I Pokémon Drago sono rari e generalmente molto forti." }
    "Buio" = @{ en = "Dark"; desc = "Il tipo Buio è immune al tipo Psico. È forte contro Psico e Spettro. Rappresenta l'astuzia e la forza bruta." }
    "Acciaio" = @{ en = "Steel"; desc = "Il tipo Acciaio ha il maggior numero di resistenze (10 tipi). I Pokémon Acciaio sono immuni al danno da Sandstorm e allo status *Poison*." }
    "Folletto" = @{ en = "Fairy"; desc = "Il tipo Folletto è immune al tipo Drago. È forte contro Lotta, Drago e Buio. È stato introdotto per bilanciare il tipo Drago." }
}

foreach ($type in $types.GetEnumerator()) {
    $name = $type.Key
    $en = $type.Value.en
    $desc = $type.Value.desc

    $content = @"
---
title: "Tipo $name"
category: Type
tags: [tipo, $($name.ToLower()), $($en.ToLower())]
summary: "Pagina del tipo $name ($en) con vantaggi, svantaggi e interazioni."
---

# Tipo $name ($en)

## Descrizione

$desc

Vedi la tabella completa delle interazioni tra Tipi in [[Tipi_Pokemon]].

## Interazioni Rapide

Consulta [[Tipi_Pokemon]] per la tabella completa delle efficacie (Super Effective, Not Very Effective, Immune).

## Correlati

- [[Tipi_Pokemon]] — Tabella completa di tutti i 18 Tipi e le loro interazioni
- [[Strategie_di_Combattimento]] — Come sfruttare i vantaggi di Tipo in battaglia
- [[Meteo_e_Scenario]] — Condizioni meteo che potenziano o indeboliscono questo Tipo
"@

    $filePath = Join-Path $typesDir "$name.md"
    Set-Content -Path $filePath -Value $content -Encoding UTF8 -NoNewline
    Write-Host "Created: Tipi/$name.md"
}

Write-Host "`nDone! Created $($types.Count) type pages."
