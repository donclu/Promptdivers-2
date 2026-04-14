#!/usr/bin/env bash
# Promptdivers — Health Check Script
# Usage: ./scripts/health-check.sh [project-root]
# Checks if a project is properly configured for Promptdivers operations.

set -euo pipefail

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

PROJECT_ROOT="${1:-.}"
SCORE=0
TOTAL=0
ISSUES=()

# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

check() {
  local label="$1"
  local result="$2" # pass, warn, fail
  local detail="${3:-}"
  TOTAL=$((TOTAL + 1))

  case "$result" in
    pass)
      SCORE=$((SCORE + 1))
      printf "  ${GREEN}✅${NC} %s" "$label"
      ;;
    warn)
      printf "  ${YELLOW}🟡${NC} %s" "$label"
      ISSUES+=("🟡 $label: $detail")
      ;;
    fail)
      printf "  ${RED}🔴${NC} %s" "$label"
      ISSUES+=("🔴 $label: $detail")
      ;;
  esac

  if [ -n "$detail" ]; then
    printf " — %s" "$detail"
  fi
  printf "\n"
}

header() {
  printf "\n${BOLD}${CYAN}## %s${NC}\n\n" "$1"
}

# ─────────────────────────────────────────────
# Banner
# ─────────────────────────────────────────────

printf "\n${BOLD}${CYAN}╔══════════════════════════════════════════════╗${NC}\n"
printf "${BOLD}${CYAN}║   📋 PROMPTDIVERS — DEMOCRACY HEALTH CHECK  ║${NC}\n"
printf "${BOLD}${CYAN}╚══════════════════════════════════════════════╝${NC}\n"
printf "\nProject: ${BOLD}%s${NC}\n" "$(cd "$PROJECT_ROOT" && pwd)"

# ─────────────────────────────────────────────
# 1. Core Files
# ─────────────────────────────────────────────

header "1. Core Files"

if [ -f "$PROJECT_ROOT/AGENTS.md" ]; then
  # Check if stack section exists
  if grep -q "## Project stack" "$PROJECT_ROOT/AGENTS.md" 2>/dev/null || \
     grep -q "Language:" "$PROJECT_ROOT/AGENTS.md" 2>/dev/null; then
    check "AGENTS.md" "pass" "exists with stack section"
  else
    check "AGENTS.md" "warn" "exists but no stack section found"
  fi
else
  check "AGENTS.md" "fail" "missing — run install.sh --project or create manually"
fi

if [ -f "$PROJECT_ROOT/PROJECT_LOG.md" ]; then
  # Check for HANDOFF_JSON
  if grep -q "HANDOFF_JSON" "$PROJECT_ROOT/PROJECT_LOG.md" 2>/dev/null; then
    check "PROJECT_LOG.md" "pass" "exists with HANDOFF_JSON"
  else
    check "PROJECT_LOG.md" "warn" "exists but no HANDOFF_JSON block"
  fi
else
  check "PROJECT_LOG.md" "warn" "missing — recommended for session continuity"
fi

if [ -f "$PROJECT_ROOT/CLAUDE.md" ]; then
  check "CLAUDE.md" "pass" "exists"
elif [ -d "$PROJECT_ROOT/.cursor" ]; then
  check "CLAUDE.md" "warn" "missing but Cursor detected — may not be needed"
else
  check "CLAUDE.md" "warn" "missing — needed for Claude Code auto-load"
fi

if [ -f "$PROJECT_ROOT/QUICK_REFERENCE.md" ]; then
  check "QUICK_REFERENCE.md" "pass"
else
  check "QUICK_REFERENCE.md" "warn" "missing — copy from Promptdivers pack for quick access"
fi

# ─────────────────────────────────────────────
# 2. Squad & Protocol Files
# ─────────────────────────────────────────────

header "2. Squad & Protocol Availability"

SQUAD_COUNT=0
for squad in a b c d; do
  if [ -f "$PROJECT_ROOT/squads/squad-${squad}-"*.md ] 2>/dev/null; then
    SQUAD_COUNT=$((SQUAD_COUNT + 1))
  fi
done

if [ "$SQUAD_COUNT" -eq 4 ]; then
  check "Squad playbooks" "pass" "all 4 present (A/B/C/D)"
elif [ "$SQUAD_COUNT" -gt 0 ]; then
  check "Squad playbooks" "warn" "$SQUAD_COUNT/4 present"
else
  check "Squad playbooks" "warn" "none found — copy squads/ from pack if using squad workflow"
fi

if [ -d "$PROJECT_ROOT/protocols" ]; then
  PROTO_COUNT=$(find "$PROJECT_ROOT/protocols" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
  check "Protocols directory" "pass" "$PROTO_COUNT protocol files"
else
  check "Protocols directory" "warn" "missing — copy protocols/ from pack"
fi

if [ -d "$PROJECT_ROOT/stratagems" ]; then
  STRAT_COUNT=$(find "$PROJECT_ROOT/stratagems" -name "*.md" ! -name "README.md" 2>/dev/null | wc -l | tr -d ' ')
  check "Stratagems directory" "pass" "$STRAT_COUNT stratagems available"
else
  check "Stratagems directory" "warn" "missing — copy stratagems/ from pack for concrete actions"
fi

# ─────────────────────────────────────────────
# 3. Session Hygiene
# ─────────────────────────────────────────────

header "3. Session Hygiene"

if [ -f "$PROJECT_ROOT/PROJECT_LOG.md" ]; then
  # Check mission_status
  # grep returns exit code 1 when no matches; under `set -e` + `pipefail` we must tolerate that case.
  LAST_STATUS=$( (grep -o '"mission_status":\s*"[^"]*"' "$PROJECT_ROOT/PROJECT_LOG.md" 2>/dev/null || true) | tail -1 | sed 's/.*"\([^"]*\)"/\1/')
  if [ -n "$LAST_STATUS" ]; then
    case "$LAST_STATUS" in
      GREEN) check "Last mission status" "pass" "$LAST_STATUS" ;;
      YELLOW) check "Last mission status" "warn" "$LAST_STATUS — has partial objectives" ;;
      RED) check "Last mission status" "fail" "$LAST_STATUS — has failed objectives" ;;
      *) check "Last mission status" "warn" "unknown: $LAST_STATUS" ;;
    esac
  else
    check "Last mission status" "warn" "no mission_status found in log"
  fi

  # Check for DEBT items
  DEBT_COUNT=$(grep -c '\[DEBT-' "$PROJECT_ROOT/PROJECT_LOG.md" 2>/dev/null || true)
  if [ "$DEBT_COUNT" -gt 0 ]; then
    check "Technical debt" "warn" "$DEBT_COUNT DEBT items tracked"
  else
    check "Technical debt" "pass" "no unresolved DEBT items"
  fi

  # Check for open_tasks
  OPEN_TASKS=$(grep -c '"open_tasks"' "$PROJECT_ROOT/PROJECT_LOG.md" 2>/dev/null || true)
  if [ "$OPEN_TASKS" -gt 0 ]; then
    check "Open tasks tracked" "pass"
  else
    check "Open tasks tracked" "warn" "no open_tasks in HANDOFF_JSON"
  fi
else
  check "Last mission status" "warn" "no PROJECT_LOG — can't check"
  check "Technical debt" "warn" "no PROJECT_LOG — can't check"
  check "Open tasks tracked" "warn" "no PROJECT_LOG — can't check"
fi

# ─────────────────────────────────────────────
# 4. IDE Integration
# ─────────────────────────────────────────────

header "4. IDE Integration"

if [ -f "$PROJECT_ROOT/.cursor/rules/promptdivers-2.mdc" ] || \
   [ -f "$PROJECT_ROOT/.cursor/rules/promptdivers.mdc" ]; then
  check "Cursor rule" "pass"
else
  check "Cursor rule" "warn" "no .cursor/rules/promptdivers-2.mdc"
fi

if [ -f "$PROJECT_ROOT/.github/copilot-instructions.md" ]; then
  check "Copilot instructions" "pass"
else
  check "Copilot instructions" "warn" "no .github/copilot-instructions.md"
fi

# Check global skills
SKILLS_FOUND=false
for dir in "$HOME/.claude/skills" "$HOME/.cursor/skills" "$HOME/.windsurf/skills"; do
  if [ -d "$dir/promptdivers-orchestrator" ] 2>/dev/null; then
    SKILLS_FOUND=true
    check "Global skills ($dir)" "pass"
  fi
done
if [ "$SKILLS_FOUND" = false ]; then
  check "Global skills" "warn" "promptdivers-orchestrator not found — run install.sh"
fi

# ─────────────────────────────────────────────
# 5. Illuminate Risk
# ─────────────────────────────────────────────

header "5. Illuminate Risk Assessment"

# Check for common secret patterns
SECRET_PATTERNS='(API_KEY|SECRET_KEY|PASSWORD|PRIVATE_KEY|aws_access|sk-[a-zA-Z0-9])'
if [ -d "$PROJECT_ROOT/src" ] || [ -d "$PROJECT_ROOT/lib" ] || [ -d "$PROJECT_ROOT/app" ]; then
  SECRETS_FOUND=$(grep -rn -E "$SECRET_PATTERNS" "$PROJECT_ROOT" \
    --include="*.ts" --include="*.js" --include="*.py" --include="*.go" --include="*.rb" \
    --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=vendor --exclude-dir=venv \
    2>/dev/null | grep -v "\.env\." | grep -v "example" | grep -v "template" | head -5 | wc -l | tr -d ' ')
  if [ "$SECRETS_FOUND" -gt 0 ]; then
    check "Hardcoded secrets scan" "fail" "possible secrets found in source — review immediately"
  else
    check "Hardcoded secrets scan" "pass" "no obvious patterns in source"
  fi
else
  check "Hardcoded secrets scan" "pass" "no source directories to scan"
fi

if [ -f "$PROJECT_ROOT/.gitignore" ]; then
  if grep -q "\.env" "$PROJECT_ROOT/.gitignore" 2>/dev/null; then
    check ".gitignore covers .env" "pass"
  else
    check ".gitignore covers .env" "warn" ".env not in .gitignore"
  fi
else
  check ".gitignore" "warn" "no .gitignore found"
fi

# ─────────────────────────────────────────────
# Results
# ─────────────────────────────────────────────

header "SITREP — Democracy Health Score"

PERCENT=$((SCORE * 100 / TOTAL))

if [ $PERCENT -ge 90 ]; then
  LEVEL="🌟 Super Earth Hero"
  COLOR="$GREEN"
elif [ $PERCENT -ge 70 ]; then
  LEVEL="🏅 Skull Admiral"
  COLOR="$GREEN"
elif [ $PERCENT -ge 50 ]; then
  LEVEL="⚔️  Helldiver"
  COLOR="$YELLOW"
else
  LEVEL="💀 Cadet"
  COLOR="$RED"
fi

printf "  Score: ${BOLD}%d / %d${NC} (%d%%)\n" "$SCORE" "$TOTAL" "$PERCENT"
printf "  Level: ${COLOR}${BOLD}%s${NC}\n" "$LEVEL"

if [ ${#ISSUES[@]} -gt 0 ]; then
  printf "\n${BOLD}  Issues to address:${NC}\n"
  for issue in "${ISSUES[@]}"; do
    printf "    %s\n" "$issue"
  done
fi

printf "\n${CYAN}  Run: install.sh --project . to fix most setup issues.${NC}\n"
printf "${CYAN}  Run: Democracy Officer protocol for a deeper audit.${NC}\n\n"

# Exit code based on level
if [ $PERCENT -ge 70 ]; then
  exit 0  # Green: all good
elif [ $PERCENT -ge 50 ]; then
  exit 0  # Yellow: warnings but OK
else
  exit 1  # Red: critical issues
fi
