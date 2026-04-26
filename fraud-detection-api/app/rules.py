def rule_based_score(tx):
    score = 0
    reasons = []

    if tx.amount > 10000:
        score += 0.4
        reasons.append("High amount")

    if tx.country in ["IR", "KP"]:
        score += 0.3
        reasons.append("High-risk country")

    if tx.frequency > 20:
        score += 0.2
        reasons.append("High transactions frequency")

    if tx.account_age_days < 10:
        score += 0.2
        reasons.append("New account")

    return min(score, 1.0), ", ".join(reasons)