# app/services/rule_engine.py

def rule_based_score(tx):
    score = 0
    reasons = []

    if tx.amount > 10000:
        score += 0.4
        reasons.append("High amount")

    if tx.country not in ["FR", "BE"]:
        score += 0.3
        reasons.append("High risk country")

    if tx.frequency > 10:
        score += 0.3
        reasons.append("High frequency")

    return score, reasons