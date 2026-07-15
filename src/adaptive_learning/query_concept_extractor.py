"""
query_concept_extractor.py

Production Query Concept Extractor

Features
--------
- Longest phrase matching
- Acronym support
- Alias support
- Hyphen normalization
- Plural normalization
- Overlap removal
- Duplicate removal
"""

import re


class QueryConceptExtractor:

    def __init__(self, vocabulary):

        self.aliases = {

            # -------------------------------------------------
            # Core ML
            # -------------------------------------------------

            "machine learning": "Machine Learning",
            "supervised learning": "Supervised Learning",
            "unsupervised learning": "Unsupervised Learning",

            "classification": "Classification",
            "regression": "Regression",
            "clustering": "Clustering",

            "decision tree": "Decision Tree",
            "random forest": "Random Forest",

            "linear regression": "Linear Regression",
            "logistic regression": "Logistic Regression",

            "support vector machine": "Support Vector Machine",
            "svm": "Support Vector Machine",

            "principal component analysis": "Principal Component Analysis",
            "pca": "Principal Component Analysis",

            "linear discriminant analysis": "Linear Discriminant Analysis",
            "lda": "Linear Discriminant Analysis",

            "k means": "K Means",
            "k-means": "K Means",
            "kmeans": "K Means",

            # -------------------------------------------------
            # Deep Learning
            # -------------------------------------------------

            "neural network": "Neural Network",
            "neural networks": "Neural Network",

            "convolutional neural network": "Convolutional Neural Network",
            "cnn": "Convolutional Neural Network",

            "recurrent neural network": "Recurrent Neural Network",
            "rnn": "Recurrent Neural Network",

            "long short term memory": "Long Short-Term Memory",
            "long short-term memory": "Long Short-Term Memory",
            "lstm": "Long Short-Term Memory",

            "gated recurrent unit": "Gated Recurrent Unit",
            "gru": "Gated Recurrent Unit",

            "graph neural network": "Graph Neural Network",
            "graph neural networks": "Graph Neural Network",
            "gnn": "Graph Neural Network",

            "transformer": "Transformer",
            "vision transformer": "Vision Transformer",

            "attention": "Attention",

            "bert": "BERT",
            "gpt": "GPT",

            # -------------------------------------------------
            # Optimization
            # -------------------------------------------------

            "gradient descent": "Gradient Descent",

            "stochastic gradient descent": "Stochastic Gradient Descent",

            "adam": "Adam Optimizer",

            "dropout": "Dropout",

            "backpropagation": "Backpropagation",

            # -------------------------------------------------
            # Model Evaluation
            # -------------------------------------------------

            "feature engineering": "Feature Engineering",

            "feature selection": "Feature Selection",

            "feature scaling": "Feature Scaling",

            "cross validation": "Cross Validation",
            "cross-validation": "Cross Validation",

            "train test split": "Train Test Split",

            "confusion matrix": "Confusion Matrix",

            "precision": "Precision",

            "recall": "Recall",

            "roc curve": "ROC Curve",

            "auc": "AUC",

            "overfitting": "Overfitting",

            "underfitting": "Underfitting",

            "bias variance": "Bias Variance Tradeoff",

            "bias variance tradeoff": "Bias Variance Tradeoff",

            "ensemble learning": "Ensemble Learning",

            "bagging": "Bagging",

            "boosting": "Boosting",

            "l1 regularization": "L1 Regularization",

            "l2 regularization": "L2 Regularization",

            # -------------------------------------------------
            # Modern AI / RAG
            # -------------------------------------------------

            "retrieval augmented generation": "Retrieval Augmented Generation",
            "retrieval-augmented generation": "Retrieval Augmented Generation",
            "rag": "Retrieval Augmented Generation",

            "knowledge graph": "Knowledge Graph",

            "graph guided rag": "Graph Guided RAG",
            "graph-guided rag": "Graph Guided RAG",

            "adaptive learning": "Adaptive Learning",

            "dense retrieval": "Dense Retrieval",

            "sparse retrieval": "Sparse Retrieval",

            "cosine similarity": "Cosine Similarity",

            "euclidean distance": "Euclidean Distance",

            "faiss": "FAISS",

            "transfer learning": "Transfer Learning",

            "xgboost": "XGBoost",

            "lightgbm": "LightGBM"

        }

        self.vocabulary = []

        seen = set()

        for concept in vocabulary:

            normalized = self._normalize(concept)

            if not normalized:
                continue

            if normalized in seen:
                continue

            seen.add(normalized)

            self.vocabulary.append(

                (concept, normalized)

            )

        self.vocabulary.sort(

            key=lambda item: len(item[1]),

            reverse=True

        )

    @staticmethod
    def _normalize(text):

        text = text.lower()

        text = text.replace("-", " ")

        text = re.sub(r"[^\w\s]", " ", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @staticmethod
    def _plural_to_singular(text):

        words = []

        for word in text.split():

            if len(word) > 3 and word.endswith("s"):

                word = word[:-1]

            words.append(word)

        return " ".join(words)

    def extract(self, query):

        query = self._normalize(query)

        query = self._plural_to_singular(query)

        detected = []

        occupied = []

        # ---------------------------------
        # Alias Matching
        # ---------------------------------

        for alias, concept in self.aliases.items():

            alias_norm = self._normalize(alias)

            pattern = r"\b" + re.escape(alias_norm) + r"\b"

            for match in re.finditer(pattern, query):

                start, end = match.span()

                overlap = False

                for s, e in occupied:

                    if start < e and end > s:

                        overlap = True

                        break

                if overlap:
                    continue

                occupied.append((start, end))

                if concept not in detected:

                    detected.append(concept)

        # ---------------------------------
        # Vocabulary Matching
        # ---------------------------------

        for original, normalized in self.vocabulary:

            pattern = r"\b" + re.escape(normalized) + r"\b"

            for match in re.finditer(pattern, query):

                start, end = match.span()

                overlap = False

                for s, e in occupied:

                    if start < e and end > s:

                        overlap = True

                        break

                if overlap:
                    continue

                occupied.append((start, end))

                if original not in detected:

                    detected.append(original)

        return detected