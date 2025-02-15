from fastapi import FastAPI, HTTPException, Query
from app.agent import Agent
from app.config import DATA_DIR

app = FastAPI(title="LLM-based Automation Agent")

# Initialize the automation agent
agent = Agent()

@app.post("/run")
async def run_task(task: str = Query(..., description="Plain‑English task description")):
    try:
        result = agent.run_task(task)
        return {"status": "success", "result": result}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Agent error: " + str(e))

@app.get("/read")
async def read_file(path: str = Query(..., description="File path within /data")):
    from app.utils.file_utils import read_file_safe
    try:
        content = read_file_safe(path)
        return {"status": "success", "content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error reading file: " + str(e))