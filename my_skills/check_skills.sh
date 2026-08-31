#!/usr/bin/env bash
# 技能组卫生检查：行数预算、Output Contract 一致性、references 链接完整性。
# 用法：my_skills/check_skills.sh（从仓库根运行）
set -u
cd "$(dirname "$0")"
fail=0

echo "== 1. SKILL.md 行数（预算 ≤150）"
for f in */SKILL.md; do
  n=$(wc -l < "$f")
  if [ "$n" -gt 150 ]; then echo "  超预算: $f = $n 行"; fail=1; else echo "  ok: $f = $n 行"; fi
done

echo "== 2. Output Contract 逐字一致"
ref=""
for f in */SKILL.md; do
  block=$(awk '/^## Output Contract/{flag=1;next} /^# /{if(flag)exit} flag' "$f")
  sum=$(printf '%s' "$block" | md5sum | cut -d' ' -f1)
  if [ -z "$ref" ]; then ref="$sum"; reffile="$f";
  elif [ "$sum" != "$ref" ]; then echo "  不一致: $f（基准 $reffile）"; fail=1; fi
done
[ "$fail" -eq 0 ] && echo "  ok: 全部一致"

echo "== 3. references 链接完整"
for f in */SKILL.md; do
  d=$(dirname "$f")
  grep -o 'references/[A-Za-z0-9._-]*' "$f" | sort -u | while read -r r; do
    [ -e "$d/$r" ] || echo "  悬空: $f -> $r"
  done
  for extra in paper-quality.md plotting-reference.md; do
    grep -q "\`$extra\`" "$f" && [ ! -e "$d/$extra" ] && echo "  悬空: $f -> $extra"
  done
done
echo "  检查完成"

exit $fail
