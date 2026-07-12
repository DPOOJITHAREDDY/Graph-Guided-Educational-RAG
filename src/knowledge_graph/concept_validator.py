"""
concept_validator.py

Validates educational concepts using
rules, cache and Gemini.
"""

import json
from pathlib import Path

from src.llm.llm_factory import LLMFactory


class ConceptValidator:

    CACHE_FILE = Path(
        "resources/concept_validation_cache.json"
    )

    def __init__(self):

        self.model = LLMFactory().get_model()

        self.quick_reject = {

            "another",
            "different",
            "many",
            "multiple",
            "several",
            "various",
            "some",
            "other"

        }

        self.cache = self._load_cache()

    def _load_cache(self):

        if not self.CACHE_FILE.exists():
            return {}

        with open(
            self.CACHE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            cache = json.load(file)

        # -----------------------------
        # Migrate old boolean cache
        # -----------------------------

        migrated = {}

        changed = False

        for key, value in cache.items():

            if isinstance(value, bool):

                changed = True

                migrated[key] = {

                    "accepted": value,

                    "reason": "Migrated from old cache"

                }

            else:

                migrated[key] = value

        if changed:

            self.cache = migrated

            self._save_cache()

        return migrated

    def _save_cache(self):

        self.CACHE_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.CACHE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.cache,
                file,
                indent=4
            )

    def validate(
        self,
        concept
    ):

        key = concept.lower()

        # -----------------------------
        # Cache
        # -----------------------------

        if key in self.cache:

            return self.cache[key]

        # -----------------------------
        # Quick Reject
        # -----------------------------

        words = key.split()

        if words and words[0] in self.quick_reject:

            result = {

                "accepted": False,

                "reason": "Starts with descriptive word"

            }

            self.cache[key] = result

            self._save_cache()

            return result

        # -----------------------------
        # Gemini Validation
        # -----------------------------

        prompt = f"""
You are an expert in Machine Learning.

Determine whether the phrase below is an
established Machine Learning educational concept.

Reply ONLY in the following format.

YES|reason

or

NO|reason

Phrase:

{concept}
"""

        response = self.model.generate_content(
            prompt
        )

        answer = response.text.strip()

        try:

            status, reason = answer.split(
                "|",
                1
            )

            accepted = status.strip().upper() == "YES"

        except Exception:

            accepted = False

            reason = "Validator parsing failed"

        result = {

            "accepted": accepted,

            "reason": reason.strip()

        }

        self.cache[key] = result

        self._save_cache()

        return result