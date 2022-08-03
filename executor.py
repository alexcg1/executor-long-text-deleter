from jina import Executor, requests
from typing import Any, Dict
from docarray import DocumentArray


class LongTextDeleter(Executor):
    """
    If a Document's .text attribute is too long, delete the Document
    """

    def __init__(self, max_length=2000, traversal_paths: str = "@r", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_length = max_length
        self.traversal_paths = traversal_paths

    @requests(on="/index")
    def delete_long_text(self, docs: DocumentArray, parameters: Dict[str, Any], **kwargs):
        traversal_paths = parameters.get("traversal_paths", self.traversal_paths)

        for doc in docs[traversal_paths]:
            if doc.text:
                if len(doc.text) > self.max_length:
                    print("too long!")
                    del docs[doc.id]
