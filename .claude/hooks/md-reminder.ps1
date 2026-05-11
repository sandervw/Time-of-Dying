$payload = $input | ConvertFrom-Json

$path = $null
if ($payload.tool_input.PSObject.Properties.Name -contains 'file_path') {
    $path = $payload.tool_input.file_path
} elseif ($payload.tool_input.PSObject.Properties.Name -contains 'notebook_path') {
    $path = $payload.tool_input.notebook_path
}

if (-not $path -or $path -notmatch '\.md$') {
    exit 0
}

$reminder = @"
Reminder before writing/editing this markdown: would the text benefit from specific proper names, or from added setting-specific lore? If yes:
- For names: run `python sampling.py names 10` from setting/ (per CLAUDE.md naming guidelines), then invent NEW names inspired by the samples.
- For lore/setting: invoke the /tod-context skill.
Skip if the content is purely structural/meta (config, index, todo, etc.), or would not benefit from added names or lore.
"@

@{
    hookSpecificOutput = @{
        hookEventName = "PreToolUse"
        permissionDecision = "allow"
        additionalContext = $reminder
    }
} | ConvertTo-Json -Depth 5
