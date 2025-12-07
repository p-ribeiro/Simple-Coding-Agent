
execute_code_schema = {
    "type": "function",
    "name": "execute_code",
    "description": "Execute Python code and return result or error",
    "parameters": {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "Python code to execute as a string"
            }
        },
        "required": ["code"],
        "additionalProperties": False
    }
}

read_file_schema = {
    "type": "function",
    "name": "read_file",
    "description": "Reads content from a file with optional offset and limit for large files.",
    "parameters": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Absolute path to the file to read",
            },
            "limit": {
                "type": "number",
                "description": "Maximum number of characters to read",
            },
            "offset": {
                "type": "number",
                "description": "Starting position in the file",
            },
        },
        "required": ["file_path"],
        "additionalProperties": False,
    },
}

write_file_schema = {
    "type": "function",
    "name": "write_file",
    "description": "Writes content to a file, creating directories if needed.",
    "parameters": {
        "type": "object",
        "properties": {
            "content": {
                "type": "string",
                "description": "Content to write to the file",
            },
            "file_path": {
                "type": "string",
                "description": "Absolute path where the file will be written",
            },
        },
        "required": ["content", "file_path"],
        "additionalProperties": False,
    },
}



tools_schemas = [
    execute_code_schema,
    read_file_schema,
    write_file_schema,
]