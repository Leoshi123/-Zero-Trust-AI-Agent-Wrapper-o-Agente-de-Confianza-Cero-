# 🛡️ AIGatekeeper (Agente de Confianza Cero)

[![Tests](https://github.com/Leoshi123/AIGatekeeper/actions/workflows/ci.yml/badge.svg)](https://github.com/Leoshi123/AIGatekeeper/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/Leoshi123/AIGatekeeper/branch/main/graph/badge.svg)](https://codecov.io/gh/Leoshi123/AIGatekeeper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

> 🌐 Available in: English, Español

**"No confíes en la IA, verifica el contexto, limpia el rastro."**

Middleware de seguridad y optimización para desarrolladores que usan agentes de IA. Detecta código zombi, prompt injection, y limpia metadata sensible.

---

## ⚡ Quick Start

**Una línea para instalar:**

```bash
# Linux / macOS
curl -fsSL https://raw.githubusercontent.com/Leoshi123/AIGatekeeper/main/install.sh | bash
```

**En tu proyecto:**

```bash
# 1. Inicializar
aigatekeeper init

# 2. Detectar prompt injection
aigatekeeper scan-prompt "Ignore all previous instructions"

# 3. Listar prompts predefinidos
aigatekeeper prompt list

# 4. Push seguro (scan + sanitize + commit + push)
aigatekeeper push "feat: add security layer"
```

Alias corto: `ag` en vez de `aigatekeeper`

---

## 🚀 v1.1.0 - CLI Productivo

> 📢 **Próximamente**: Migración a **C/C++** para máxima performance. Ver [Roadmap](#-roadmap).

### Novedades en esta versión

| Feature | Descripción |
|---------|-------------|
| 🆕 `aigatekeeper init` | Registra proyecto, detecta stack, crea `.aigatekeeper/` |
| 🆕 `aigatekeeper prompt` | Templates predefinidos (security-audit, tdd-mode, code-review) |
| 🆕 `aigatekeeper scan-prompt` | Detecta 4 vectores de prompt injection |
| 🆕 `aigatekeeper push` | `git add + scan + sanitize + commit + push` en un comando |
| 🆕 Entry points | `aigatekeeper` y `ag` disponibles directamente en PATH |

### Comandos del CLI

```bash
aigatekeeper --help

Commands:
  init         Registra el proyecto actual
  prompt       Gestiona templates de prompts
  scan-prompt  Escanea en busca de prompt injection
  push         Secure push: git + scan + sanitize
  shield       Detector de código zombi
  sanitize     Limpiador de metadata
  prune        Podador de contexto AST
  hooks        Git hooks de seguridad
  demo         Demo completa
```

---

## 🛡️ Características

| Capa | Protección |
|------|------------|
| 🧹 **Metadata Cleaner** | Elimina comentarios de IA, rutas absolutas, firmas de modelos |
| 🔑 **Secret Detector** | Bloquea API keys, tokens, credenciales |
| ⚠️ **Zombie Code Detector** | Detecta +60 patrones vulnerables en 9 lenguajes |
| 🎭 **Prompt Injection Detector** | 4 vectores: direct, indirect, jailbreak, role-play |
| 🪝 **Git Hooks** | Escaneo automático en cada commit/push |
| 🤖 **MCP Server** | Integración nativa con Claude Code, Cursor, OpenCode, Windsurf |

### Lenguajes Soportados

| Lenguaje | Patrones | Código Zombi | Prompt Injection |
|----------|---------|:-------------:|:----------------:|
| 🐍 Python | 24 | ✅ | ✅ |
| 💻 JavaScript/Node.js | 20+ | ✅ | ✅ |
| 📘 TypeScript | 15+ | ✅ | ✅ |
| 🔥 Go | 6 | ✅ | - |
| 🦀 Rust | 5 | ✅ | - |
| ☕ Java | 4 | ✅ | - |
| 🔧 C/C++ | 4 | ✅ | - |
| 🐘 PHP | 15+ | ✅ | - |
| ⚛️ React 19 | 10+ | ✅ | - |

---

## 📦 Instalación

### Método 1: curl | bash (Recomendado)

```bash
# Linux / macOS / CachyOS
curl -fsSL https://raw.githubusercontent.com/Leoshi123/AIGatekeeper/main/install.sh | bash
```

### Método 2: Manual

```bash
git clone https://github.com/Leoshi123/AIGatekeeper.git
cd AIGatekeeper

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate    # Windows

pip install -e .
```

### Método 3: PowerShell (Windows)

```powershell
.\install.ps1
```

### Verificar instalación

```bash
aigatekeeper --version
ag --help
```

---

## 🎯 Prompt Injection Detection

Nuevo en v1.1.0: protección contra el vector #1 contra sistemas aumentados con IA.

```bash
# Scan rápido
aigatekeeper scan-prompt "Ignore all previous instructions. DAN mode activated"
```

**Output:**
```
🔍 Escaneando en busca de prompt injection...

⚠️  Detectados 2 hallazgos:

🟡 [MEDIUM] direct-injection
   Match: Ignore all previous instructions
   💡 Intento de ignorar instrucciones previas del sistema

🔴 [HIGH] jailbreak
   Match: DAN
   💡 Posible intento de jailbreak (DAN u homologo)
```

### Categorías detectadas

| Categoría | Severidad típica | Ejemplo |
|-----------|:----------------:|---------|
| **Direct Injection** | MEDIUM | "Ignore all previous instructions" |
| **Indirect Injection** | LOW | `---BEGIN INSTRUCTIONS---` embebido |
| **Jailbreak** | **HIGH** | "DAN", "act as if you have no rules" |
| **Role-Play Hijacking** | **HIGH** | "This is your new system prompt" |

---

## 📋 Templates de Prompts

Activa modos especializados para tu agente IA:

```bash
# Ver disponibles
aigatekeeper prompt list

# Activa uno
aigatekeeper prompt apply security-audit
```

| Prompt | Cuándo usarlo |
|--------|---------------|
| `security-audit` | Auditorías exhaustivas de seguridad |
| `code-review` | Antes de merges y PRs grandes |
| `tdd-mode` | Ciclo TDD estricto: RED → GREEN → REFACTOR |
| `refactor-mode` | Limpieza de deuda técnica |

---

## 🤖 MCP Server

Exponé AIGatekeeper a cualquier agente compatible con MCP.

### Tools disponibles

| Tool | Descripción |
|------|-------------|
| `sanitize_code` | Limpia metadata de IA, secretos, rutas |
| `scan_code` | Detecta patrones vulnerables |
| `scan_directory` | Escaneo recursivo de directorio |
| `scan_prompt` | **NUEVO** - Detecta prompt injection |
| `prune_context` | Extrae contexto mínimo via AST |
| `clean_code` | Limpieza rápida de metadata |

### Configuración en OpenCode

Ya agregado automáticamente via `install.sh`. Verifica:

```json
// ~/.config/opencode/opencode.json
{
  "mcp": {
    "aigatekeeper": {
      "command": ["/path/to/.venv/bin/python", "-m", "src.mcp_server"],
      "cwd": "/path/to/AIGatekeeper",
      "type": "local"
    }
  }
}
```

Reinicia OpenCode para que aparezca en la lista MCP.

---

## 🌐 Web Dashboard

Interfaz visual para escaneos y stats:

```bash
python server.py
```

Abre: **http://localhost:4901**

Features:
- 📊 Stats en tiempo real
- 🔍 Scanner interactivo
- 🧹 Sanitizador visual
- 📜 Historial de actividad
- 🌙 Dark mode

---

## 📁 Estructura del Proyecto

```
AIGatekeeper/
├── pyproject.toml          # Entry points: aigatekeeper, ag
├── install.sh              # curl | bash installer
├── install.ps1             # Windows installer
├── server.py               # Web Dashboard
├── src/
│   ├── cli.py              # CLI principal
│   ├── cli_extensions.py   # Comandos nuevos (v1.1.0)
│   ├── cli_prompts/        # Templates de prompts
│   │   ├── security-audit.md
│   │   ├── code-review.md
│   │   ├── tdd-mode.md
│   │   └── refactor-mode.md
│   ├── mcp_server.py       # MCP Server
│   ├── detector/
│   │   ├── __init__.py
│   │   └── injection_detector.py   # Prompt injection (v1.1.0)
│   ├── sanitizer/
│   ├── ast_parser/
│   └── wrapper/
├── tests/
│   ├── test_injection_detector.py  # 15 tests (v1.1.0)
│   └── ...
└── .aigatekeeper/          # Creado por `aigatekeeper init`
    └── config.json
```

---

## 🔧 Configuración por Proyecto

```bash
aigatekeeper init
```

Crea `.aigatekeeper/config.json`:

```json
{
  "project_id": "mi-proyecto",
  "initialized_at": "2026-05-26T...",
  "stack": ["Python (pip)", "Git repository"],
  "test_framework": "pytest",
  "settings": {
    "scan_on_commit": true,
    "scan_on_push": true,
    "prompt_injection_enabled": true,
    "zombie_code_enabled": true
  },
  "active_prompt": "security-audit"
}
```

---

## 🗺️ Roadmap

> 📢 **Anuncio**: Próximamente migración del **core a C/C++**

### Por qué C/C++?

| Factor | Python Actual | C/C++ Futuro |
|--------|:-------------:|:------------:|
| Velocidad escaneo | Referencia | **~50-100x más rápido** |
| Memoria | Alto | **Muy bajo** |
| Embebible | No | **Sí** (estático) |
| Startup time | ~100-300ms | **~1ms** |
| Distribución | Python requerido | **Binario standalone** |

### Versiones Planificadas

| Versión | Estado | Feature |
|---------|:------:|---------|
| **v1.0.0** | ✅ | Release inicial |
| **v1.0.1** | ✅ | Multi-lenguaje + MCP Server |
| **v1.0.2** | ✅ | MCP Resilience + Indestructible Server |
| **v1.0.3** | ✅ | Web Dashboard |
| **v1.0.5** | ✅ | Adversarial Testing |
| **v1.1.0** | 🚀 | **CLI Productivo + Prompt Injection** (actual) |
| **v2.0.0** | 📅 | **Migración Core a C/C++** |
| **v2.1.0** | 📅 | Bindings: Python, Node.js, Go |
| **v3.0.0** | 📅 | Engine de ML para detección avanzada |

### v2.0.0 - Migración C/C++ (Próximamente)

Arquitectura planeada:

```
┌─────────────────────────────────────────────────────────┐
│                  CLI Layer (Python mantenido)            │
│  aigatekeeper init | prompt | scan-prompt | push         │
├─────────────────────────────────────────────────────────┤
│                  FFI / Bindings Layer                    │
│         Python → C API / Node.js N-API / Go cgo         │
├─────────────────────────────────────────────────────────┤
│                  Core Engine (C/C++)                     │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────┐   │
│  │   Scanner   │ │   Sanitizer │ │  AST Optimizer  │   │
│  │   (regex)   │ │  (patterns) │ │ (tree-sitter)   │   │
│  └─────────────┘ └─────────────┘ └─────────────────┘   │
│  ┌─────────────────────────────────────────────────┐    │
│  │     Prompt Injection Engine (nuevo en v2)      │    │
│  │  • Heuristic patterns  • Semantic analysis      │    │
│  │  • ML inference opcional • Obfuscation resistant│    │
│  └─────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────┤
│                  Distribución                            │
│  • Binario standalone (no Python requerido)              │
│  • ~5-10MB comprimido                                    │
│  • Windows / Linux / macOS / ARM                         │
└─────────────────────────────────────────────────────────┘
```

**Mantendremos compatibilidad total**:
- CLI Python existente funcionará igual
- MCP Server sin cambios
- APIs públicas preservadas
- Solo el motor interno cambia

---

## 🤝 Contribuir

1. Fork el repositorio
2. Crea branch: `git checkout -b feature/tu-feature`
3. Implementa cambios
4. Agrega tests: `pytest tests/`
5. Commit y push
6. Crea Pull Request

Ver también: [CONTRIBUTING.md](CONTRIBUTING.md) (si existe)

---

## 📄 Licencia

MIT License - ver [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

- [MoureDev](https://moure.dev) - Inspiración de aprendizaje continuo
- [Gentleman Programming](https://gentlemanprogramming.com) - Filosofía de calidad
- [Comunidad Discord](https://discord.com/invite/gentleman-programming-769863833996754944) - Apoyo constante

---

**🛡️ Hecho con ❤️ para la comunidad**

> **"La seguridad no es un feature, es un requisito."**
