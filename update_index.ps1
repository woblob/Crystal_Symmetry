# PowerShell script to update the index file

# Define a colon character to avoid PowerShell parsing issues
$colon = [char]58

# Create main index file
$indexContent = "# Crystal Symmetry Project Tasks`n`n"
$indexContent += "This is an improved navigation structure for the tasks in the Crystal Symmetry project.`n`n"
$indexContent += "## Tasks`n`n"

for ($i = 1; $i -le 10; $i++) {
    $taskFile = "tasks/task_$($i.ToString("000")).txt"
    if (Test-Path $taskFile) {
        $content = Get-Content $taskFile -Raw
        
        # Extract task information
        if ($content -match "# Task ID$colon (\d+)") {
            $taskId = $matches[1]
        } else {
            $taskId = $i
        }
        
        if ($content -match "# Title$colon (.*)") {
            $taskTitle = $matches[1].Trim()
        } else {
            $taskTitle = "Task $i"
        }
        
        if ($content -match "# Status$colon (.*)") {
            $taskStatus = $matches[1].Trim()
        } else {
            $taskStatus = "unknown"
        }
        
        Write-Host "Adding task $taskId: $taskTitle - $taskStatus"
        $indexContent += "- [Task $taskId$colon $taskTitle](../task_$($i.ToString("000"))/overview.md) - $taskStatus`n"
    }
}

$indexContent += "`n## Important Note`n`n"
$indexContent += "This is a copy of the original tasks directory with an improved structure for navigation. "
$indexContent += "The original task files are still maintained in the main tasks directory and should be used "
$indexContent += "for interaction with Task Master. This structure is for documentation and navigation purposes only.`n"

# Write main index file
Set-Content -Path "tasks/docs/README/index.md" -Value $indexContent

Write-Host "Index file updated successfully"
