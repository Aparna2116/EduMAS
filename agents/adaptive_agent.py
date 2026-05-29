from memory.sqlite_store import get_sessions


def determine_next_level(student_id: str, current_level: str):

    sessions = get_sessions(student_id)
    sessions = [session for session in sessions if session["score"] > 0]

    if len(sessions) == 0:
        return {
            "recommended_level": current_level,
            "reason": "No previous sessions found"
        }

    recent_sessions = sessions[:3]

    average_score = sum(
        session["score"] for session in recent_sessions
    ) / len(recent_sessions)

    if average_score >= 85:

        if current_level == "beginner":
            next_level = "intermediate"

        elif current_level == "intermediate":
            next_level = "advanced"

        else:
            next_level = "advanced"

        reason = f"High performance detected ({average_score:.2f}%)"

    elif average_score < 60:

        if current_level == "advanced":
            next_level = "intermediate"

        elif current_level == "intermediate":
            next_level = "beginner"

        else:
            next_level = "beginner"

        reason = f"Low performance detected ({average_score:.2f}%)"

    else:

        next_level = current_level

        reason = f"Stable performance ({average_score:.2f}%)"

    return {
        "recommended_level": next_level,
        "average_score": average_score,
        "reason": reason
    }