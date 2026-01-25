#!/bin/bash
# Regenerate RAG-optimized versions of reference documentation
# Run this script whenever these reference files are updated:
#   - reference/admin-guide.md
#   - reference/approval-systems.md
#   - reference/approval-strategy-guide.md
#   - reference/can-do-list-format.md
#
# Usage: ./scripts/regenerate-rag-docs.sh

set -e
cd "$(dirname "$0")/.."

echo "=== Regenerating RAG-optimized documentation ==="

# 1. can-do-list-format.md - Simple conversion (small file, just change ## to ###)
echo "Processing can-do-list-format.md..."
sed 's/^## /### /g' reference/can-do-list-format.md > rag-optimized/can-do-list-format.md
echo "  Created rag-optimized/can-do-list-format.md"

# 2. approval-strategy-guide.md - Split into focused topic files
echo "Processing approval-strategy-guide.md..."
python3 scripts/split-approval-strategy.py
echo "  Created rag-optimized/approvals/*.md"

# 3. approval-systems.md - Split into focused topic files  
echo "Processing approval-systems.md..."
python3 scripts/split-approval-systems.py
echo "  Updated rag-optimized/approvals/*.md"

# 4. admin-guide.md - Split into focused topic files
echo "Processing admin-guide.md..."
python3 scripts/split-admin-guide.py
echo "  Created rag-optimized/admin/*.md"

echo ""
echo "=== RAG regeneration complete ==="
echo "Remember to: git add -A && git commit -m 'Regenerate RAG docs' && git push"
