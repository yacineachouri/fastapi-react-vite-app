def rule_based_score(tx):
    score = 0

    if tx.amount > 10000:
        score += 0.4

    if tx.country in ["IR", "KP"]:
        score += 0.3

    if tx.frequency > 20:
        score += 0.2

    if tx.account_age_days < 10:
        score += 0.2

    return min(score, 1.0)