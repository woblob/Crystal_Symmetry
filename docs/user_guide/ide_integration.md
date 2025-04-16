# IDE Integration for Type Checking

This guide explains how to set up your IDE to work effectively with the type hints in the Crystal Symmetry project.

## Visual Studio Code

Visual Studio Code (VS Code) with the Python extension provides excellent support for type checking. The project includes a `.vscode/settings.json` file with recommended settings for optimal type checking.

### Recommended Extensions

Install the following VS Code extensions for the best experience:

1. **Python** (ms-python.python)
2. **Pylance** (ms-python.vscode-pylance)
3. **Black Formatter** (ms-python.black-formatter)
4. **isort** (ms-python.isort)

### Settings

The project's `.vscode/settings.json` file includes the following settings for type checking:

```json
{
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.diagnosticMode": "workspace",
    "python.analysis.autoImportCompletions": true,
    "python.analysis.extraPaths": [
        "${workspaceFolder}/stubs"
    ],
    "python.analysis.stubPath": "${workspaceFolder}/stubs",
    "python.linting.enabled": true,
    "python.linting.mypyEnabled": true,
    "python.linting.mypyArgs": [
        "--config-file=${workspaceFolder}/pyproject.toml"
    ]
}
```

These settings enable:
- Basic type checking with Pylance
- Workspace-wide diagnostics
- Auto-import completions
- Integration with the project's stub files
- mypy linting with the project's configuration

### Customizing Type Checking Severity

You can customize the severity of type checking issues in VS Code by adding the following to your settings:

```json
"python.analysis.diagnosticSeverityOverrides": {
    "reportUnusedImport": "warning",
    "reportUnusedVariable": "warning",
    "reportMissingTypeStubs": "information"
}
```

## PyCharm

PyCharm Professional provides excellent support for Python type hints. Here's how to set it up for optimal type checking:

### Enable Type Checking

1. Go to **File > Settings > Editor > Inspections > Python > Type Checker**
2. Check the **Enable type checker** option
3. Set the severity to **Warning**
4. Enable **Check variable annotations**

### Configure Stub Directories

1. Go to **File > Settings > Project > Project Structure**
2. Mark the `stubs` directory as a **Sources** folder (right-click and select **Sources**)

### Configure mypy Integration

1. Go to **File > Settings > Tools > External Tools**
2. Click the **+** button to add a new tool
3. Configure mypy:
   - Name: mypy
   - Program: mypy
   - Arguments: `--config-file=$ProjectFileDir$/pyproject.toml $FileDir$/$FileName$`
   - Working directory: `$ProjectFileDir$`

### Run Configurations

Create a run configuration for mypy:

1. Go to **Run > Edit Configurations**
2. Click the **+** button and select **Python**
3. Configure:
   - Name: mypy
   - Script path: `-m`
   - Parameters: `mypy --config-file=$ProjectFileDir$/pyproject.toml krysztalki`
   - Working directory: `$ProjectFileDir$`

## Other IDEs

For other IDEs, ensure they are configured to:

1. Recognize the `stubs` directory for type information
2. Use mypy with the project's `pyproject.toml` configuration
3. Enable Python type checking features

## Troubleshooting

### Missing Type Information

If your IDE doesn't recognize type information:

1. Ensure the IDE is configured to use the `stubs` directory
2. Check that the `py.typed` marker file is present in the package
3. Try restarting the IDE or its language server

### False Positives

If you encounter false positive type errors:

1. Check if the error is due to a missing stub file
2. Consider adding type ignores (`# type: ignore`) for specific lines
3. Update the stub files if necessary

### Performance Issues

If type checking is slow:

1. Consider using a more selective type checking mode
2. Exclude large third-party packages from type checking
3. Use incremental type checking if available
