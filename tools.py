from e2b_code_interpreter import Sandbox
from typing import Callable, Optional
import json

def execute_code(sbx: Sandbox, code: str, language: str = "python") -> tuple[str, dict]:
    execution = sbx.run_code(code, language)
    metadata = {}
    results = execution.results
    
    for result in results:
        if result.png:
            metadata["images"] = [result.png]
            result.png = None
            result.chart = None
            
    return execution.to_json(), metadata

def read_file(sbx: Sandbox, file_path: str, limit: Optional[int] = 16, offset: int = 0) -> str:
    data = sbx.files.read(file_path)
    
    return data[offset:offset + limit if limit else None]

def write_file(sbx: Sandbox, content: str, file_path: str):
    sbx.files.write(file_path, content)
    return "OK"
    
    
tools = {
    "execute_code" : execute_code,
    "read_file": read_file,
    "write_file": write_file
}

def execute_tool(name: str, args: str, tools: dict[str, Callable], **kwargs):
    try:
        parsed_args = json.loads(args)
        if not isinstance(parsed_args, dict):
            return {"error": f"{name} expected a JSON object (mapping), got {type(parsed_args).__name__}"}

        if name not in tools:
            return {"error": f"Tool {name} does not exist."}
        
        result = tools[name](**parsed_args, **kwargs)
    except json.JSONDecodeError as e:
        result = {"error": f"{name} failed to parse arguments: {str(e)}"}
    except KeyError as e:
        result = {"error": f"Missing keys in arguments: {str(e)}"}    
    except Exception as e:
       result = {"error": str(e)}
    
    return result 

    
        
        