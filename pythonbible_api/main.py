"""pythonbible-api API endpoints."""

from __future__ import annotations

from typing import Any, Dict, List

import pythonbible as bible
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, Any]:
    """Hello World."""
    return {"message": "Hello World"}


@app.get("/verse/{verse_id:int}")
async def get_verse_from_id(verse_id: int) -> dict[str, Any]:
    """Return the verse for the given id."""
    reference: bible.NormalizedReference = bible.convert_verse_ids_to_references(
        [verse_id],
    )[0]
    book_titles: bible.formatter.BookTitles = bible.get_book_titles(reference.book)

    return {
        "id": verse_id,
        "reference": reference,
        "book_title": book_titles.short_title,
        "book_full_title": book_titles.long_title,
        "chapter": reference.start_chapter,
        "verse": reference.start_verse,
        "verse_text": bible.get_verse_text(verse_id),
    }


@app.get("/verse/{reference:str}")
async def get_verse_from_reference(reference: str) -> dict[str, Any]:
    """Return the verse for the given reference."""
    normalized_references: List[bible.NormalizedReference] = bible.get_references(
        reference,
    )

    if len(normalized_references) != 1:
        return "error - TODO"

    verse_ids: List[int] = bible.convert_references_to_verse_ids(normalized_references)

    if len(verse_ids) != 1:
        return "another error - TODO"

    book_titles: bible.formatter.BookTitles = bible.get_book_titles(
        normalized_references[0].book,
    )

    return {
        "id": verse_ids[0],
        "reference": normalized_references[0],
        "book_title": book_titles.short_title,
        "book_full_title": book_titles.long_title,
        "chapter": normalized_references[0].start_chapter,
        "verse": normalized_references[0].start_verse,
        "verse_text": bible.get_verse_text(verse_ids[0]),
    }


@app.get("/verses/{input_value:str}")
async def get_verses_from_reference(input_value: str) -> dict[str, Any]:
    """Return the verses for the given input value."""
    normalized_references: List[bible.NormalizedReference] = bible.get_references(
        input_value,
    )
    verse_ids: List[int] = bible.convert_references_to_verse_ids(normalized_references)
    verse_ids.sort()
    verses: List[Dict[str, Any]] = []
    verse_texts: List[str] = []

    for verse_id in verse_ids:
        reference: bible.NormalizedReference = bible.convert_verse_ids_to_references(
            [verse_id],
        )[0]
        book_titles: bible.formatter.BookTitles = bible.get_book_titles(reference.book)
        verse_text = bible.get_verse_text(verse_id)

        verses.append(
            {
                "id": verse_id,
                "reference": reference,
                "book_title": book_titles.short_title,
                "book_full_title": book_titles.long_title,
                "chapter": reference.start_chapter,
                "verse": reference.start_verse,
                "verse_text": verse_text,
            },
        )

        verse_texts.append(verse_text)

    return {"value": input_value, "verses": verses, "passage": "\n".join(verse_texts)}


@app.get("/references/{input_value:str}")
async def get_references(input_value: str) -> dict[str, Any]:
    """Return the normalized references for the given input value."""
    references: List[bible.NormalizedReference] = bible.get_references(input_value)

    return {
        "value": input_value,
        "references": references,
        "reference_string": bible.format_scripture_references(references),
    }
