# TCL Firmware Discussion Hub - Local Dev Script
# Senior Engineer Version: Bootstraps Python & MkDocs automatically.

$ErrorActionPreference = "Stop"

# Ensure we are in the script's directory
Set-Location $PSScriptRoot

function Write-Step ([string]$msg) {
    Write-Host "`n🚀 $msg" -ForegroundColor Cyan
}

function Write-Success ([string]$msg) {
    Write-Host "✅ $msg" -ForegroundColor Green
}

function Write-Error-Custom ([string]$msg, [string]$help) {
    Write-Host "`n❌ ERROR: $msg" -ForegroundColor Red
    if ($help) {
        Write-Host "💡 HELP: $help" -ForegroundColor Yellow
    }
    Write-Host "`n[The script cannot continue. Please fix the issue and try again.]" -ForegroundColor Gray
    exit 1
}

Write-Step "Cleaning up old build artifacts..."
if (Test-Path "$PSScriptRoot/site") {
    Remove-Item -Path "$PSScriptRoot/site" -Recurse -Force
    Write-Success "Cleaned 'site' directory."
}

Write-Step "Checking Environment Readiness..."

# 1. Check for Python
try {
    $pythonVersion = python --version 2>&1
    Write-Success "Python detected ($pythonVersion)"
} catch {
    Write-Error-Custom "Python is not installed or not in your PATH." "Download it from https://www.python.org/downloads/"
}

# 2. Sync Dependencies
$reqPath = Join-Path $PSScriptRoot "requirements.txt"
if (Test-Path $reqPath) {
    Write-Step "Syncing Python dependencies (pip install)..."
    pip install -r $reqPath --quiet
    Write-Success "Dependencies are up-to-date."
} else {
    Write-Error-Custom "requirements.txt not found at $reqPath!" "This is a critical file for the project."
}

Write-Step "Launching MkDocs Dev Server..."
Write-Host "✨ The site will launch at http://127.0.0.1:8000/TCL-Discussion-Telegram/" -ForegroundColor Gray

# Start Browser in background
$url = "http://127.0.0.1:8000/TCL-Discussion-Telegram/"
Start-Job -ScriptBlock {
    param($url)
    Start-Sleep -Seconds 5
    Start-Process "explorer.exe" $url
} -ArgumentList $url | Out-Null

# Run MkDocs
python -m mkdocs serve
