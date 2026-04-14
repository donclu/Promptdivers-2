# Promptdivers — installer (PowerShell)
# Same behavior as install.sh: copies bundled skills to IDE global folders and optional project bootstrap.
# Works on Windows (Windows PowerShell 5.1+ or PowerShell 7+), macOS, and Linux (PowerShell Core / pwsh).
#
# Usage:
#   pwsh  -File ./install.ps1
#   pwsh  -File ./install.ps1 -Project .
#   pwsh  -File ./install.ps1 -Cursor
#   powershell.exe -ExecutionPolicy Bypass -File .\install.ps1   # Windows PowerShell 5.1
#
# Bash-style flags: --project, --cursor, --claude, --help

#Requires -Version 5.1

$ErrorActionPreference = 'Stop'

# True on Windows for both Windows PowerShell 5.1 and PowerShell 7+ ($IsWindows exists only in Core)
$IsWinOS = [System.Environment]::OSVersion.Platform -eq [System.PlatformID]::Win32NT

# Pack root at script scope ($PSScriptRoot empty when dot-sourced; $MyInvocation inside a function would be wrong)
if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) {
    $PackDir = [System.IO.Path]::GetFullPath($PSScriptRoot)
} elseif ($MyInvocation.MyCommand.Path) {
    $PackDir = [System.IO.Path]::GetFullPath((Split-Path -Parent -LiteralPath $MyInvocation.MyCommand.Path))
} else {
    $PackDir = [System.IO.Path]::GetFullPath((Get-Location).ProviderPath)
}

$SkillsSrc = Join-Path $PackDir 'skills'
$SkillNames = @(
    'promptdivers-orchestrator',
    'promptdivers-pelican',
    'promptdivers-tactical-signals',
    'promptdivers-orbital-control',
    'promptdivers-ministry-of-truth',
    'promptdivers-stratagem-terminal'
)

# UTF-8 output on Windows consoles (helps emoji); harmless if it fails in CI
try {
    if ($IsWinOS) {
        [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
    }
} catch {
}

function Write-PromptLog([string]$Message) { Write-Host "[promptdivers] $Message" -ForegroundColor Cyan }
function Write-PromptOk([string]$Message) { Write-Host "  ✅ $Message" -ForegroundColor Green }
function Write-PromptWarn([string]$Message) { Write-Host "  ⚠️  $Message" -ForegroundColor Yellow }
function Write-PromptFail([string]$Message) { Write-Host "  ❌ $Message" -ForegroundColor Red }
function Write-PromptHeader([string]$Message) { Write-Host "`n$Message" -ForegroundColor Cyan }

function Show-InstallHelp {
    $exe = if ($PSVersionTable.PSEdition -eq 'Core') { 'pwsh' } else { 'powershell' }
    @"

  Promptdivers — installer (PowerShell)

  $($exe) -File ./install.ps1              Auto-detect IDEs, install skills globally
  $($exe) -File ./install.ps1 -Project .   Bootstrap AGENTS.md + CLAUDE + QUICK_REFERENCE + PROJECT_LOG
  $($exe) -File ./install.ps1 -Project . -VendorFramework
                                   Vendor the full pack into .framework-promptdivers2/ and install root stubs
  $($exe) -File ./install.ps1 -Project . -VendorFramework -FrameworkDir .framework-promptdivers2
                                   Override the vendored framework directory name
  $($exe) -File ./install.ps1 -Cursor      Cursor only (~/.cursor/skills)
  $($exe) -File ./install.ps1 -Claude      Claude Code only (~/.claude/skills)
  $($exe) -File ./install.ps1 -Help        This message

  Windows (classic PowerShell 5.1): powershell.exe -ExecutionPolicy Bypass -File .\install.ps1
  If scripts are blocked: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

  macOS / Linux: install pwsh (https://aka.ms/powershell), then use -File ./install.ps1 from the pack root.

"@
    | Write-Host
}

# Parse args (support -Project . and --project .)
$ProjectDir = ''
$ForceCursor = $false
$ForceClaude = $false
$VendorFramework = $false
$FrameworkDirName = '.framework-promptdivers2'

$raw = @($args)
$i = 0
while ($i -lt $raw.Count) {
    $a = [string]$raw[$i]
    if ($a -in @('--help', '--Help', '-Help', '-h')) {
        Show-InstallHelp
        exit 0
    }
    if ($a -in @('--project', '-Project')) {
        if ($i + 1 -ge $raw.Count -or [string]::IsNullOrWhiteSpace($raw[$i + 1])) {
            Write-PromptFail '-Project / --project requires a non-empty directory path'
            exit 1
        }
        $ProjectDir = [string]$raw[$i + 1].Trim()
        $i += 2
        continue
    }
    if ($a -in @('--vendor-framework', '-VendorFramework')) {
        $VendorFramework = $true
        $i++
        continue
    }
    if ($a -in @('--framework-dir', '-FrameworkDir')) {
        if ($i + 1 -ge $raw.Count -or [string]::IsNullOrWhiteSpace($raw[$i + 1])) {
            Write-PromptFail '-FrameworkDir / --framework-dir requires a non-empty directory name'
            exit 1
        }
        $FrameworkDirName = [string]$raw[$i + 1].Trim()
        $i += 2
        continue
    }
    if ($a -in @('--cursor', '-Cursor')) {
        $ForceCursor = $true
        $i++
        continue
    }
    if ($a -in @('--claude', '-Claude')) {
        $ForceClaude = $true
        $i++
        continue
    }
    Write-PromptWarn "Unknown argument: $a (skipping)"
    $i++
}

if (-not (Test-Path -LiteralPath $SkillsSrc -PathType Container)) {
    Write-PromptFail "Skills folder not found: $SkillsSrc (is the script inside the Promptdivers pack root?)"
    exit 1
}

function Ensure-Directory {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        $null = New-Item -ItemType Directory -Path $Path -Force
    }
}

function Install-SkillsTo {
    param([string]$DestRoot, [string]$IdeLabel)

    Ensure-Directory -Path $DestRoot

    foreach ($skill in $SkillNames) {
        $src = Join-Path $SkillsSrc $skill
        if (-not (Test-Path -LiteralPath $src -PathType Container)) {
            Write-PromptFail "Skill not found: $src"
            exit 1
        }
        $dest = Join-Path $DestRoot $skill
        if (Test-Path -LiteralPath $dest) {
            Remove-Item -LiteralPath $dest -Recurse -Force
        }
        Copy-Item -LiteralPath $src -Destination $dest -Recurse -Force
        Write-PromptOk "${IdeLabel} → $dest"
    }
}

function Vendor-FrameworkToProject {
    param([string]$ProjectRoot, [string]$FrameworkDirName)

    $frameworkRoot = Join-Path $ProjectRoot $FrameworkDirName
    Ensure-Directory -Path $frameworkRoot
    Write-PromptHeader \"📦 Vendoring framework → $frameworkRoot\"

    $paths = @(
        'AGENTS.md','CLAUDE.md','QUICK_REFERENCE.md','VERSION','CHANGELOG.md','README.md','README-ES.md','FIRST_MISSION.md',
        'docs','missions','protocols','scripts','squads','stratagems','templates','skills','.cursor','.github'
    )
    foreach ($p in $paths) {
        $src = Join-Path $PackDir $p
        if (Test-Path -LiteralPath $src) {
            Copy-Item -LiteralPath $src -Destination $frameworkRoot -Recurse -Force
        }
    }
    Write-PromptOk "Vendored Promptdivers pack into $FrameworkDirName/"

    $stubMap = @{
        'project-agents.stub.template.md' = 'AGENTS.md'
        'project-claude.stub.template.md' = 'CLAUDE.md'
        'project-quick-reference.stub.template.md' = 'QUICK_REFERENCE.md'
    }
    foreach ($k in $stubMap.Keys) {
        $stubSrc = Join-Path (Join-Path $PackDir 'templates') $k
        if (Test-Path -LiteralPath $stubSrc -PathType Leaf) {
            $dest = Join-Path $ProjectRoot $stubMap[$k]
            if (Test-Path -LiteralPath $dest) {
                Write-PromptWarn "$($stubMap[$k]) already exists in $ProjectRoot — skipping (delete first to overwrite)"
            } else {
                Copy-Item -LiteralPath $stubSrc -Destination $dest -Force
                Write-PromptOk "Created $($stubMap[$k]) (stub) → $ProjectRoot/"
            }
        }
    }
}

function Resolve-ExistingDirectory {
    param([string]$Path)
    try {
        $item = Get-Item -LiteralPath $Path -ErrorAction Stop
        if (-not $item.PSIsContainer) {
            return $null
        }
        return $item.FullName
    } catch {
        return $null
    }
}

Write-PromptHeader '🚀 Promptdivers — deployment begins'
Write-Host ''

# Home directory: $HOME is automatic in PowerShell; fall back for unusual hosts
$homeRaw = if (-not [string]::IsNullOrWhiteSpace($HOME)) {
    $HOME
} elseif ($IsWinOS -and -not [string]::IsNullOrWhiteSpace($env:USERPROFILE)) {
    $env:USERPROFILE
} elseif (-not [string]::IsNullOrWhiteSpace($env:HOME)) {
    $env:HOME
} else {
    (Get-Location).ProviderPath
}
$homeDir = [System.IO.Path]::GetFullPath($homeRaw)

$installed = 0

$claudeSkills = Join-Path (Join-Path $homeDir '.claude') 'skills'
$cursorSkills = Join-Path (Join-Path $homeDir '.cursor') 'skills'
$windsurfSkills = Join-Path (Join-Path $homeDir '.windsurf') 'skills'

$claudeDir = Join-Path $homeDir '.claude'
$cursorDir = Join-Path $homeDir '.cursor'
$windsurfDir = Join-Path $homeDir '.windsurf'

if ($ForceClaude -or ((-not $ForceCursor) -and (Test-Path -LiteralPath $claudeDir -PathType Container))) {
    Write-PromptLog 'Claude Code detected → installing to ~/.claude/skills/'
    Install-SkillsTo -DestRoot $claudeSkills -IdeLabel 'Claude Code'
    $installed++
}

if ($ForceCursor -or ((-not $ForceClaude) -and (Test-Path -LiteralPath $cursorDir -PathType Container))) {
    Write-PromptLog 'Cursor detected → installing to ~/.cursor/skills/'
    Install-SkillsTo -DestRoot $cursorSkills -IdeLabel 'Cursor'
    $installed++
}

if ((-not $ForceClaude) -and (-not $ForceCursor) -and (Test-Path -LiteralPath $windsurfDir -PathType Container)) {
    Write-PromptLog 'Windsurf detected → installing to ~/.windsurf/skills/'
    Install-SkillsTo -DestRoot $windsurfSkills -IdeLabel 'Windsurf'
    $installed++
}

if ($installed -eq 0) {
    Write-PromptWarn 'No IDE detected automatically.'
    Write-PromptWarn 'Run with -Cursor or -Claude to install to a specific IDE.'
    if ($IsWinOS) {
        Write-PromptWarn 'Example: pwsh -File .\install.ps1 -Cursor   or   powershell -File .\install.ps1 -Cursor'
    } else {
        Write-PromptWarn 'Example: pwsh -File ./install.ps1 -Cursor'
    }
}

if (-not [string]::IsNullOrWhiteSpace($ProjectDir)) {
    Write-Host ''
    Write-PromptHeader "📍 Bootstrapping project: $ProjectDir"

    # Expand ~ to home (common on macOS/Linux shells; PowerShell does not do this automatically)
    if ($ProjectDir.StartsWith('~')) {
        $tail = $ProjectDir.Substring(1).TrimStart('\', '/')
        if ([string]::IsNullOrWhiteSpace($tail)) {
            $ProjectDir = $homeDir
        } else {
            $ProjectDir = Join-Path $homeDir $tail
        }
    }

    $proj = Resolve-ExistingDirectory -Path $ProjectDir
    if (-not $proj) {
        Write-PromptFail "Directory does not exist: $ProjectDir"
        exit 1
    }

    if ($VendorFramework) {
        Vendor-FrameworkToProject -ProjectRoot $proj -FrameworkDirName $FrameworkDirName
    } else {
        foreach ($f in @('AGENTS.md', 'CLAUDE.md', 'QUICK_REFERENCE.md')) {
            $src = Join-Path $PackDir $f
            if (Test-Path -LiteralPath $src -PathType Leaf) {
                $dest = Join-Path $proj $f
                if (Test-Path -LiteralPath $dest) {
                    Write-PromptWarn "$f already exists in $proj — skipping (delete first to overwrite)"
                } else {
                    Copy-Item -LiteralPath $src -Destination $dest -Force
                    Write-PromptOk "Copied $f → $proj/"
                }
            }
        }
    }

    $logDest = Join-Path $proj 'PROJECT_LOG.md'
    if (-not (Test-Path -LiteralPath $logDest)) {
        $tpl = Join-Path (Join-Path $PackDir 'templates') 'project-log.template.md'
        if (-not (Test-Path -LiteralPath $tpl -PathType Leaf)) {
            Write-PromptFail "Template not found: $tpl"
            exit 1
        }
        Copy-Item -LiteralPath $tpl -Destination $logDest -Force
        Write-PromptOk 'Created PROJECT_LOG.md from template'
    } else {
        Write-PromptWarn 'PROJECT_LOG.md already exists — skipping'
    }

    Write-Host ''
    Write-PromptLog "Next: edit AGENTS.md in $proj — fill in your stack, permissions, and critical paths."
}

Write-Host ''
Write-PromptHeader '✅ FOR DEMOCRACY — deployment complete'
Write-Host ''
Write-Host "  Skills installed: $($SkillNames -join ' ')"
Write-Host ''
Write-Host '  What to do next:'
$nextInstall = if ($IsWinOS) {
    'pwsh -File .\install.ps1 -Project .   (or powershell -File .\install.ps1 -Project .)'
} else {
    'pwsh -File ./install.ps1 -Project .'
}
Write-Host "  1. Edit AGENTS.md in your project (or run: $nextInstall)"
Write-Host '  2. Open your IDE — skills load per your IDE (see README)'
Write-Host '  3. Say ''status'' to get a SITREP, ''debrief'' to close a session'
Write-Host ''
Write-Host '  Docs: README.md | Field guide: QUICK_REFERENCE.md'
Write-Host ''
