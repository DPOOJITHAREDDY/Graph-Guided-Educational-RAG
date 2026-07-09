"""
Prompts used for Knowledge Graph construction.
"""

CONCEPT_EXTRACTION_PROMPT = """
You are an expert educational knowledge extraction system.

Extract ONLY important educational concepts from the following textbook passage.

Rules:

1. Ignore examples.
2. Ignore numbers.
3. Ignore page numbers.
4. Ignore figures.
5. Ignore variable names.
6. Ignore mathematical values.
7. Ignore generic words.

Return ONLY JSON.

Format:

{
  "concepts":[
      {
          "name":"Decision Tree",
          "type":"Algorithm"
      }
  ]
}

Text:

{text}
"""