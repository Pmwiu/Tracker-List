#!/usr/bin/env bash
# 应急回滚：列出最近10条提交，选择 hash 恢复，提交并推送
set -euo pipefail

BRANCH="${1:-main}"
echo "=== 最近 10 条提交 ==="
git log --oneline -10

echo
read -rp "输入要回滚到的提交 hash（留空取消）: " HASH
if [ -z "$HASH" ]; then
  echo "已取消。"
  exit 0
fi

if ! git cat-file -e "${HASH}^{commit}" 2>/dev/null; then
  echo "错误：无效的提交 hash。"
  exit 1
fi

echo "回滚到 ${HASH} ..."
git checkout "$HASH" -- .
git commit -m "rollback: restore to ${HASH}" || true
git push origin "$BRANCH"
echo "回滚完成。"
