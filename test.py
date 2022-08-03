from executor import LongTextDeleter
from docarray import Document, DocumentArray

docs = DocumentArray([Document(text=f"{'a'*5}"), Document(text=f"{'a'*5000}")])

print(docs)

exec = LongTextDeleter()

exec.delete_long_text(parameters={}, docs=docs)

print(docs)
