---
name: Git Guardrails
slug: git-guardrails
version: 1.0.0
homepage: https://github.com/AvilaCarlosDev/openclaw-skills/tree/main/git-guardrails
description: "Hooks y guardrails para bloquear comandos git peligrosos (push --force, reset --hard, clean) antes de que ejecuten."
changelog: "Skill inicial para protección de git en OpenClaw."
metadata: {"clawdbot":{"emoji":"🛡️","requires":{"bins":["git"]},"os":["linux","darwin","win32"],"configPaths":["~/git-guardrails/"]}}
---

## When to Use

Usa este skill cuando:
- Quieres prevenir accidentes con git (force push, hard reset)
- Trabajas en equipo y quieres proteger ramas compartidas
- Has perdido trabajo antes por comandos git peligrosos
- Para establecer convenciones de equipo sobre git

## Architecture

Configuración vive en `~/git-guardrails/` y hooks en el repo.

```
~/git-guardrails/
├── memory.md        # Configuración global, preferencias
└── templates/       # Templates de hooks reutilizables

<repo-root>/.git/hooks/
├── pre-commit       → Hooks instalados
├── pre-push         → ...
└── ...
```

## Dangerous Commands

### 🔴 Nivel: DESTRUCCIÓN TOTAL

| Comando | Qué hace | Por qué es peligroso |
|---------|----------|---------------------|
| `git push --force` | Sobrescribe historial remoto | Pierdes commits de otros |
| `git push --force-with-lease` | Fuerza con verificación | Menos peligroso, pero aún riesgoso |
| `git reset --hard HEAD~N` | Elimina N commits localmente | Pierdes trabajo irreversiblemente |
| `git clean -fd` | Elimina archivos no trackeados | Pierdes archivos no commiteados |
| `git filter-branch` | Reescribe historial | Puede corromper repo si se usa mal |

### 🟡 Nivel: RIESGO MODERADO

| Comando | Qué hace | Por qué es riesgoso |
|---------|----------|---------------------|
| `git rebase -i` | Reescribe historial interactivo | Puede perder commits si te equivocas |
| `git checkout -f` | Descarta cambios locales | Pierdes trabajo no commiteado |
| `git merge --abort` | Aborta merge en progreso | Pierdes trabajo del merge |
| `git stash drop` | Elimina stash | Pierdes cambios stasheados |

### 🟢 Nivel: SEGURO (pero verifica)

| Comando | Qué hace | Verificación recomendada |
|---------|----------|-------------------------|
| `git commit --amend` | Modifica último commit | Verifica que no hayas pusheado |
| `git revert` | Revierte commit | Verifica que es el commit correcto |
| `git cherry-pick` | Copia commit entre branches | Verifica que no haya conflictos |

## Guardrail Implementation

### Opción A: Git Hooks (Por Repo)

**Pre-push hook para bloquear force push:**

```bash
#!/bin/bash
# .git/hooks/pre-push

# Leer información del push
while read local_ref local_sha remote_ref remote_sha; do
  # Verificar si es force push
  if [ "$local_sha" = "0000000000000000000000000000000000000000" ]; then
    echo "⚠️  ERROR: Estás intentando borrar ramas remotas."
    echo "   Si es intencional, usa --no-verify para saltar este hook."
    exit 1
  fi
done

# Verificar ramas protegidas
protected_branches=("main" "master" "develop")
current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/refs/heads/,,')

for protected in "${protected_branches[@]}"; do
  if [ "$current_branch" = "$protected" ]; then
    echo "⚠️  ERROR: No se permite push directo a $protected."
    echo "   Crea un PR y pide review."
    exit 1
  fi
done

exit 0
```

**Pre-commit hook para verificar cambios:**

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Verificar que no haya secretos en los cambios
if git diff --cached | grep -iE "(password|secret|api_key|token)\s*[:=]" > /dev/null; then
  echo "⚠️  ERROR: Posible secreto detectado en cambios."
  echo "   Revisa que no estés commiteando credenciales."
  echo "   Si es un falso positivo, usa --no-verify."
  exit 1
fi

# Verificar que no haya archivos muy grandes
large_files=$(git diff --cached --name-only | xargs -I {} sh -c 'if [ -f "{}" ] && [ $(stat -f%z "{}" 2>/dev/null || stat -c%s "{}" 2>/dev/null) -gt 10485760 ]; then echo "{}"; fi')

if [ -n "$large_files" ]; then
  echo "⚠️  ERROR: Archivos >10MB detectados:"
  echo "$large_files"
  echo "   Considera usar Git LFS o no commitear estos archivos."
  exit 1
fi

exit 0
```

### Opción B: Alias Seguros

**Agrega a `~/.gitconfig`:**

```ini
[alias]
  # Force push seguro (requiere confirmación)
  push-force = "!f() { echo '⚠️  ¿Estás seguro de que quieres hacer force push?'; read -p 'Escribe YES para confirmar: ' confirm; if [ \"$confirm\" = \"YES\" ]; then git push --force-with-lease \"$@\"; else echo 'Cancelado.'; fi; }; f"
  
  # Reset hard con backup
  reset-hard-safe = "!f() { branch=$(git rev-parse --abbrev-ref HEAD); git branch backup-$branch-$(date +%Y%m%d-%H%M%S); git reset --hard \"$@\"; echo '✓ Backup creado. Puedes recuperar con: git checkout backup-...'; }; f"
  
  # Clean con preview
  clean-dry = clean -n
  clean-interactive = clean -i
  
  # Ver estado antes de commit
  pre-commit-check = "!f() { git status; git diff --stat; echo '---'; git diff --cached --name-only; }; f"
```

### Opción C: Husky + lint-staged (Para Teams)

**Setup con Husky:**

```bash
# Instalar
npm install -D husky lint-staged
npx husky install

# Agregar hook
npx husky add .husky/pre-push 'npx lint-staged'

# Configurar en package.json
{
  "lint-staged": {
    "*.{js,ts,jsx,tsx}": ["eslint --fix", "git add"],
    "*.{md,json}": ["prettier --write", "git add"]
  }
}
```

## Setup Script

**Script para instalar guardrails en un repo:**

```bash
#!/bin/bash
# install-git-guardrails.sh

echo "🛡️  Instalando Git Guardrails..."

REPO_ROOT=$(git rev-parse --show-toplevel)
HOOKS_DIR="$REPO_ROOT/.git/hooks"

# Crear pre-push hook
cat > "$HOOKS_DIR/pre-push" << 'EOF'
#!/bin/bash
# Git Guardrails: Pre-push hook

# Verificar ramas protegidas
protected_branches=("main" "master")
current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/refs/heads/,,')

for protected in "${protected_branches[@]}"; do
  if [ "$current_branch" = "$protected" ]; then
    echo "⚠️  ERROR: Push directo a $protected no permitido."
    echo "   Usa un Pull Request."
    exit 1
  fi
done

exit 0
EOF

chmod +x "$HOOKS_DIR/pre-push"

# Crear pre-commit hook
cat > "$HOOKS_DIR/pre-commit" << 'EOF'
#!/bin/bash
# Git Guardrails: Pre-commit hook

# Verificar secretos
if git diff --cached | grep -iE "(password|secret|api_key|token)\s*[:=]" > /dev/null; then
  echo "⚠️  ERROR: Posible secreto detectado."
  echo "   Usa --no-verify si es falso positivo."
  exit 1
fi

exit 0
EOF

chmod +x "$HOOKS_DIR/pre-commit"

echo "✓ Guardrails instalados en $REPO_ROOT"
echo "  Hooks activos: pre-push, pre-commit"
echo "  Para saltar un hook: git <command> --no-verify"
```

## Recovery Commands

**Cuando algo sale mal:**

```bash
# Recuperar commit "perdido"
git reflog
git checkout HEAD@{N}  # N = índice del reflog

# Recuperar stash eliminado (si no fue garbage collected)
git fsck --lost-found

# Deshacer último commit (sin perder cambios)
git reset --soft HEAD~1

# Deshacer merge
git merge --abort

# Recuperar archivo eliminado
git checkout HEAD -- path/to/file
```

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Hooks muy estrictos | El equipo los salta siempre | Empieza con guardrails mínimos, agrega gradualmente |
| Sin escape hatch | Bloquea casos legítimos | Siempre permite --no-verify para emergencias |
| Hooks no compartidos | Cada dev tiene reglas diferentes | Usa Husky o script de setup para compartir hooks |
| Sin backup | Reset hard pierde trabajo | Crea backup automático antes de operaciones peligrosas |
| Ignorar educación | Hooks no enseñan por qué | Incluye mensajes explicativos en los hooks |

## Adapt to the User

- **Para devs solitarios:** Guardrails mínimos, enfócate en backup y recovery
- **Para equipos pequeños:** Hooks compartidos, reglas consensuadas
- **Para empresas:** Guardrails estrictos, branches protegidos, required reviews
- **Para open source:** Pre-commit hooks para CI, branch protection rules

## Scope

Este skill SÓLO:
- Configura hooks y guardrails para git
- Previene comandos peligrosos
- Proporciona recovery commands
- Educa sobre prácticas seguras de git

Este skill NUNCA:
- Bloquea sin escape hatch (--no-verify siempre disponible)
- Modifica historial sin backup
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/git-guardrails/`:

- `memory.md` - Configuración global, preferencias
- `templates/` - Templates de hooks reutilizables

## Related Skills

- `issue-triage` - Para gestionar PRs en lugar de push directo
- `plan-to-issues` - Para trabajar con branches de feature
- `tdd-helper` - Para commits pequeños y frecuentes

## Feedback

- Si fue útil: `clawhub star git-guardrails`
- Mantente actualizado: `clawhub sync`
