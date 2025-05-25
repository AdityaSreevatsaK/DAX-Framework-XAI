"""
DAX-Framework-XAI: Domain-Aligned Explainability Selector

This script implements a minimal decision-support tool for selecting XAI methods
based on data modality, domain constraints, and explanation goals, following the
DAX (Domain-Aligned Explainability) Framework.

Author: Aditya Sreevatsa K
Date: 2025
"""

# Scoring table - Heuristic Weights
METHOD_SCORES = {
    "SHAP": [1.0, 0.2, 0.0, 1.0, 0.0, 0.0],
    "Anchors": [0.8, 0.6, 0.0, 0.9, 0.4, 0.0],
    "Permutation Importance": [1.0, 0.3, 0.0, 0.3, 0.0, 0.0],
    "Counterfactuals": [0.7, 0.6, 0.4, 0.8, 0.0, 0.5],
    "LIME": [0.3, 1.0, 0.3, 0.2, 1.0, 0.1],
    "Attention Maps": [0.0, 1.0, 0.2, 0.3, 1.0, 0.2],
    "Prompt Probes": [0.0, 1.0, 0.0, 0.2, 0.9, 0.0],
    "Grad-CAM": [0.0, 0.0, 1.0, 0.5, 0.0, 1.0],
    "Saliency Maps": [0.0, 0.0, 0.9, 0.3, 0.0, 0.9],
    "Integrated Gradients": [0.0, 0.0, 1.0, 0.4, 0.0, 1.0],
}

SCORE_DIMENSIONS = ["tabular", "text", "image", "legal", "token", "spatial"]


def dax_xai_selector(data_type, has_legal_constraints=False, needs_token_level=False, needs_spatial_localization=False,
                     top_n=5):
    """
    Rank XAI methods based on context using weighted heuristic scores.

    Parameters:
        data_type (str): 'tabular', 'text', or 'image'
        has_legal_constraints (bool)
        needs_token_level (bool)
        needs_spatial_localization (bool)
        top_n (int): How many top methods to return

    Returns:
        list of tuples: [(method_name, score), ...]
    """

    # Set query vector based on input context
    query_vector = [0] * 6
    if data_type.lower() == "tabular":
        query_vector[0] = 1
    elif data_type.lower() == "text":
        query_vector[1] = 1
    elif data_type.lower() == "image":
        query_vector[2] = 1

    if has_legal_constraints:
        query_vector[3] = 1
    if needs_token_level:
        query_vector[4] = 1
    if needs_spatial_localization:
        query_vector[5] = 1

    # Compute dot product score for each method
    scored_methods = []
    for method, weights in METHOD_SCORES.items():
        score = sum(w * q for w, q in zip(weights, query_vector))
        scored_methods.append((method, round(score, 3)))

    # Sort methods by score descending
    scored_methods.sort(key=lambda x: x[1], reverse=True)

    return scored_methods[:top_n]
