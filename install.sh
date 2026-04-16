#!/usr/bin/env bash
# Promptdivers — installer
# Installs skills to your IDE(s) and optionally bootstraps a project.
#
# Usage:
#   ./install.sh                    Auto-detect IDEs, install skills globally
#   ./install.sh --project <dir>    Copy AGENTS.md, CLAUDE.md, QUICK_REFERENCE.md into <dir>
#                                   and create PROJECT_LOG.md from template if missing
#   ./install.sh --project <dir> --vendor-framework
#                                   Vendor the full pack into <dir>/.framework-promptdivers2/
#                                   and install root stubs (AGENTS.md / CLAUDE.md / QUICK_REFERENCE.md)
#   ./install.sh --cursor           Install to Cursor only (~/.cursor/skills/)
#   ./install.sh --claude           Install to Claude Code only (~/.claude/skills/)
#   ./install.sh --help             Show this message
#
# Windows / PowerShell: use install.ps1 (same flags as --project / --cursor / --claude).

set -euo pipefail

PACK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly PACK_DIR
SKILLS_SRC="${PACK_DIR}/skills"
readonly SKILLS_SRC
SKILLS=(
  promptdivers-orchestrator
  promptdivers-pelican
  promptdivers-tactical-signals
  promptdivers-orbital-control
  promptdivers-ministry-of-truth
  promptdivers-stratagem-terminal
)
readonly SKILLS

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
RESET='\033[0m'

log()    { echo -e "${CYAN}[promptdivers]${RESET} $*"; }
ok()     { echo -e "${GREEN}  ✅ $*${RESET}"; }
warn()   { echo -e "${YELLOW}  ⚠️  $*${RESET}"; }
fail()   { echo -e "${RED}  ❌ $*${RESET}"; }
header() { echo -e "\n${CYAN}$*${RESET}"; }

if [[ "${1:-}" == "--help" ]]; then
  cat <<'EOF'

  Promptdivers — installer

  ./install.sh                  Auto-detect IDEs, install skills globally
  ./install.sh --project <dir>  Also bootstrap AGENTS.md + CLAUDE.md + QUICK_REFERENCE.md into <dir>, and create PROJECT_LOG.md from template
  ./install.sh --project <dir> --vendor-framework
                               Vendor the full pack into <dir>/.framework-promptdivers2/ and install root stubs
  ./install.sh --project <dir> --vendor-framework --framework-dir <name>
                               Override the vendored framework directory name
  ./install.sh --cursor         Install to Cursor only (~/.cursor/skills/)
  ./install.sh --claude         Install to Claude Code only (~/.claude/skills/)
  ./install.sh --help           Show this message

EOF
  exit 0
fi

PROJECT_DIR=""
FORCE_CURSOR=false
FORCE_CLAUDE=false
VENDOR_FRAMEWORK=false
FRAMEWORK_DIR_NAME=".framework-promptdivers2"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project)
      if [[ $# -lt 2 || -z "${2:-}" ]]; then
        fail "--project requires a non-empty directory path"
        exit 1
      fi
      PROJECT_DIR="$2"
      shift 2
      ;;
    --vendor-framework) VENDOR_FRAMEWORK=true; shift ;;
    --framework-dir)
      if [[ $# -lt 2 || -z "${2:-}" ]]; then
        fail "--framework-dir requires a non-empty directory name"
        exit 1
      fi
      FRAMEWORK_DIR_NAME="$2"
      shift 2
      ;;
    --cursor)  FORCE_CURSOR=true; shift ;;
    --claude)  FORCE_CLAUDE=true; shift ;;
    *)
      warn "Unknown argument: $1 (skipping)"
      shift
      ;;
  esac
done

install_skills() {
  local dest="$1"
  local ide_name="$2"
  local skill src
  mkdir -p "$dest"
  for skill in "${SKILLS[@]}"; do
    src="${SKILLS_SRC}/${skill}"
    if [[ -d "$src" ]]; then
      cp -R "$src" "${dest}/"
      ok "${ide_name} → ${dest}/${skill}"
    else
      fail "Skill not found: ${src}"
    fi
  done
}

vendor_framework() {
  local project_dir="$1"
  local framework_dir_name="$2"
  local local_framework
  local_framework="${project_dir}/${framework_dir_name}"

  mkdir -p "${local_framework}"
  header "📦 Vendoring framework → ${local_framework}"

  for p in AGENTS.md CLAUDE.md QUICK_REFERENCE.md VERSION CHANGELOG.md README.md README-ES.md FIRST_MISSION.md \
           docs missions protocols scripts squads stratagems templates skills experiments .cursor .github; do
    if [[ -e "${PACK_DIR}/${p}" ]]; then
      cp -R "${PACK_DIR}/${p}" "${local_framework}/"
    fi
  done
  ok "Vendored Promptdivers pack into ${framework_dir_name}/"

  for src in project-agents.stub.template.md project-claude.stub.template.md project-quick-reference.stub.template.md; do
    if [[ -f "${PACK_DIR}/templates/${src}" ]]; then
      local dest
      case "$src" in
        project-agents.stub.template.md) dest="AGENTS.md" ;;
        project-claude.stub.template.md) dest="CLAUDE.md" ;;
        project-quick-reference.stub.template.md) dest="QUICK_REFERENCE.md" ;;
        *) dest="${src/project-/}"; dest="${dest/.stub.template.md/.md}" ;;
      esac
      if [[ -f "${project_dir}/${dest}" ]]; then
        warn "${dest} already exists in ${project_dir} — skipping (delete first to overwrite)"
      else
        cp "${PACK_DIR}/templates/${src}" "${project_dir}/${dest}"
        ok "Created ${dest} (stub) → ${project_dir}/"
      fi
    fi
  done
}

header "🚀 Promptdivers — deployment begins"
echo ""

INSTALLED=0

if $FORCE_CLAUDE || { [[ $FORCE_CURSOR == false ]] && [[ -d "${HOME}/.claude" ]]; }; then
  log "Claude Code detected → installing to ~/.claude/skills/"
  install_skills "${HOME}/.claude/skills" "Claude Code"
  INSTALLED=$((INSTALLED + 1))
fi

if $FORCE_CURSOR || { [[ $FORCE_CLAUDE == false ]] && [[ -d "${HOME}/.cursor" ]]; }; then
  log "Cursor detected → installing to ~/.cursor/skills/"
  install_skills "${HOME}/.cursor/skills" "Cursor"
  INSTALLED=$((INSTALLED + 1))
fi

if [[ $FORCE_CLAUDE == false ]] && [[ $FORCE_CURSOR == false ]] && [[ -d "${HOME}/.windsurf" ]]; then
  log "Windsurf detected → installing to ~/.windsurf/skills/"
  install_skills "${HOME}/.windsurf/skills" "Windsurf"
  INSTALLED=$((INSTALLED + 1))
fi

if [[ $INSTALLED -eq 0 ]]; then
  warn "No IDE detected automatically."
  warn "Run with --cursor or --claude to install to a specific IDE."
  warn "Or install manually: cp -R skills/promptdivers-* ~/.claude/skills/"
fi

if [[ -n "${PROJECT_DIR}" ]]; then
  echo ""
  header "📍 Bootstrapping project: ${PROJECT_DIR}"

  if [[ ! -d "${PROJECT_DIR}" ]]; then
    fail "Directory does not exist: ${PROJECT_DIR}"
    exit 1
  fi

  if [[ "$VENDOR_FRAMEWORK" == true ]]; then
    vendor_framework "${PROJECT_DIR}" "${FRAMEWORK_DIR_NAME}"
  else
    for f in AGENTS.md CLAUDE.md QUICK_REFERENCE.md; do
      if [[ -f "${PACK_DIR}/${f}" ]]; then
        if [[ -f "${PROJECT_DIR}/${f}" ]]; then
          warn "${f} already exists in ${PROJECT_DIR} — skipping (delete first to overwrite)"
        else
          cp "${PACK_DIR}/${f}" "${PROJECT_DIR}/"
          ok "Copied ${f} → ${PROJECT_DIR}/"
        fi
      fi
    done
  fi

  if [[ ! -f "${PROJECT_DIR}/PROJECT_LOG.md" ]]; then
    cp "${PACK_DIR}/templates/project-log.template.md" "${PROJECT_DIR}/PROJECT_LOG.md"
    ok "Created PROJECT_LOG.md from template"
  else
    warn "PROJECT_LOG.md already exists — skipping"
  fi

  echo ""
  log "Next: edit AGENTS.md in ${PROJECT_DIR} — fill in your stack, permissions, and critical paths."
fi

echo ""
header "✅ FOR DEMOCRACY — deployment complete"
echo ""
echo "  Skills installed: ${SKILLS[*]}"
echo ""
echo "  What to do next:"
echo "  1. Edit AGENTS.md in your project (or run: ./install.sh --project .)"
echo "  2. Open your IDE and start a session — skills + pack doctrine load per your IDE (see README)"
echo "  3. Say 'status' to get a SITREP, 'debrief' to close a session"
echo ""
echo "  Docs: README.md | Field guide: QUICK_REFERENCE.md"
echo ""
