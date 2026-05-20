from fastapi import APIRouter
from app.workflows.content_workflow import ContentWorkflow

router = APIRouter()


@router.get("/generate")
def generate(keyword: str = "AI"):

    workflow = ContentWorkflow()

    result = workflow.run(keyword)

    return result