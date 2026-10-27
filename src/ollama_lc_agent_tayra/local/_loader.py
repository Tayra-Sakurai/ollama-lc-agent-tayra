# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Loader modules."""
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from ..core import load_documents
from langchain_docling import DoclingLoader
from pathlib import Path

__all__ = [
    'create_loader',
    'create_vector_store',
    'local_load',
]


def create_loader(
    path: str | Path
) -> DoclingLoader:
    """Creates an instance of ``DoclingLoader``.

    Args:
        path: The path to folder of the document files.

    Returns:
        The loader instance.
    """
    p_obj = Path(path)
    plist: list[str] = []
    for p in p_obj.glob('**.pdf'):
        plist.append(str(p.resolve()))
    for p2 in p_obj.glob('**.docx'):
        plist.append(str(p2.resolve()))
    return DoclingLoader(plist)


def create_vector_store(
    persist_dir: str | Path,
    model: str = 'embeddinggemma:latest',
    dims: int = 768
) -> Chroma:
    """Creates a ChromaDb instance.

    Args:
        persist_dir: The persistent directory for the database.
        model: The model name.
        dims: The number of dimensions.

    Returns:
        The created ChromaDb connection.
    """
    p_obj = Path(persist_dir)
    embedding_function = OllamaEmbeddings(
        model=model,
        dimensions=dims
    )
    return Chroma(
        collection_name='doc_collection',
        embedding_function=embedding_function,
        persist_directory=str(p_obj.resolve())
    )


def local_load(
    path: str | Path,
    persist_dir: str | Path,
    model: str = 'embeddinggemma:latest',
    ndims: int = 768,
    chars: list[str] | None = None
) -> None:
    """Loading function for local system.

    Args:
        path: The path to the documents.
        persist_dir: The ChromaDb directory.
        model: The embedding model.
        ndims: The number of dimensions.
        chars: The delimiters.
    """
    loader = create_loader(path)
    chroma = create_vector_store(
        persist_dir,
        model,
        ndims
    )
    load_documents(
        loader,
        chroma,
        chars
    )
