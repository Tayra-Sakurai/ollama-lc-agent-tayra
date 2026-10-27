# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Document loading module."""
from langchain_core.document_loaders import BaseLoader
from langchain_core.vectorstores import VectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

__all__ = [
    'load_documents',
]


def load_documents(
    loader: BaseLoader,
    vectorstore: VectorStore,
    characters: list[str] | None = None
) -> None:
    """Loads documents using the selected loader.

    Args:
        loader: The loader.
        vectorstore: The vector store database adaptor.
        characters: The delimiters, optional.
    """
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        separators=characters,
        chunk_size=100,
        chunk_overlap=10
    )
    docs = splitter.split_documents(documents)
    for doc in docs:
        doc.metadata = { key: str(value) for key, value in doc.metadata.items() if isinstance(value, (str, int, float,)) }
    vectorstore.add_documents(docs)
