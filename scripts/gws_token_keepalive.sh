#!/bin/bash
# gws_token_keepalive.sh — 在 7 天过期窗口内主动刷新 OAuth token
#
# 由 launchd 每 5 天调用一次。流程：
#   1. 调用 gws auth status 检查 token 有效性
#   2. 有效 → 做一次轻量 Gmail API 调用触发 access_token 刷新
#   3. 无效 → 发送 macOS 桌面通知提醒用户手动 gws auth login

set -euo pipefail

GWS_BIN="${GWS_BIN:-gws}"
NOW=$(date -u +%Y-%m-%dT%H:%M:%S+00:00)

STATUS=$("$GWS_BIN" auth status 2>&1) || true

if echo "$STATUS" | grep -q '"token_valid": true'; then
    echo "[$NOW] token_keepalive: token valid, triggering refresh via getProfile"
    # 轻量 API 调用，确保 refresh token 被服务端承认并续期
    if "$GWS_BIN" gmail users getProfile --params '{"userId": "me"}' > /dev/null 2>&1; then
        echo "[$NOW] token_keepalive: refresh succeeded"
    else
        echo "[$NOW] token_keepalive: WARNING — API call failed, token may expire soon" >&2
        osascript -e 'display notification "Token refresh API 调用失败，请检查网络或运行 gws auth login" with title "⚠️ 邮件同步" subtitle "knowledge-bank"' 2>/dev/null || true
    fi
else
    echo "[$NOW] token_keepalive: TOKEN EXPIRED — manual login required" >&2
    osascript -e 'display notification "OAuth Token 已过期，请运行 gws auth login" with title "⚠️ 邮件同步" subtitle "knowledge-bank"' 2>/dev/null || true
fi
