# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""RAG system function."""
from langchain_core.vectorstores import VectorStore
from langchain.agents.middleware import ModelRequest

__all__ = [
    'load_vector_store',
]


def load_vector_store(
    store: VectorStore,
    request: ModelRequest,
    prompt: str = """You are a smart agent helps the user's tasks.

You have access to the user's ducuments. The documents are:
---
"""
) -> str:
    """Loads the vector store and generates a system prompt.

    Args:
        store: The vector store accesser.
        request: The raw user request.
        prompt: The system prompt base text to be handed to the model.

    Returns:
        The system prompt constructed from the ``request``.
    """
    message = request.messages[-1].text
    docs_related = store.similarity_search(message)
    return prompt + '\n\n'.join([doc.page_content for doc in docs_related])
