#!/usr/bin/env bash
# Patch comfyui-frontend-package to preserve workflow subdirectories.
# This script is idempotent — safe to run multiple times.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

# Find the main dialogService bundle (the one containing extractWorkflowFromAsset)
DIALOG_JS="$(grep -rl 'extractWorkflowFromAsset' .venv/lib/python*/site-packages/comfyui_frontend_package/static/assets/dialogService-*.js 2>/dev/null | head -n1 || true)"

if [ -z "$DIALOG_JS" ] || [ ! -f "$DIALOG_JS" ]; then
    echo "[!] Frontend dialogService JS not found — skipping patch"
    exit 0
fi

# Check if already patched
if grep -q '_sf=e.subfolder||e.user_metadata?.subfolder' "$DIALOG_JS"; then
    echo "[+] Frontend workflow-subdir patch already applied"
    exit 0
fi

echo "[+] Applying frontend workflow-subdir patch to: $DIALOG_JS"

python3 - "$DIALOG_JS" << 'PYEOF'
import sys

js_path = sys.argv[1]
with open(js_path, 'r') as f:
    content = f.read()

# Patch 1: extractWorkflowFromAsset — preserve asset subfolder
old1 = "async function extractWorkflowFromAsset(e){let t=e.name.replace(/\\.[^/.]+$/,`.json`),n=getOutputAssetMetadata(e.user_metadata);if(n?.jobId)"
new1 = "async function extractWorkflowFromAsset(e){let t=e.name.replace(/\\.[^/.]+$/,`.json`),n=getOutputAssetMetadata(e.user_metadata);let _sf=e.subfolder||e.user_metadata?.subfolder||``;if(_sf)t=_sf+`/`+t;if(n?.jobId)"

if old1 not in content:
    print("[!] Patch 1 target not found")
    sys.exit(1)
content = content.replace(old1, new1)

# Patch 2: createNewTemporary — inherit active workflow directory
old2 = "createNewTemporary=(e,t)=>createNewWorkflow(getUnconflictedPath(Sf.basePath+(e??`Unsaved Workflow.json`)),t)"
new2 = "createNewTemporary=(e,t)=>{let a=jO().workflow.activeWorkflow?.directory;if(a&&a.startsWith(Sf.basePath.slice(0,-1))&&(!e||!e.includes(`/`))){if(!a.endsWith(`/`))a+=`/`;return createNewWorkflow(getUnconflictedPath(a+(e??`Unsaved Workflow.json`)),t)}return createNewWorkflow(getUnconflictedPath(Sf.basePath+(e??`Unsaved Workflow.json`)),t)}"

if old2 not in content:
    print("[!] Patch 2 target not found")
    sys.exit(1)
content = content.replace(old2, new2)

# Patch 3: createTemporary — inherit active workflow directory
old3 = "createTemporary=(e,t)=>{let n=getUnconflictedPath(Sf.basePath+(e??`Unsaved Workflow.json`)),i=t?ensureWorkflowId(t):void 0;"
new3 = "createTemporary=(e,t)=>{let a=jO().workflow.activeWorkflow?.directory,b=Sf.basePath;if(a&&a.startsWith(Sf.basePath.slice(0,-1))&&(!e||!e.includes(`/`))){b=a;if(!b.endsWith(`/`))b+=`/`}let n=getUnconflictedPath(b+(e??`Unsaved Workflow.json`)),i=t?ensureWorkflowId(t):void 0;"

if old3 not in content:
    print("[!] Patch 3 target not found")
    sys.exit(1)
content = content.replace(old3, new3)

with open(js_path, 'w') as f:
    f.write(content)

print("[+] Patches applied successfully")
PYEOF

# Verify
if grep -q '_sf=e.subfolder||e.user_metadata?.subfolder' "$DIALOG_JS"; then
    echo "[+] Frontend patch verified"
else
    echo "[!] Frontend patch verification failed — please check $DIALOG_JS"
    exit 1
fi
